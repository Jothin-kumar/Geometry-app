import sys

from ._angles import Angle, angle, get_angle_by_name, refresh_angles
from ._line import (Line, delete_line, get_line_by_name, line,
                    refresh_intersecting_lines, refresh_line,
                    refresh_parallel_lines)
from ._point import (Point, delete_point, get_point_by_coordinates,
                     get_point_by_name, point, refresh_collinear_points)

# Import global_variables module
sys.path.append('../')
import global_variables


def refresh_all():
    for line_ in global_variables.lines:
        line_.refresh()
    for point_ in global_variables.points:
        point_.refresh()
    refresh_collinear_points()
    refresh_parallel_lines()
    refresh_intersecting_lines(create_text_command=global_variables.create_text_command,
                               delete_line=global_variables.delete_line)
    refresh_angles()


global_variables.Point = Point
global_variables.point = point
global_variables.delete_point = delete_point
global_variables.Line = Line
global_variables.line = line
global_variables.delete_line = delete_line
global_variables.refresh_line = refresh_line
global_variables.Angle = Angle
global_variables.angle = angle
global_variables.refresh_angles = refresh_angles
