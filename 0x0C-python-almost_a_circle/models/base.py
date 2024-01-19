#!/usr/bin/python3
"""Module for Base class"""
import json
import csv


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set by dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                list_dicts = cls.from_json_string(content)
                return [cls.create(**obj) for obj in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for rect in list_objs:
                    writer.writerow([rect.id, rect.width, rect.height, rect.x, rect.y])
            elif cls.__name__ == "Square":
                for square in list_objs:
                    writer.writerow([square.id, square.size, square.x, square.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module"""
        import turtle

        turtle.bgcolor("white")
        turtle.title("Draw Shapes")

        def draw_shape(shape, color):
            """Draw a shape using turtle"""
            turtle.pendown()
            turtle.fillcolor(color)
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(shape.size)
                turtle.left(90)

            turtle.end_fill()
            turtle.penup()

        for rect in list_rectangles:
            turtle.goto(rect.x, rect.y)
            draw_shape(rect, "blue")

        for square in list_squares:
            turtle.goto(square.x, square.y)
            draw_shape(square, "red")

        turtle.hideturtle()
        turtle.done()

    def __str__(self):
        """Override the __str__ method"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.to_dictionary))
