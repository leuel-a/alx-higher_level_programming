#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """This is MyInt class"""

    def __ne__(self, obj):
        """Override the != to make it =="""
        return self.real == obj

    def __eq__(self, obj):
        """Override the == to make it !="""
        return self.real != obj
