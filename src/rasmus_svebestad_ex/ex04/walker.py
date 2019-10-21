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
        while a = False:
            self.move()
            self.is_at_home()
        
        return
