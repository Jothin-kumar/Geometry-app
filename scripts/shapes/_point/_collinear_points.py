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

# Import global_variables module
sys.path.append('../../')
import global_variables


def refresh_collinear_points():
    global_variables.set_value('collinear_points_list', [])
    collinear_points_dict_x = {}
    collinear_points_dict_y = {}
    collinear_points_dict_slant_plus = {}
    collinear_points_dict_slant_minus = {}
    for point in global_variables.get_value('points'):
        try:
            collinear_points_dict_x[point.x].append(point)
        except KeyError:
            collinear_points_dict_x[point.x] = [point]
        try:
            collinear_points_dict_y[point.y].append(point)
        except KeyError:
            collinear_points_dict_y[point.y] = [point]
        try:
            collinear_points_dict_slant_plus[point.x + point.y].append(point)
        except KeyError:
            collinear_points_dict_slant_plus[point.x + point.y] = [point]
        try:
            collinear_points_dict_slant_minus[point.x - point.y].append(point)
        except KeyError:
            collinear_points_dict_slant_minus[point.x - point.y] = [point]
    for collinear_points in collinear_points_dict_x.values():
        if len(collinear_points) >= 3:
            global_variables.get_value('collinear_points_list').append(collinear_points)
    for collinear_points in collinear_points_dict_y.values():
        if len(collinear_points) >= 3:
            global_variables.get_value('collinear_points_list').append(collinear_points)
    for collinear_points in collinear_points_dict_slant_plus.values():
        if len(collinear_points) >= 3:
            global_variables.get_value('collinear_points_list').append(collinear_points)
    for collinear_points in collinear_points_dict_slant_minus.values():
        if len(collinear_points) >= 3:
            global_variables.get_value('collinear_points_list').append(collinear_points)
