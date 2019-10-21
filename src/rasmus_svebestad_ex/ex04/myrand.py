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

    def rand(self):
        if len(self.a_list) <= 0:
            raise RuntimeError
        else:
            return self.a_list.pop(0)


if __name__ == "__main__":

    lcgrand = LCGRand(1)
    listrand = ListRand([1, 14, 33, 13, 222, 1033, 2])
    for i in range(10):
        if i < 5:
            print(lcgrand.rand())
        else:
            print(listrand.rand())
