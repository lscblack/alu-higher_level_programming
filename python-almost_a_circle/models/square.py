#!/usr/bin/python3
"""Class Square that inherit from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """"
            Class Square inheriting Rectangle
            Attr :
                    id: number
                    size: number
                    x: number
                    y: number
        """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.size = kwargs["size"] if "size" in kwargs \
                else self.size
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
