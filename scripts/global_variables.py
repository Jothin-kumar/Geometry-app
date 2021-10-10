def blank_command(**kwargs):
    pass


class BlankClass:
    def __init__(self, **kwargs):
        pass


points = []
collinear_points_list = []
lines = []
parallel_lines_list = []
intersecting_lines_and_intersection_point = {}
angles = []
refresh_line = blank_command
refresh_angles = blank_command
create_text_command = blank_command
create_line_command = blank_command
delete_point = blank_command
delete_line = blank_command
refresh_all_panels = blank_command
Point = BlankClass
Line = BlankClass
Angle = BlankClass
previous_click_point = None
