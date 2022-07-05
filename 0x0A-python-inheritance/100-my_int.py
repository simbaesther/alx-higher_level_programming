#!/usr/bin/python3
"""
Module containing class MyInt that inherits from int
"""


class MyInt(int):
    """ Class that inherits from int """

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
