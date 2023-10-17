#!/usr/bin/python3
"""
Module containe one class to print info about square
"""

import sys


class square():
    """
    class to print info about the square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ SQUARE INITALIZATION """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ PERMITER of the square """
        return (self.width * self.height * 2)

    def __str__(self):
        """ SQUARE STRING """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ MAIN FUNCTION CALL CHECK """

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
