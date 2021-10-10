import sys

# Import global_variables module
sys.path.append('../../')
import global_variables


def refresh_collinear_points():
    global_variables.collinear_points_list = []
    collinear_points_dict_x = {}
    collinear_points_dict_y = {}
    collinear_points_dict_slant_plus = {}
    collinear_points_dict_slant_minus = {}
    for point in global_variables.points:
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
            global_variables.collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_y.values():
        if len(collinear_points) >= 3:
            global_variables.collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_slant_plus.values():
        if len(collinear_points) >= 3:
            global_variables.collinear_points_list.append(collinear_points)
    for collinear_points in collinear_points_dict_slant_minus.values():
        if len(collinear_points) >= 3:
            global_variables.collinear_points_list.append(collinear_points)
