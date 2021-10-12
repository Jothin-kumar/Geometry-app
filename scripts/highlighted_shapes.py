import global_variables


def unhighlight_all_points():
    for point in global_variables.get_value('points'):
        point.unhighlight()


def unhighlight_all_lines():
    for line in global_variables.get_value('lines'):
        line.unhighlight()


def unhighlight_all():
    unhighlight_all_points()
    unhighlight_all_lines()
