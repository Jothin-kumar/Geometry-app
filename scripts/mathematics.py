from shapes import points
collinear_points_list = []


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
