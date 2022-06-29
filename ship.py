class Ship:
    START_SPEED_X = 0
    START_SPEED_Y = 0
    START_HEADING = 0

    def __init__(self, location_x, location_y, speed_x=START_SPEED_X,
                 speed_y=START_SPEED_Y, heading=START_HEADING):
        self.__location_x = location_x
        self.__speed_x = speed_x
        self.__location_y = location_y
        self.__speed_y = speed_y
        self.__heading = heading

    def get_location_x(self):
        """This function returns the location x of the ship"""
        return self.__location_x

    def get_location_y(self):
        """This function returns the location y of the ship"""
        return self.__location_y

    def get_speed_x(self):
        """This function returns the speed x of the ship"""
        return self.__speed_x

    def get_speed_y(self):
        """This function returns the speed y of the ship"""
        return self.__speed_y

    def get_heading(self):
        """This function returns a float number of the direction of the ship"""
        return float(self.__heading)

    def get_radius(self):
        """This function returns the radius of the ship, which is 1"""
        return 1

    def set_location_x(self, new_location_x):
        """This function sets the location x of the ship"""
        self.__location_x = new_location_x

    def set_location_y(self, new_location_y):
        """This function sets the location y of the ship"""
        self.__location_y = new_location_y

    def set_speed_x(self, new_speed_x):
        """This function sets the speed x of the ship"""
        self.__speed_x = new_speed_x

    def set_speed_y(self, new_speed_y):
        """This function sets the speed y of the ship"""
        self.__speed_y = new_speed_y

    def set_heading(self, new_heading):
        """This function sets the direction of the ship"""
        self.__heading = new_heading
