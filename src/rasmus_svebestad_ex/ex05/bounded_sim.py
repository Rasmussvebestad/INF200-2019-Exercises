# -*- coding: utf-8 -*-

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


from walker_sim import Simulation
import random


class BoundedWalker(Simulation):
    def __init__(self, start, home, left_limit, right_limit):
        self.position = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.steps = 0

    def bounded_move(self):
        a = random.randint(0, 1)
        if self.position != self.left_limit and self.position != self.right_limit:
            self.position += a * 2 - 1
            self.steps += 1
        elif self.position == self.right_limit and a == 0:
            self.position += a * 2 - 1
            self.steps += 1
        elif self.position == self.left_limit and a == 1:
            self.position += a * 2 - 1
            self.steps += 1

    def bounded_walk(self):
        while not BoundedWalker.is_at_home(self):
            self.bounded_move(self)
        return BoundedWalker.get_steps(self)


class BoundedSimulation(BoundedWalker):
    def __init__(self, start, home, seed, left_limit, right_limit):
        self.position = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.seed = seed
        self.steps = 0

    def bounded_single_walk(self):
        random.seed(self.seed)
        while not BoundedSimulation.is_at_home(self):
            BoundedSimulation.bounded_move(self)
        return BoundedSimulation.get_steps(self)

    def bounded_simulation(self, num_walks):
        list1 = []
        for j in range(num_walks):
            list1.append(self.bounded_single_walk())
        return list1


if __name__ == "__main__":

    run = [0, -10, -100, -1000, -10000]

    for i in run:
        print(BoundedSimulation(0, 20, 1, i, 20).bounded_simulation(20))
