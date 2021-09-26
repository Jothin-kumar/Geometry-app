import GUI
import shapes

current_shape = 'point'  # Current shape to edit. Ex: Point, Line
previous_click_point = None  # Previously clicked coordinates as shapes.Point object. Defined as None for now


def switch_to_point_edit():  # Switch to point edit.
    global current_shape
    current_shape = 'point'


def switch_to_line_edit():  # Switch to Line edit.
    global previous_click_point
    global current_shape
    current_shape = 'line'
    previous_click_point = None  # Empty previous click point to start a new shape.


def refresh_points_panel():  # Command to refresh points.
    points_pane.set_texts(shapes.points)


def refresh_lines_panel():  # Command to refresh lines.
    lines_pane.set_texts(shapes.lines)


def refresh_all():  # Command to refresh side panel.
    refresh_points_panel()
    refresh_lines_panel()


points_pane = GUI.ShapePane(shape_name='Points', switch_to_this_shape_command=switch_to_point_edit)  # The points panel.
lines_pane = GUI.ShapePane(shape_name='Lines', switch_to_this_shape_command=switch_to_line_edit)  # The lines panel.
previous_highlighted_point = None  # Variable to store previous highlighted point.
previous_highlighted_line = None  # Variable to store previous highlighted line.
previous_point_property = None  # Variable to store previous point shown in property panel.
previous_line_property = None  # Variable to store previous line shown in property panel.


def on_point_pane_element_switch(string: str):
    global previous_highlighted_point
    global previous_point_property
    if previous_highlighted_point:  # If previous highlighted point is not None.
        previous_highlighted_point.un_highlight()  # Un-Highlight.
    if previous_point_property:  # If previous point property is not None.
        previous_point_property.delete()  # Delete it.
    point = shapes.get_point_by_name(string)  # Get point object from it's name.
    if point:
        point.highlight()  # Highlight the point.
    previous_point_property = GUI.PointPropertyPane(point, refresh_all)  # When called next time, this is previous.
    previous_highlighted_point = point  # When called next time, this point is the previously highlighted one.


def on_line_pane_element_switch(string: str):
    global previous_highlighted_line
    global previous_line_property
    if previous_highlighted_line:  # If previous highlighted line is not None.
        previous_highlighted_line.un_highlight()  # Un-Highlight.
    if previous_line_property:  # If previous line property is not None.
        previous_line_property.delete()  # Delete it.
    line = shapes.get_line_by_name(string)  # Get line object from it's name.
    if line:
        line.highlight()  # highlight the line.
    previous_line_property = GUI.LinePropertyPane(line, refresh_all)
    previous_highlighted_line = line  # When called next time, this line is the previously highlighted one.


points_pane.on_listbox_element_switch(on_point_pane_element_switch)
lines_pane.on_listbox_element_switch(on_line_pane_element_switch)


def on_diagram_editor_click(event):  # When user clicks on the diagram editor.
    x = (int(event.x / 50) * 50) + 25
    y = (int(event.y / 50) * 50) + 25
    if current_shape == 'point':  # If current shape is Point, Just create a new point where clicked.
        global previous_point_property
        global previous_highlighted_point
        try:  # Try to create a Point.
            shapes.point(x, y, GUI.create_text, GUI.delete)  # Create a point.
            points_pane.set_texts(shapes.points)  # Refresh panel.
        except ValueError:  # In case it already exists, do nothing.
            pass
        if previous_highlighted_point:  # If previous highlighted point is not None.
            previous_highlighted_point.un_highlight()  # Un-Highlight.
        if previous_point_property:  # If previous point property is not None.
            previous_point_property.delete()  # Delete it.
        point = shapes.get_point_by_coordinates(x, y)  # Get point object from it's coordinates.
        if point:
            point.highlight()  # Highlight the point.
        previous_point_property = GUI.PointPropertyPane(point, refresh_all)  # When called next time, this is previous.
        previous_highlighted_point = point  # When called next time, this point is the previously highlighted one.
    elif current_shape == 'line':  # If current shape is line, Draw line from previous clicked coordinate to here.
        global previous_click_point
        current_click_point = shapes.get_point_by_coordinates(x, y)
        if previous_click_point and current_click_point:
            # If the Point 'previous_click_point' and 'current_click_point' exists.
            try:  # Try to create a line.
                shapes.line(previous_click_point, current_click_point, GUI.create_line, GUI.delete)  # Create a line.
                lines_pane.set_texts(shapes.lines)  # Refresh panel.
            except ValueError:  # In case it already exists, do nothing.
                pass
        previous_click_point = current_click_point


GUI.on_diagram_viewer_click(on_diagram_editor_click)
GUI.mainloop()
