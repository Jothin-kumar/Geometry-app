import sys

# Import global_variables module
sys.path.append('../../')
import global_variables


def refresh_intersecting_lines(create_text_command, delete_line):
    global_variables.intersecting_lines_and_intersection_point = {}
    horizontal_lines = []
    vertical_lines = []
    for line in global_variables.get_value('lines'):
        if line.point1.y == line.point2.y:
            horizontal_lines.append(line)
        elif line.point1.x == line.point2.x:
            vertical_lines.append(line)
    for horizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
            global_variables.get_value('intersecting_lines_and_intersection_point')[(vertical_line.point1.x,
                                                                                     horizontal_line.point1.y)] = {
                'horizontal line': horizontal_line, 'vertical line': vertical_line
            }
            try:
                global_variables.get_value('point')(vertical_line.point1.x, horizontal_line.point1.y,
                                                    create_text_command, delete_line)
            except ValueError:
                pass
