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
    global line_exists_in_a_parallel_line_group
    global parallel_lines_list
    parallel_lines_list = []
    parallel_lines_list_temp = []
    line_exists_in_a_parallel_line_group = []
    def parallel(line1: Line, line2: Line):
        return any([
            any([
                line1.point1.x - line1.point2.x == line2.point1.x - line2.point2.x,
                line1.point1.y - line1.point2.y == line2.point1.y - line2.point2.y,
                ]),
            all([
                line1.point1.x + line1.point2.x == line2.point1.x + line2.point2.x,
                line1.point1.y + line1.point2.y == line2.point1.y + line2.point2.y,
                ]),
            all([
                line1.point1.x - line1.point1.y == line1.point2.x - line1.point2.y,
                line2.point1.x - line2.point1.y == line2.point2.x - line2.point2.y,
            ]),
            all([
                line1.point1.x + line1.point1.y == line1.point2.x + line1.point2.y,
                line2.point1.x + line2.point1.y == line2.point2.x + line2.point2.y,
            ])
        ]) and all([
            line1.point1 != line2.point1,
            line1.point2 != line2.point2,
            line1.point1 != line2.point2,
            line1.point2 != line2.point1
        ])
    for line in lines:
        line_exists_in_a_parallel_line_group = False
        for parallel_lines in parallel_lines_list_temp:
            for parallel_line in parallel_lines:
                if parallel_line == line:
                    line_exists_in_a_parallel_line_group = True
        if not line_exists_in_a_parallel_line_group:
            for parallel_lines in parallel_lines_list_temp:
                is_parallel = True
                for parallel_line in parallel_lines:
                    if not parallel(line, parallel_line):
                        is_parallel = False
                if is_parallel:
                    parallel_lines.append(line)
                    line_exists_in_a_parallel_line_group = True
                    break
        if not line_exists_in_a_parallel_line_group:
            parallel_lines_list_temp.append([line])
    for parallel_lines in parallel_lines_list_temp:
        if not parallel_lines in parallel_lines_list:
            parallel_lines_list.append(parallel_lines)


def refresh_all():
    refresh_collinear_points()
    refresh_parallel_lines()