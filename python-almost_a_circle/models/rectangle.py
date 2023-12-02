#!/usr/bin/python3
"""Script with implementation of rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Represent rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle"""
        super().__init__(id)
        self.validate_value("width", width)
        self.validate_value("height", height)
        self.validate_value("x", x)
        self.validate_value("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            Returning private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set private attribute width
        """
        self.validate_value("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            Returning private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.validate_value("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute
        '''
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            Returning private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting private attribute
        '''
        self.validate_value("y", value)
        self.__y = value

    @staticmethod
    def validate_value(attribute, value):
        '''
        method to validate values for setter methods
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        '''
            Returns the area of the rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

    def __str__(self):
        '''
            Overwritting the str method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
