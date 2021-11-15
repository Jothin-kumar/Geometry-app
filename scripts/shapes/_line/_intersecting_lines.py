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

Author: Jothin kumar (https://jothin-kumar.github.io/)
Github repository of this project: https://github.com/Jothin-kumar/Geometry-app
"""
import sys

# Import global_variables module
sys.path.append('../../')
import global_variables


def refresh_intersecting_lines(create_text_command, delete_line):
    global_variables.set_value('intersecting_lines_and_intersection_point', {})
    horizontal_lines = []
    vertical_lines = []
    for line in global_variables.get_value('lines'):
        if line.point1.y == line.point2.y:
            horizontal_lines.append(line)
        elif line.point1.x == line.point2.x:
            vertical_lines.append(line)
    for horizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
            global_variables.get_value('intersecting_lines_and_intersection_point')[(vertical_line.point1.x,
                                                                                     horizontal_line.point1.y)] = {
                'horizontal line': horizontal_line, 'vertical line': vertical_line
            }
            try:
                global_variables.get_value('point')(vertical_line.point1.x, horizontal_line.point1.y,
                                                    create_text_command, delete_line)
            except ValueError:
                pass
