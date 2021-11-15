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
