# -*- coding: utf-8 -*-

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1
        self.r = [seed]

    def rand(self):
        self.r.append(self.a * self.r[-1] % self.m)
        return self.r[-1]

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            random_number = self.rand()
            yield random_number


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        if self.num_generated_numbers is None:
            raise RuntimeError()

        next_number_generated = self.generator.rand()
        self.num_generated_numbers += 1

        if self.length == self.num_generated_numbers:
            raise StopIteration

        return next_number_generated

    def infinite_random_sequence(self):
        pass


if __name__ == "__main__":

    generator = LCGRand(1)
    for rand in generator.random_sequence(10):
        print(rand)

    i = 0
    for rand in generator.infinite_random_sequence():
        print('The {}-th random number is {}'.format(i, rand))
        if i > 100:
            break
        i += 1
