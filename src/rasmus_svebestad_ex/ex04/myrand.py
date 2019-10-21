# -*- coding: utf-8 -*-

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1
        self.seed = seed

    def rand(self):
        r = [None]
        r[1] = self.seed
        r.append(self.a * r[-1] % self.m)
        return r[-1]


class ListRand:
    def __init__(self, a_list):
        self.a_list = a_list

    def rand(self):
        if len(self.a_list) <= 0:
            raise RuntimeError
        else:
            return self.a_list.pop(0)


for i in range(10):
    if i < 5:
        print(LCGRand.rand(3))
    else:
        print(ListRand.rand([1, 14, 33, 13, 222, 1033, 2]))
