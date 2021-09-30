from types import prepare_class
from typing import List
from shapes import points, lines, Line
collinear_points_list = []
parallel_lines_list = []


def refresh_collinear_points():
    global collinear_points_list
    collinear_points_list = []
    collinear_points_dict_x = {}
    collinear_points_dict_y = {}
    collinear_points_dict_slant_plus = {}
    collinear_points_dict_slant_minus = {}
    for point in points:
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
            collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_y.values():
        if len(collinear_points) >= 3:
            collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_slant_plus.values():
        if len(collinear_points) >= 3:
            collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_slant_minus.values():
        if len(collinear_points) >= 3:
            collinear_points_list.append(collinear_points)


def refresh_parallel_lines():
    global parallel_lines_list
    parallel_lines_list = []
    parallel_lines_dicts_x = []
    parallel_lines_dicts_y = []
    for line in lines:
        if line.point1.x == line.point2.x:
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_x:
                if not line.point1.x in parallel_line_dict['reserved x']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved x'].append(line.point1.x)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_x.append({'lines': [line], 'reserved x': [line.point1.x]})
        if line.point1.y == line.point2.y:
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_y:
                if not line.point1.y in parallel_line_dict['reserved y']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved y'].append(line.point1.y)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_y.append({'lines': [line], 'reserved y': [line.point1.y]})
    for parallel_line_dict in parallel_lines_dicts_x:
        parallel_lines_list.append(parallel_line_dict['lines'])
    for parallel_line_dict in parallel_lines_dicts_y:
        parallel_lines_list.append(parallel_line_dict['lines'])


def refresh_all():
    refresh_collinear_points()
    refresh_parallel_lines()