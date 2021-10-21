"""
View this repository on github: https://github.com/Jothin-kumar/Geometry-app

MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys

# Import global_variables module
sys.path.append('../../')
import global_variables


class Angle:
    def __init__(self, line1: global_variables.get_value('Line'), line2: global_variables.get_value('Line')):
        for angle_ in global_variables.get_value('angles'):
            if angle_.lines in ([line1, line2], [line2, line1]):
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
        for angle_ in global_variables.get_value('angles'):
            angle_.unhighlight()
        for line_ in global_variables.get_value('lines'):
            line_.unhighlight()
        for line in self.lines:
            line.highlight(unhighlighted_others=True)

    def unhighlight(self):
        for line in global_variables.get_value('lines'):
            line.unhighlight()


def angle(line1: global_variables.get_value('Line'), line2: global_variables.get_value('Line')):
    angle_ = Angle(line1, line2)
    global_variables.get_value('angles').append(angle_)
    return angle_


def refresh_angles():
    global_variables.set_value('angles', [])
    for line1 in global_variables.get_value('lines'):
        for line2 in global_variables.get_value('lines'):
            if not line1 == line2:
                if line1.point1 == line2.point1 or line1.point1 == line2.point2 or line1.point2 == line2.point1 or line1.point2 == line2.point2:
                    try:
                        angle(line1, line2)
                    except ValueError:
                        pass


def get_angle_by_name(name: str):
    for angle_ in global_variables.get_value('angles'):
        if angle_.name == name:
            return angle_
