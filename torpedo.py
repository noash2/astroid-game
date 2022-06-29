class Torpedo:
    def __init__(self, location_x, location_y, speed_x, speed_y, direction):
        self.__location_x = location_x
        self.__speed_x = speed_x
        self.__location_y = location_y
        self.__speed_y = speed_y
        self.__direction = direction
        self.__life_cycle_torpedo = 200

    def get_location_x(self):
        """This function returns the location x of the torpedo."""
        return self.__location_x

    def get_location_y(self):
        """This function returns the location y of the torpedo."""
        return self.__location_y

    def get_speed_x(self):
        """This function returns the speed x of the torpedo."""
        return self.__speed_x

    def get_speed_y(self):
        """This function returns the speed y of the torpedo."""
        return self.__speed_y

    def get_direction(self):
        """This function returns the torpedo's direction."""
        return float(self.__direction)

    def get_radius(self):
        """This function returns the torpedo's radius."""
        return 4

    def get_life_cycle(self):
        """This function returns 200 (which is the torpedo's life cycle)."""
        return self.__life_cycle_torpedo

    def set_location_x(self, new_location_x):
        """This function sets the torpedo's location x."""
        self.__location_x = new_location_x

    def set_location_y(self, new_location_y):
        """This function sets the torpedo's location y."""
        self.__location_y = new_location_y

    def set_speed_x(self, new_speed_x):
        """This function sets the torpedo's speed x."""
        self.__speed_x = new_speed_x

    def set_speed_y(self, new_speed_y):
        """This function sets the torpedo's speed y."""
        self.__speed_y = new_speed_y

    def set_direction(self, new_direction):
        """This function sets new direction for the torpedo."""
        self.__direction = new_direction

    def update_life_cycle_torpedo(self):
        """This function updates the life cycle of the torpedo."""
        self.__life_cycle_torpedo -= 1
