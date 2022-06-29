from screen import Screen
import sys
from ship import Ship
import random
import math
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5

TITLE_CRASHED_SHIP = "OOPS!"
TITLE_EXIT_GAME = "The end of the world!"

MESSAGE_CRASHED_SHIP = "You crashed with the ship"
MESSAGE_NO_MORE_ASTEROIDS = "You won!"
MESSAGE_NO_MORE_LIVES = "You are a LOOSER!! try again :)"
MESSAGE_ASKED_EXIT = "You entered the exit key, and the game is over."


class GameRunner:

    def __init__(self, asteroids_amount):
        # Screen object:
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        # Ship object:
        ship_location_x, ship_location_y = self.choosing_random_location()
        self.__ship = Ship(ship_location_x, ship_location_y)
        # Asteroid objects:
        self.__asteroids_amount = asteroids_amount
        self.__lst_torpedoes = []
        self.__lives = 3
        self.__points = 0
        self.__game_loop_counter = 0
        self.__lst_asteroids = self.set_lst_asteroids()

    def set_lst_asteroids(self):
        """
        This function creates the asteroids according to the asteroid's
        amount, and puts them all in a list
        """
        asteroids = []
        for i in range(self.__asteroids_amount):
            location_x, location_y = self.choosing_random_location()
            if location_x == self.__ship.get_location_x() and \
                    location_y == self.__ship.get_location_y():
                location_x, location_y = self.choosing_random_location()
            speed_x = random.randint(1, 4) * random.choice([-1, 1])
            speed_y = random.randint(1, 4) * random.choice([-1, 1])
            asteroid = Asteroid(location_x, location_y, speed_x, speed_y, 3)
            asteroids.append(asteroid)
            self.__screen.register_asteroid(asteroid, 3)
        return asteroids

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def choosing_random_location(self):
        location_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        location_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return location_x, location_y

    def move_object(self, obj):
        """
        This function moves the current object.
        :param obj: Class. The current object we want to move.
        """
        new_x = self.__screen_min_x + (obj.get_location_x() + obj.get_speed_x()
           - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x)
        new_y = self.__screen_min_y + (obj.get_location_y() + obj.get_speed_y()
           - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y)
        obj.set_location_x(new_x)
        obj.set_location_y(new_y)

    def change_ship_direction(self):
        """
        This function changes the ship's direction.
        """
        if self.__screen.is_left_pressed() is True:
            self.__ship.set_heading(self.__ship.get_heading() + 7)
        if self.__screen.is_right_pressed() is True:
            self.__ship.set_heading(self.__ship.get_heading() - 7)

    def accelerate_ship_speed(self):
        """This function accelerates the ship's speed."""
        if self.__screen.is_up_pressed() is True:
            self.__ship.set_speed_x(self.__ship.get_speed_x() + \
                          math.cos(math.radians(self.__ship.get_heading())))
            self.__ship.set_speed_y(self.__ship.get_speed_y() + \
                          math.sin(math.radians(self.__ship.get_heading())))

    def draw_and_move_asteroids(self):
        """This function draws all the current asteroids to the screen first,\
                 than moves them on the screen."""
        for asteroid in self.__lst_asteroids:
            self.__screen.draw_asteroid(asteroid, asteroid.get_location_x(),
            asteroid.get_location_y())
            self.move_object(asteroid)

    def check_if_asteroid_crashed_with_ship(self):
        """This function reduces lives when an intersection happens between
        the ship and asteroid."""
        for asteroid in self.__lst_asteroids:
            if asteroid not in self.__lst_asteroids:
                return
            if asteroid.has_intersection(self.__ship):
                self.__screen.show_message(TITLE_CRASHED_SHIP,
                                           MESSAGE_CRASHED_SHIP)
                self.__lives -= 1
                self.__screen.remove_life()
                self.remove_asteroid(asteroid)
                break

    def check_if_asteroid_crashed_with_torpedo(self):
        """This function calls the 'split function' if there is an
        intersection and updates the points of the game according to the
        asteroid's size."""
        for torpedo in self.__lst_torpedoes:
            for asteroid in self.__lst_asteroids:
                if asteroid.has_intersection(torpedo):
                    self.split_asteroid(asteroid, torpedo)
                    if asteroid.get_size() == 3:
                        self.__points += 20
                    elif asteroid.get_size() == 2:
                        self.__points += 50
                    elif asteroid.get_size() == 1:
                        self.__points += 100
                    break
                self.__screen.set_score(self.__points)

    def split_asteroid(self, asteroid, torpedo):
        """This function splits the asteroid ,that crashed with torpedo, \
        in two small asteroids."""
        new_speed_x = (torpedo.get_speed_x() + asteroid.get_speed_x()) / (
            math.sqrt((asteroid.get_speed_x()) ** 2 + (asteroid.get_speed_y() ** 2)))
        new_speed_y = (torpedo.get_speed_y() + asteroid.get_speed_y()) / (
            math.sqrt((asteroid.get_speed_x()) ** 2 + (asteroid.get_speed_y() ** 2)))
        if asteroid not in self.__lst_asteroids:
            return
        if asteroid.get_size() > 1:
            new_asteroid_1 = Asteroid(asteroid.get_location_x(),
                             asteroid.get_location_y(), new_speed_x,
                                      new_speed_y, asteroid.get_size() - 1)
            new_asteroid_2 = Asteroid(asteroid.get_location_x(),
                             asteroid.get_location_y(), - (new_speed_x),
                                      - (new_speed_y), asteroid.get_size() - 1)

            self.__lst_asteroids += [new_asteroid_1, new_asteroid_2]
            self.__screen.register_asteroid(new_asteroid_1,
                                            new_asteroid_1.get_size())
            self.__screen.register_asteroid(new_asteroid_2, new_asteroid_2.get_size())
            self.__screen.draw_asteroid(new_asteroid_1,
                                        new_asteroid_1.get_location_x(),
                                        new_asteroid_1.get_location_y())
            self.__screen.draw_asteroid(new_asteroid_2,
                                        new_asteroid_2.get_location_x(),
                                        new_asteroid_2.get_location_y())
        self.remove_asteroid(asteroid)
        self.remove_torpedo(torpedo)

    def remove_asteroid(self, asteroid):
        """
        This function takes off the current asteroid from the screen,\
        and from the game at all.
        :param asteroid: The current asteroid which will be deleted.
        """
        self.__screen.unregister_asteroid(asteroid)
        self.__lst_asteroids.remove(asteroid)

    def remove_torpedo(self, torpedo):
        """
        This function removes the current torpedo from the screen,\
         and from the game at all.
        :param torpedo: The current torpedo which
        """
        self.__screen.unregister_torpedo(torpedo)
        self.__lst_torpedoes.remove(torpedo)
        pass

    def create_and_draw_torpedo(self):
        """
        This function creates torpedoes and draws them on the screen.
        """
        if len(self.__lst_torpedoes) < 10:
            torpedo_speed_x = self.__ship.get_speed_x() + 2 * math.cos(
                math.radians(self.__ship.get_heading()))
            torpedo_speed_y = self.__ship.get_speed_y() + 2 * math.sin(
            math.radians(self.__ship.get_heading()))
            torpedo = Torpedo(self.__ship.get_location_x(),
                       self.__ship.get_location_y(), torpedo_speed_x,
                              torpedo_speed_y, self.__ship.get_heading())
            self.__screen.register_torpedo(torpedo)
            self.__lst_torpedoes.append(torpedo)
        else:
            return

    def move_torpedo(self):
        """This function moves all the torpedoed on the screen."""
        for torpedo in self.__lst_torpedoes:
            self.move_object(torpedo)
            self.__screen.draw_torpedo(torpedo, torpedo.get_location_x(),
                           torpedo.get_location_y(), torpedo.get_direction())

    def end_life_torpedo(self):
        """This function updates the torpedo's lives \
         and if the torpedo has not have more lives, it will be removed."""
        for torpedo in self.__lst_torpedoes:
            torpedo.update_life_cycle_torpedo()
            if torpedo.get_life_cycle() == 0:
                self.remove_torpedo(torpedo)

    def exit_game(self):
        """This function checks if the game is over, according to the 3 options-
        1 - if there's no more asteroids
        2- the user lost all the lives.
        3 - if the user pressed the exit key - q."""
        if len(self.__lst_asteroids) == 0: # 1
            self.__screen.show_message(TITLE_EXIT_GAME, MESSAGE_NO_MORE_ASTEROIDS)
            self.__screen.end_game()
            sys.exit()
        elif self.__lives == 0: # 2
            self.__screen.show_message(TITLE_EXIT_GAME, MESSAGE_NO_MORE_LIVES)
            self.__screen.end_game()
            sys.exit()
        elif self.__screen.should_end(): # 3
            self.__screen.show_message(TITLE_EXIT_GAME, MESSAGE_ASKED_EXIT)
            self.__screen.end_game()
            sys.exit()

    def _game_loop(self):
        """"This is the main function that manages the game"""
        # Creates and moves the ship
        self.__screen.draw_ship(self.__ship.get_location_x(),
                                self.__ship.get_location_y(),
                                self.__ship.get_heading())
        self.move_object(self.__ship)
        self.change_ship_direction()
        self.accelerate_ship_speed()

        # Creates and moves the asteroids and the torpedoes
        self.draw_and_move_asteroids()
        if self.__screen.is_space_pressed():
            self.create_and_draw_torpedo()
        self.move_torpedo()
        self.check_if_asteroid_crashed_with_ship()
        self.check_if_asteroid_crashed_with_torpedo()
        # self.clean- torpedo & asteroids.
        self.end_life_torpedo()
        self.exit_game()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
