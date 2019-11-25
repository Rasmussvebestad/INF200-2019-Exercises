# -*- coding: utf-8 -*-

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


from random import randint
import random


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


class Simulation(Walker):
    def __init__(self, start, home, seed):
        self.position = start
        self.home = home
        self.seed = seed
        self.steps = 0

    def single_walk(self):
        random.seed(self.seed)
        while not Simulation.is_at_home(self):
            Simulation.move(self)
        return Simulation.get_steps(self)

    def run_simulation(self, num_walks):
        list1 = []
        for j in range(num_walks):
            list1.append(self.single_walk())
        return list1


if __name__ == "__main__":

    run = [Simulation(10, 0, 12345),
           Simulation(10, 0, 12345),
           Simulation(10, 0, 54321),
           Simulation(0, 10, 12345),
           Simulation(0, 10, 12345),
           Simulation(0, 10, 54321)]

    for i in run:
        print(i.run_simulation(20))
