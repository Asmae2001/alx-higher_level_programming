#!/usr/bin/python3
"""Module for Base class"""
class Base:
    """Base class with private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    # Example usage
    b1 = Base()
    print(b1.id)  # Output: 1

    b2 = Base(5)
    print(b2.id)  # Output: 5

