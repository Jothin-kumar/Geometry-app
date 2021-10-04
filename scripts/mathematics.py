from shapes import points, lines, point
collinear_points_list = []
parallel_lines_list = []
intersecting_lines_and_intersection_point = {}


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
    parallel_lines_dicts_plus = []
    parallel_lines_dicts_minus = []
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
        elif line.point1.y == line.point2.y:
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_y:
                if not line.point1.y in parallel_line_dict['reserved y']:
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
                parallel_lines_dicts_plus.append({'lines': [line], 'reserved x y sum': [line.point1.x + line.point1.y]})
        elif (line.point1.x - line.point1.y) == (line.point2.x - line.point2.y):
            line_grouped = False
            for parallel_line_dict in parallel_lines_dicts_minus:
                if not (line.point1.x - line.point1.y) in parallel_line_dict['reserved x y difference']:
                    parallel_line_dict['lines'].append(line)
                    parallel_line_dict['reserved x y difference'].append(line.point1.x - line.point1.y)
                    line_grouped = True
            if not line_grouped:
                parallel_lines_dicts_minus.append({'lines': [line], 'reserved x y difference': [line.point1.x - line.point1.y]})
    for parallel_line_dict in parallel_lines_dicts_x:
        parallel_lines_list.append(parallel_line_dict['lines'])
    for parallel_line_dict in parallel_lines_dicts_y:
        parallel_lines_list.append(parallel_line_dict['lines'])
    for parallel_lines_dict in parallel_lines_dicts_plus:
        parallel_lines_list.append(parallel_lines_dict['lines'])
    for parallel_lines_dict in parallel_lines_dicts_minus:
        parallel_lines_list.append(parallel_lines_dict['lines'])


def refresh_intersecting_lines(create_text_command, delete_line):
    global intersecting_lines_and_intersection_point
    intersecting_lines_and_intersection_point = {}
    horizontal_lines = []
    vertical_lines = []
    for line in lines:
        if line.point1.y == line.point2.y:
            horizontal_lines.append(line)
        elif line.point1.x == line.point2.x:
            vertical_lines.append(line)
    for horizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
            intersecting_lines_and_intersection_point[(vertical_line.point1.x, horizontal_line.point1.y)] = {'horizontal line': horizontal_line, 'vertical line': vertical_line}
            try:
                point(vertical_line.point1.x, horizontal_line.point1.y, create_text_command, delete_line)
            except ValueError:
                pass


def refresh_all(create_text_command, delete_line):
    refresh_collinear_points()
    refresh_parallel_lines()
    refresh_intersecting_lines(create_text_command, delete_line)
