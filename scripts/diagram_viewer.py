"""
View this repository on github: https://github.com/Jothin-kumar/Geometry-app

MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import global_variables
import gui
import shapes
from current_mode import get_current_shape, set_point_modify_mode
from shape_panels import refresh_all as refresh_all_panels

previous_point_property = None
previous_highlighted_point = None


def on_diagram_editor_click(event):  # When user clicks on the diagram editor.
    x = (int(event.x / 50) * 50) + 25
    y = (int(event.y / 50) * 50) + 25
    current_shape = get_current_shape()
    if current_shape == 'point':  # If current shape is Point, Just create a new point where clicked.
        global previous_point_property
        global previous_highlighted_point
        import current_mode
        if current_mode.point_modify_mode:
            previous_highlighted_point.set_coordinates(x, y)
            current_mode.point_modify_mode = False
            for line in global_variables.get_value('lines'):
                if line.point1.x == previous_highlighted_point.x and line.point1.y == previous_highlighted_point.y:
                    line.point1 = shapes.get_point_by_coordinates(x, y)
                elif line.point2.x == previous_highlighted_point.x and line.point2.y == previous_highlighted_point.y:
                    line.point2 = shapes.get_point_by_coordinates(x, y)
                global_variables.get_value('refresh_line')(line)
        else:
            try:  # Try to create a Point.
                shapes.point(x, y, gui.create_text, gui.delete)  # Create a point.
            except ValueError:  # In case it already exists, do nothing.
                pass
        if previous_highlighted_point:  # If previous highlighted point is not None.
            previous_highlighted_point.unhighlight()  # Un-Highlight.
        if previous_point_property:  # If previous point property is not None.
            previous_point_property.delete()  # Delete it.
        point = shapes.get_point_by_coordinates(x, y)  # Get point object from it's coordinates.
        if point:
            point.highlight()  # Highlight the point.
        previous_point_property = gui.PointPropertyPane(point, shapes.refresh_all, point_modify_command=set_point_modify_mode)
        # When called next time, this is previous.
        previous_highlighted_point = point  # When called next time, this point is the previously highlighted one.
    elif current_shape == 'line':  # If current shape is line, Draw line from previous clicked coordinate to here.
        current_click_point = shapes.get_point_by_coordinates(x, y)
        if global_variables.get_value('previous_click_point') and current_click_point:
            # If the Point 'previous_click_point' and 'current_click_point' exists.
            try:  # Try to create a line.
                shapes.line(global_variables.get_value('previous_click_point'), current_click_point, gui.create_line,
                            gui.delete)  # Create a line.
            except ValueError:  # In case it already exists, do nothing.
                pass
        global_variables.set_value('previous_click_point', current_click_point)
    shapes.refresh_all()
    refresh_all_panels()


def trigger():
    gui.on_diagram_viewer_click(on_diagram_editor_click)
