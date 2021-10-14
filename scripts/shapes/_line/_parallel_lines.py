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


def refresh_parallel_lines():
    global_variables.set_value('parallel_lines_list', [])
    parallel_lines_dicts_x = []
    parallel_lines_dicts_y = []
    parallel_lines_dicts_plus = []
    parallel_lines_dicts_minus = []
    for line in global_variables.get_value('lines'):
        if line.point1.x == line.point2.x:
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_x:
                if line.point1.x not in parallel_line_dict['reserved x']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved x'].append(line.point1.x)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_x.append({'lines': [line], 'reserved x': [line.point1.x]})
        elif line.point1.y == line.point2.y:
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_y:
                if line.point1.y not in parallel_line_dict['reserved y']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved y'].append(line.point1.y)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_y.append({'lines': [line], 'reserved y': [line.point1.y]})
        elif (line.point1.x + line.point1.y) == (line.point2.x + line.point2.y):
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_plus:
                if not (line.point1.x + line.point1.y) in parallel_line_dict['reserved x y sum']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved x y sum'].append(line.point1.x + line.point1.y)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_plus.append(
                    {'lines': [line], 'reserved x y sum': [line.point1.x + line.point1.y]})
        elif (line.point1.x - line.point1.y) == (line.point2.x - line.point2.y):
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_minus:
                if not (line.point1.x - line.point1.y) in parallel_line_dict['reserved x y difference']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved x y difference'].append(line.point1.x - line.point1.y)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_minus.append(
                    {'lines': [line], 'reserved x y difference': [line.point1.x - line.point1.y]})
    for parallel_line_dict_x in parallel_lines_dicts_x:
        global_variables.get_value('parallel_lines_list').append(parallel_line_dict_x['lines'])
    for parallel_line_dict_y in parallel_lines_dicts_y:
        global_variables.get_value('parallel_lines_list').append(parallel_line_dict_y['lines'])
    for parallel_lines_dict_plus in parallel_lines_dicts_plus:
        global_variables.get_value('parallel_lines_list').append(parallel_lines_dict_plus['lines'])
    for parallel_lines_dict_minus in parallel_lines_dicts_minus:
        global_variables.get_value('parallel_lines_list').append(parallel_lines_dict_minus['lines'])
