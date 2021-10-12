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
