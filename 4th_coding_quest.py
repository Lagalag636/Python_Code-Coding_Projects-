class Table:
    """A class representing a table with various attributes."""

    def __init__(self, name, surface_type, shape, width, length, height, diameter, legs):
        """Initialize table attributes."""
        self.name = name
        self.surface_type = surface_type
        self.shape = shape
        self.surface_dimensions = [width, length, height, diameter]
        self.legs = legs

    def dimensions_for_shape(self):
        """
        Return relevant dimensions based on the shape of the table.
        """
        if self.shape == "rectangle":
            return self.surface_dimensions[0:2]  # width, length
        elif self.shape == "circle":
            return self.surface_dimensions[0:4]  # diameter
        elif self.shape == "oval":
            return self.surface_dimensions[0:2]  # width, length
        elif self.shape == "square":
            return self.surface_dimensions[0:2]  # width
        else:
            raise ValueError("Invalid shape")
        
    def surface_area_of_table(self):
        """
        Return the area of the table surface based on its shape.
        """
        if self.shape == "rectangle":
            return self.surface_dimensions[0] * self.surface_dimensions[1]
        elif self.shape == "circle":
            user_table_diameter = self.surface_dimensions[0]
            user_table_diameter = user_table_diameter / 2
            user_table_diameter = user_table_diameter ** 2
            3.14 * user_table_diameter
            self.surface_dimensions[0] = user_table_diameter
            return self.surface_dimensions[0]
        elif self.shape == "oval":
            return 3.14 * (self.surface_dimensions[0] / 2) * (self.surface_dimensions[1] / 2)
        elif self.shape == "square":
            return self.surface_dimensions[0] ** 2
        else:
            raise ValueError("Invalid shape")


if __name__ == "__main__":
    try:
        name = input("Table name: ")
        surface_type = input("What is the surface made out of?\n")
        shape = input("What is the shape of the table?\n")

        width = float(input("Width of table: "))
        length = float(input("Length of table: "))
        height = float(input("Height of table: "))
        diameter = float(input("Diameter of table (if applicable, else enter 0): "))
        legs = int(input("Number of legs: "))

        user_table = Table(name, surface_type, shape, width, length, height, diameter, legs)

        if user_table.legs < 0:
            raise ValueError("Number of legs must be greater than 0.")
        elif user_table.legs == 1:
            raise ValueError("That makes a podium, not a table.")
        elif user_table.legs == 2:
            raise ValueError("That makes a bench, not a table.")
        elif user_table.legs == 3:
            raise ValueError("That makes a stool, not a table.")
        elif user_table.legs >= 10:
            raise ValueError("...Why?")
        else:
            user_table.surface_dimensions = user_table.dimensions_for_shape()

        print("Table name:", user_table.name)
        print("Surface area of table:", user_table.surface_area_of_table())

    except ValueError as e:
        print("ValueError:", e)
