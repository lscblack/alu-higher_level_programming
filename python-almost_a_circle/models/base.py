#!/usr/bin/python3
"""base class."""
import json


class Base:
    """The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json to string."""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """List of objects"""
        file_name = cls.__name__ + ".json"
        yy = []
        if list_objs:
            for i in list_objs:
                yy.append(cls.to_dictionary(i))

        with open(file_name, mode="w") as saveme:
            saveme.write(cls.to_json_string(yy))

    @staticmethod
    def from_json_string(json_string):
        """Json conversion."""
        if json_string is None:
            return []

        if len(json_string) == 0:
            return []

        json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """CReatiNG oBJectS."""
        if cls.__name__ == "Rectangle":
            yves = cls(3, 2)
        if cls.__name__ == "Square":
            yves = cls(3)
        yves.update(**dictionary)
        return yves

    @classmethod
    def load_from_file(cls):
        """list of objects"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                content = file.read()
        except FileNotFoundError:
            return []

        hi = cls.from_json_string(content)
        fine = []
        for hello in hi:
            fine.append(cls.create(**hello))
        return fine
