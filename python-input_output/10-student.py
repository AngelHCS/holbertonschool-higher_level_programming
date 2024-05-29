#!/usr/bin/python3
# 10-student.pyi
"""Define the student class"""


class Student:
    """Class student, self explanatory."""

    def __init__(self, first_name, last_name, age):
        """Defines
        has arg of self,firstname,lastname,age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """def has self,attrs"""

            if attrs is not None and isinstance(attrs, list):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
                return self.__dict__
