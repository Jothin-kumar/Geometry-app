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

Author: Jothin kumar (https://jothin.tech)
Github repository of this project: https://github.com/Jothin-kumar/Geometry-app
"""
import current_mode
import global_variables
import gui
import shapes
from highlighted_shapes import unhighlight_all_lines, unhighlight_all_points
from shapes import refresh_all as _refresh_all

points_pane = gui.ShapePane(shape_name='Points',
                            switch_to_this_shape_command=current_mode.switch_to_point_edit)  # The points panel.
lines_pane = gui.ShapePane(shape_name='Lines',
                           switch_to_this_shape_command=current_mode.switch_to_line_edit)  # The lines panel.
angle_pane = gui.ShapePane(shape_name='Angles', switch_to_this_shape_command=current_mode.switch_to_angle_mode)
collinear_points_pane = gui.ShapePane('Collinear points',
                                      switch_to_this_shape_command=current_mode.switch_to_collinear_points_mode)
parallel_lines_pane = gui.ShapePane('Parallel lines',
                                    switch_to_this_shape_command=current_mode.switch_to_parallel_lines_mode)


def refresh_points_panel():  # Command to refresh points.
    points_pane.set_texts(global_variables.get_value('points'))


def refresh_lines_panel():  # Command to refresh lines.
    lines_pane.set_texts(global_variables.get_value('lines'))


def refresh_angles_panel():
    shapes.refresh_angles()
    angle_pane.set_texts(global_variables.get_value('angles'))


def refresh_collinear_points_panel():
    shapes.refresh_collinear_points()
    append_list = []
    for points in global_variables.get_value('collinear_points_list'):
        append_value = ''
        for point in points:
            append_value += point.name
            append_value += ' '
        append_list.append(append_value)
    collinear_points_pane.set_texts(append_list)


def refresh_parallel_lines_panel():
    shapes.refresh_parallel_lines()
    append_list = []
    for lines in global_variables.get_value('parallel_lines_list'):
        append_value = ''
        for line in lines:
            append_value += line.name
            append_value += ' '
        if len(lines) > 1:
            append_list.append(append_value)
    parallel_lines_pane.set_texts(append_list)


previous_point_property = None
previous_line_property = None


def on_point_pane_element_switch(string: str):
    global previous_point_property
    unhighlight_all_points()
    if previous_point_property:  # If previous point property is not None.
        previous_point_property.delete()  # Delete it.
    point = shapes.get_point_by_name(string)  # Get point object from it's name.
    if point:
        point.highlight()  # Highlight the point.
    previous_point_property = gui.PointPropertyPane(point, _refresh_all,
                                                    point_modify_command=current_mode.set_point_modify_mode)
    # When called next time, this is previous.


def on_collinear_points_pane_element_switch(string: str):
    unhighlight_all_points()
    points = []
    for point_name in string.split():
        points.append(shapes.get_point_by_name(point_name))
    for point in points:
        point.highlight()


def on_line_pane_element_switch(string: str):
    global previous_line_property
    unhighlight_all_lines()
    if previous_line_property:  # If previous line property is not None.
        previous_line_property.delete()  # Delete it.
    line = shapes.get_line_by_name(string)  # Get line object from it's name.
    if line:
        line.highlight()  # highlight the line.
    previous_line_property = gui.LinePropertyPane(line, _refresh_all)


def on_parallel_line_pane_element_switch(string: str):
    unhighlight_all_lines()
    lines = []
    for line_name in string.split():
        lines.append(shapes.get_line_by_name(line_name))
    for line in lines:
        line.highlight(unhighlighted_others=True)


def on_angle_pane_element_switch(string: str):
    unhighlight_all_lines()
    angle = shapes.get_angle_by_name(string)
    if angle:
        angle.highlight()


points_pane.on_listbox_element_switch(current_mode.get_current_shape, on_point_pane_element_switch)
lines_pane.on_listbox_element_switch(current_mode.get_current_shape, on_line_pane_element_switch)
angle_pane.on_listbox_element_switch(current_mode.get_current_shape, on_angle_pane_element_switch)
collinear_points_pane.on_listbox_element_switch(current_mode.get_current_shape,
                                                on_collinear_points_pane_element_switch)
parallel_lines_pane.on_listbox_element_switch(current_mode.get_current_shape, on_parallel_line_pane_element_switch)


def refresh_all():
    refresh_points_panel()
    refresh_lines_panel()
    refresh_angles_panel()
    refresh_collinear_points_panel()
    refresh_parallel_lines_panel()


global_variables.set_value('refresh_all_panels', 'refresh_all')
