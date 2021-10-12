import sys

from ._intersecting_lines import refresh_intersecting_lines
from ._parallel_lines import refresh_parallel_lines

# Import global_variables module
sys.path.append('../../')
import global_variables


class Line:
    def __init__(self, point1: global_variables.get_value('Point'), point2: global_variables.get_value('Point'),
                 create_line_command, delete_command, show: bool = True):
        self.point1 = point1
        self.point2 = point2
        if self.point1 == self.point2:
            raise ValueError('A line must have two different points.')
        for line_ in global_variables.get_value('lines'):
            if (line_.point1 == point1 and line_.point2 == point2) or (
                    line_.point2 == point1 and line_.point1 == point2):
                raise ValueError('Line already exists.')
        self.points = [point1, point2]
        self.name = point1.name + point2.name
        self.create_line_command = create_line_command
        if show:
            self.line = create_line_command(point1.x, point1.y, point2.x, point2.y)
        self.displayed = show
        self.delete_command = delete_command

    def hide(self):
        self.delete_command(self.line)
        self.displayed = False

    def show(self):
        if not self.displayed:
            self.line = self.create_line_command(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
            self.displayed = False

    def refresh(self):
        self.hide()
        self.show()

    def highlight(self, unhighlighted_others=False):
        if not unhighlighted_others:
            for angle_ in global_variables.get_value('angles'):
                angle_.unhighlight()
            for line_ in global_variables.get_value('lines'):
                line_.unhighlight()
        self.hide()
        self.line = self.create_line_command(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill='red')
        self.displayed = True

    def unhighlight(self):
        self.hide()
        if self.point1 and self.point2:
            self.show()


def line(point1: global_variables.get_value('Point'), point2: global_variables.get_value('Point'), create_line_command,
         delete_command, show: bool = True):
    line_ = Line(point1, point2, create_line_command, delete_command, show)
    global_variables.get_value('lines').append(line_)
    global_variables.get_value('refresh_angles')()
    return line_


def delete_line(line_: Line):
    line_.point1 = None
    line_.point2 = None
    line_.hide()
    del global_variables.get_value('lines')[global_variables.get_value('lines').index(line_)]
    global_variables.refresh_angles()


def refresh_line(line_: Line):
    line_.refresh()


def get_line_by_name(name: str):
    for line_ in global_variables.get_value('lines'):
        if line_.name == name:
            return line_
