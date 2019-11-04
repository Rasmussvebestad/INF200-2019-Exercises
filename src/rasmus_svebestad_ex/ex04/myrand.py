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


class ListRand:
    def __init__(self, a_list):
        self.a_list = a_list
        self.index = 0

    def rand(self):
        if self.index == len(self.a_list):
            raise RuntimeError
        else:
            self.index += 1
            return self.a_list[self.index - 1]


if __name__ == "__main__":

    lcgrand = LCGRand(1)
    listrand = ListRand([1, 14, 33, 13, 222, 1033, 2])
    for i in range(10):
        if i < 5:
            print(lcgrand.rand())
        else:
            print(listrand.rand())
