from global_variables import lines, points


def unhighlight_all_points():
    for point in points:
        point.unhighlight()


def unhighlight_all_lines():
    for line in lines:
        line.unhighlight()


def unhighlight_all():
    unhighlight_all_points()
    unhighlight_all_lines()
