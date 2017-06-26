#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
from ctypes.wintypes import CHAR

"""
This module provides functionality for writing characters on a grid.
The module provides functions for adding horizontal and vertical lines,
and for (optionally filled) rectangles, and for (optionally boxed) text.
All char arguments must be strings of length 1; these are guarded by
assertions. If out of range row or column values are given, the
appropriate exception, RowRangeError or ColumnRangeError will
be raised---use the RangeError exception if you want to catch either.

>>> resize(14, 50)
>>> add_rectangle(0, 0, *get_size())
>>> add_vertical_line(5, 10, 13)
>>> add_vertical_line(2, 9, 12, "!")
>>> add_horizontal_line(3, 10, 20, "+")
>>> add_rectangle(0, 0, 5, 5, "%")
>>> add_rectangle(5, 7, 12, 40, "#", True)
>>> add_rectangle(7, 9, 10, 38, " ")
>>> add_text(8, 10, "This is the CharGrid module")
>>> add_text(1, 32, "Pleasantville", "@")
>>> add_rectangle(6, 42, 11, 46, fill=True)
>>> render(False)
%%%%%*********************************************
%   %                           @@@@@@@@@@@@@@@  *
%   %                           @Pleasantville@  *
%   %     ++++++++++            @@@@@@@@@@@@@@@  *
%%%%%                                            *
*      #################################         *
*      #################################  ****   *
*      ##                             ##  ****   *
*      ## This is the CharGrid module ##  ****   *
* !    ##                             ##  ****   *
* !  | #################################  ****   *
* !  | #################################         *
*    |                                           *
**************************************************
"""


import subprocess
import sys


class RangeError(Exception):
    pass


class RowRangeError(RangeError):
    pass


class ColumnRangeError(RangeError):
    pass


_CHAR_ASSERT_TEMPLATE = ("char must be a single character: '{0}' "
                         "is too long")
_max_rows = 25
_max_columns = 80
_grid = []
_background_char = " "

if sys.platform.startswith("win"):
    def clear_screen():
        subprocess.call(["cmd.exe", "/C", "cls"])
else:
    def clear_screen():
        subprocess.call(["clear"])
clear_screen.__doc__ = """Clears the screen using the underlying \
window system's clear screen command"""


def resize(max_rows, max_columns, char=None):
    """Изменяет размер сетки, очищает содержимое и изменяет символ фона,
    если аргумент char не равен None
    """
    assert max_rows > 0 and max_columns > 0, "too small"
    global _grid, _max_rows, _max_columns, _background_char
    if char is not None:
        assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
        _background_char = char
    _max_rows = max_rows
    _max_columns = max_columns
    _grid = [[_background_char for column in range(_max_columns)]for row in range(_max_rows)]
    
    
def add_horizontal_line(row, column0, column1, char="-"):
    """ Добавляет в сетку горизонтальную линию, используя указанный символ
    
    >>> add_horizontal_line(8, 20, 25, "=")
    >>> char_at(8, 20) == char_at(8, 24) == "="
    True
    >>> add_horizontal_line(31, 11, 12)
    Trackback (most recent call last):
    ...
    RowRangeError
    """
    assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
    try:
        for column in range(column0, column1):
            _grid[row][column] = char
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()

resize(_max_rows, _max_columns)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

