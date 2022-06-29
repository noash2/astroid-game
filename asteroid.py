import math


class Asteroid:
    START_SPEED_X = 0
    START_SPEED_Y = 0
    START_SIZE = 3

    def __init__(self, location_x, location_y, speed_x=START_SPEED_X,
                 speed_y=START_SPEED_Y, size=START_SIZE):
        self.__location_x = location_x
        self.__speed_x = speed_x
        self.__location_y = location_y
        self.__speed_y = speed_y
        self.__size = size

    def get_location_x(self):
        """This function returns the location x of the asteroid."""
        return self.__location_x

    def get_location_y(self):
        """This function returns the location y of the asteroid."""
        return self.__location_y

    def get_speed_x(self):
        """This function returns the speed of the asteroid on x."""
        return self.__speed_x

    def get_speed_y(self):
        """This function returns the speed of the asteroid on y  ."""
        return self.__speed_y

    def get_size(self):
        """This function returns the size of the asteroid"""
        return self.__size

    def get_radius(self):
        """This function returns the asteroid's radius."""
        radius = (self.__size * 10) - 5
        return radius

    def set_location_x(self, new_location_x):
        """This function sets the location x of the asteroid."""
        self.__location_x = new_location_x

    def set_location_y(self, new_location_y):
        """This function sets the location y of the asteroid."""
        self.__location_y = new_location_y

    def set_speed_x(self, new_speed_x):
        """This function sets the speeds on x of the asteroid."""
        self.__speed_x = new_speed_x

    def set_speed_y(self, new_speed_y):
        """This function sets the speeds on y of the asteroid."""
        self.__speed_y = new_speed_y

    def set_size(self, new_size):
        """This function sets new asteroid's size."""
        self.__size = new_size

    def has_intersection(self, obj):
        """
        This function checks if an intersection happened.
        :param obj: Class object: ship or torpedo.
        :return:  True - if an intersection happened
                False - if not."""
        distance = math.sqrt((int(obj.get_location_x()) - int(
            self.get_location_x())) ** 2 + int((obj.get_location_y()) - int(
                self.get_location_y())) ** 2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False
