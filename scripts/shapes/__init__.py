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
    for line_ in global_variables.get_value('lines'):
        line_.refresh()
    for point_ in global_variables.get_value('points'):
        point_.refresh()
    refresh_collinear_points()
    refresh_parallel_lines()
    refresh_intersecting_lines(create_text_command=global_variables.get_value('create_text_command'),
                               delete_line=global_variables.get_value('delete_line'))
    refresh_angles()


global_variables.set_value('Point', Point)
global_variables.set_value('point', point)
global_variables.set_value('delete_point', delete_point)
global_variables.set_value('Line', Line)
global_variables.set_value('line', line)
global_variables.set_value('delete_line', delete_line)
global_variables.set_value('refresh_line', refresh_line)
global_variables.set_value('Angle', Angle)
global_variables.set_value('angle', angle)
global_variables.set_value('refresh_angles', refresh_angles)
global_variables.set_value('points', [])
global_variables.set_value('lines', [])
global_variables.set_value('angles', [])
