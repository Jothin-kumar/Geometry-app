from shapes import points, lines, Line
collinear_points_list = []
parallel_lines_list = []


def refresh_collinear_points():
    global collinear_points_list
    collinear_points_list = []
    collinear_points_list_temp = []
    for point in points:
        collinear_points_list_temp.append({'points': [point], 'collinear by': 'x', 'x': point.x})
        collinear_points_list_temp.append({'points': [point], 'collinear by': 'y', 'y': point.y})
        for collinear_points in collinear_points_list_temp:
            if collinear_points['collinear by'] == 'x':
                if collinear_points['x'] == point.x:
                    if not point in collinear_points['points']:
                        collinear_points['points'].append(point)
            elif collinear_points['collinear by'] == 'y':
                if collinear_points['y'] == point.y:
                    if not point in collinear_points['points']:
                        collinear_points['points'].append(point)
    for collinear_points in collinear_points_list_temp:
        if len(collinear_points['points']) > 2:
            collinear_points_list.append(collinear_points['points'])
    collinear_points_list_temp = []
    for point in points:
        point_exists_in_a_collinear_point_group = False
        for collinear_points in collinear_points_list_temp:
            for collinear_point in collinear_points:
                if collinear_point == point:
                    point_exists_in_a_collinear_point_group = True
        if not point_exists_in_a_collinear_point_group:
            for collinear_points_ in collinear_points_list_temp:
                if any([
                    (collinear_points_[0].x - collinear_points_[0].y) == (point.x - point.y),
                    (collinear_points_[0].x + collinear_points_[0].y) == (point.x + point.y)
                    ]):
                    collinear_points_.append(point)
                    point_exists_in_a_collinear_point_group = True
                    break
        if not point_exists_in_a_collinear_point_group:
            collinear_points_list_temp.append([point])
    for collinear_points in collinear_points_list_temp:
        if len(collinear_points) > 2:
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
            line1.point2 != line2.point2
        ])
    for line in lines:
        line_exists_in_a_parallel_line_group = False
        for parallel_lines in parallel_lines_list_temp:
            for parallel_line in parallel_lines:
                if parallel_line == line:
                    line_exists_in_a_parallel_line_group = True
        if not line_exists_in_a_parallel_line_group:
            for parallel_lines in parallel_lines_list_temp:
                if parallel(line, parallel_lines[0]):
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