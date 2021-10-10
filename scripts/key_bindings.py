import gui
from current_mode import switch_to_point_edit, switch_to_line_edit, switch_to_angle_mode, switch_to_collinear_points_mode, switch_to_parallel_lines_mode


def trigger():
    gui.bind_key('p', switch_to_point_edit)
    gui.bind_key('l', switch_to_line_edit)
    gui.bind_key('a', switch_to_angle_mode)
    gui.bind_key('c', switch_to_collinear_points_mode)
    gui.bind_key('r', switch_to_parallel_lines_mode)
