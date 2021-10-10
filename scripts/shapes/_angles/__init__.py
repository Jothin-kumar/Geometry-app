import sys

# Import global_variables module
sys.path.append('../../')
import global_variables


class Angle:
    def __init__(self, line1: global_variables.Line, line2: global_variables.Line):
        for angle_ in global_variables.angles:
            if angle_.lines == [line1, line2] or angle_.lines == [line2, line1]:
                raise ValueError('Angle already exists')
        self.lines = [line1, line2]
        self.vertex = None
        for point1 in line1.points:
            for point2 in line2.points:
                if point1 == point2:
                    self.vertex = point1
        self.points = []
        for line in self.lines:
            for point in line.points:
                if point not in self.points and point != self.vertex:
                    self.points.append(point)
        self.name = f'{self.points[0].name}{self.vertex.name}{self.points[1].name}'

    def highlight(self):
        for angle_ in global_variables.angles:
            angle_.unhighlight()
        for line_ in global_variables.lines:
            line_.unhighlight()
        for line in self.lines:
            line.highlight(unhighlighted_others=True)

    def unhighlight(self):
        for line in global_variables.lines:
            line.unhighlight()


def angle(line1: global_variables.Line, line2: global_variables.Line):
    angle_ = Angle(line1, line2)
    global_variables.angles.append(angle_)
    return angle_


def refresh_angles():
    global_variables.angles = []
    for line1 in global_variables.lines:
        for line2 in global_variables.lines:
            if not line1 == line2:
                if line1.point1 == line2.point1 or line1.point1 == line2.point2 or line1.point2 == line2.point1 or line1.point2 == line2.point2:
                    try:
                        angle(line1, line2)
                    except ValueError:
                        pass


def get_angle_by_name(name: str):
    for angle_ in global_variables.angles:
        if angle_.name == name:
            return angle_
