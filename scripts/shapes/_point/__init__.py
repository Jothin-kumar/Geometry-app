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

Author: Jothin kumar (https://jothin.tech)
Github repository of this project: https://github.com/Jothin-kumar/Geometry-app
"""
import sys
from itertools import cycle

from ._collinear_points import refresh_collinear_points

# Import global_variables module
sys.path.append('../../')
import global_variables

variable_letters = iter(cycle(['A', 'B', 'C', 'X', 'Y', 'Z']))

variable_num = 1


def get_variable_letter():
    global variable_num
    current_variable_letter = next(variable_letters)
    if current_variable_letter == 'Z':
        variable_num += 1
    return current_variable_letter + str(variable_num)


class Point:
    def __init__(self, x: int, y: int, create_text_command, delete_command, show: bool = True):
        self.x = x
        self.y = y
        for point_ in global_variables.get_value('points'):
            if point_.x == self.x and point_.y == self.y:
                raise ValueError('Point already exists.')
        self.name = get_variable_letter()
        self.coordinates = (self.x, self.y)
        self.create_text_command = create_text_command
        if show:
            self.text = self.create_text_command(self.x, self.y, text=self.name)
        self.displayed = show
        self.delete_command = delete_command
        self.blink = False

    def hide(self):
        if self.displayed:
            self.delete_command(self.text)
            self.displayed = False

    def show(self):
        if not self.displayed:
            self.text = self.create_text_command(self.x, self.y, text=self.name)
            self.displayed = True

    def set_coordinates(self, x: int, y: int):
        self.x = x
        self.y = y
        self.hide()
        self.show()

    def rename(self, new_name: str, refresh_command):
        if not new_name == self.name:
            for point_ in global_variables.get_value('points'):
                if point_.name == new_name:
                    raise ValueError(
                        f'A variable with the name {new_name} already exists. Please choose a different variable.'
                    )
            self.name = new_name
            self.hide()
            self.show()
            for line_ in global_variables.get_value('lines'):
                global_variables.get_value('refresh_line')(line_)
            refresh_command()

    def highlight(self):
        self.hide()
        self.text = self.create_text_command(self.x, self.y, text=self.name, fill='red')
        self.displayed = True

    def unhighlight(self):

        self.hide()
        if self.x and self.y:
            self.show()

    def refresh(self):
        self.hide()
        self.show()


def point(x: int, y: int, create_text_command, delete_command, show_point: bool = True):
    point_ = Point(x, y, create_text_command, delete_command, show_point)
    global_variables.get_value('points').append(point_)
    return point_


def delete_point(point_: Point):
    point_.x = None
    point_.y = None
    point_.hide()
    del global_variables.get_value('points')[global_variables.get_value('points').index(point_)]


def get_point_by_coordinates(x: int, y: int):
    for point_ in global_variables.get_value('points'):
        if point_.x == x and point_.y == y:
            return point_


def get_point_by_name(name: str):
    for point_ in global_variables.get_value('points'):
        if point_.name == name:
            return point_


global_variables.set_value('point', point)
global_variables.set_value('Point', Point)
global_variables.set_value('delete_point', delete_point)
