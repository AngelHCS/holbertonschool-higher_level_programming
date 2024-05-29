#!/usr/bin/python3
# 9-student.py
"""Define the Student class."""


class Student:
    """class student, self explanatory."""

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a Student."""

        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
