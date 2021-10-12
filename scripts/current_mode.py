import global_variables
import gui
import highlighted_shapes

current_shape = 'point'  # point is the default shape
point_modify_mode = False


def set_point_modify_mode():
    global point_modify_mode
    point_modify_mode = True


def get_current_shape():
    return current_shape


def on_mode_switch():
    global_variables.set_value('previous_click_point', None)
    highlighted_shapes.unhighlight_all()


def switch_to_point_edit():  # Switch to point edit.
    global current_shape
    current_shape = 'point'
    gui.set_current_mode('Point')
    on_mode_switch()


def switch_to_line_edit():  # Switch to Line edit.
    global current_shape
    current_shape = 'line'
    gui.set_current_mode('Line')
    on_mode_switch()


def switch_to_angle_mode():
    global current_shape
    current_shape = 'angle'
    gui.set_current_mode('Angle')
    on_mode_switch()


def switch_to_collinear_points_mode():
    global current_shape
    current_shape = 'collinear point'
    gui.set_current_mode('Collinear points')
    on_mode_switch()


def switch_to_parallel_lines_mode():
    global current_shape
    current_shape = 'parallel line'
    gui.set_current_mode('Parallel lines')
    on_mode_switch()
