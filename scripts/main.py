from tkinter.constants import NO
import GUI
import shapes
import mathematics

current_shape = 'point'  # Current shape to edit. Ex: Point, Line
point_modify_mode = False
previous_click_point = None  # Previously clicked coordinates as shapes.Point object. Defined as None for now


def switch_to_point_edit():  # Switch to point edit.
    global current_shape
    current_shape = 'point'
    GUI.set_current_mode('Point')


def set_point_modify_mode():
    global point_modify_mode
    point_modify_mode = True


def switch_to_line_edit():  # Switch to Line edit.
    global previous_click_point
    global current_shape
    current_shape = 'line'
    previous_click_point = None  # Empty previous click point to start a new shape.
    GUI.set_current_mode('Line')
    for angle in shapes.angles:
        angle.unhighlight()


def switch_to_angle_mode():
    global current_shape
    current_shape = 'angle'
    GUI.set_current_mode('Angle')
    for line in shapes.lines:
        line.un_highlight()


def switch_to_collinear_points_mode():
    global current_shape
    current_shape = 'collinear point'
    GUI.set_current_mode('Collinear points')


def refresh_points_panel():  # Command to refresh points.
    points_pane.set_texts(shapes.points)


def refresh_lines_panel():  # Command to refresh lines.
    lines_pane.set_texts(shapes.lines)


def refresh_angles_panel():
    angle_pane.set_texts(shapes.angles)


def refresh_collinear_points_panel():
    append_list = []
    for points in mathematics.collinear_points_list:
        append_value = ''
        for point in points:
            append_value += point.name
            append_value += ' '
        append_list.append(append_value)
    colliner_points_pane.set_texts(append_list)


def refresh_parallel_lines_panel():
    append_list = []
    for lines in mathematics.parallel_lines_list:
        append_value = ''
        for line in lines:
            append_value += line.name
            append_value += ' '
        if len(lines) > 1:
            append_list.append(append_value)
    parallel_lines_pane.set_texts(append_list)


def refresh_all():  # Command to refresh side panel.
    refresh_points_panel()
    refresh_lines_panel()
    refresh_angles_panel()
    mathematics.refresh_all()
    refresh_collinear_points_panel()
    refresh_parallel_lines_panel()
    GUI.refresh_diagram_editor()


points_pane = GUI.ShapePane(shape_name='Points', switch_to_this_shape_command=switch_to_point_edit)  # The points panel.
lines_pane = GUI.ShapePane(shape_name='Lines', switch_to_this_shape_command=switch_to_line_edit)  # The lines panel.
angle_pane = GUI.ShapePane(shape_name='Angles', switch_to_this_shape_command=switch_to_angle_mode)
colliner_points_pane = GUI.ShapePane('Collinear points', switch_to_this_shape_command=switch_to_collinear_points_mode)
parallel_lines_pane = GUI.ShapePane('Parallel lines', switch_to_this_shape_command=lambda: None)
previous_highlighted_point = None  # Variable to store previous highlighted point.
previous_highlighted_line = None  # Variable to store previous highlighted line.
previous_point_property = None  # Variable to store previous point shown in property panel.
previous_line_property = None  # Variable to store previous line shown in property panel.
previous_highlighted_angle = None
previous_highlighted_collinear_points = []
previous_highlighted_parallel_lines = []


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
    previous_point_property = GUI.PointPropertyPane(point, refresh_all, point_modify_command=set_point_modify_mode)
    # When called next time, this is previous.
    previous_highlighted_point = point  # When called next time, this point is the previously highlighted one.


def on_collinear_points_pane_element_switch(string: str):
    global previous_highlighted_collinear_points
    if previous_highlighted_collinear_points:
        for previous_highlighted_point in previous_highlighted_collinear_points:
            previous_highlighted_point.un_highlight()
    points = []
    for point_name in string.split():
        points.append(shapes.get_point_by_name(point_name))
    for point in points:
        point.highlight()
    previous_highlighted_collinear_points = points


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


def on_angle_pane_element_switch(string: str):
    global previous_highlighted_angle
    if previous_highlighted_angle:
        previous_highlighted_angle.unhighlight()
    angle = shapes.get_angle_by_name(string)
    if angle:
        angle.highlight()
    previous_highlighted_angle = angle


def get_current_shape():
    return current_shape


points_pane.on_listbox_element_switch(get_current_shape, on_point_pane_element_switch)
lines_pane.on_listbox_element_switch(get_current_shape, on_line_pane_element_switch)
angle_pane.on_listbox_element_switch(get_current_shape, on_angle_pane_element_switch)
colliner_points_pane.on_listbox_element_switch(get_current_shape, on_collinear_points_pane_element_switch)


def on_diagram_editor_click(event):  # When user clicks on the diagram editor.
    x = (int(event.x / 50) * 50) + 25
    y = (int(event.y / 50) * 50) + 25
    if current_shape == 'point':  # If current shape is Point, Just create a new point where clicked.
        global previous_point_property
        global previous_highlighted_point
        global point_modify_mode
        if point_modify_mode:
            previous_highlighted_point.set_coordinates(x, y)
            point_modify_mode = False
            for line in shapes.lines:
                if line.point1.x == previous_highlighted_point.x and line.point1.y == previous_highlighted_point.y:
                    line.point1 = shapes.get_point_by_coordinates(x, y)
                elif line.point2.x == previous_highlighted_point.x and line.point2.y == previous_highlighted_point.y:
                    line.point2 = shapes.get_point_by_coordinates(x, y)
                shapes.refresh_line(line)
        else:
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
        previous_point_property = GUI.PointPropertyPane(point, refresh_all, point_modify_command=set_point_modify_mode)
        # When called next time, this is previous.
        previous_highlighted_point = point  # When called next time, this point is the previously highlighted one.
    elif current_shape == 'line':  # If current shape is line, Draw line from previous clicked coordinate to here.
        global previous_click_point
        current_click_point = shapes.get_point_by_coordinates(x, y)
        if previous_click_point and current_click_point:
            # If the Point 'previous_click_point' and 'current_click_point' exists.
            try:  # Try to create a line.
                shapes.line(previous_click_point, current_click_point, GUI.create_line, GUI.delete)  # Create a line.
            except ValueError:  # In case it already exists, do nothing.
                pass
        previous_click_point = current_click_point
    refresh_all()


GUI.on_diagram_viewer_click(on_diagram_editor_click)
GUI.mainloop()
