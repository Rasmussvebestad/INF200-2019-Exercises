# -*- coding: utf-8 -*-

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


from random import randint


class Walker:
    def __init__(self, x0, home):
        self.position = x0
        self.home = home
        self.steps = 0

    def move(self):
        self.position = self.position + randint(0, 1) * 2 - 1
        self.steps = self.steps + 1

    def is_at_home(self):
        if self.position == self.home:
            return True
        return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps

    def walk_home(self):
        a = False
        while not a:
            self.move()
            a = self.is_at_home()
        return self.get_steps()


if __name__ == "__main__":

    for i in ((0, 1),
              (0, 2),
              (0, 5),
              (0, 10),
              (0, 20),
              (0, 50),
              (0, 100)):
        list1 = []
        for j in range(5):
            walking_home = Walker(i[0], i[1])
            list1.append(walking_home.walk_home())
        print('Distance : ' + str(i[1]) + ' -> Path lengths:' + str(list1))
