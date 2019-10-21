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
    def __init__(self, alist):
        self.alist = alist

    def rand(self):
        if len(self.alist) <= 0:
            raise RuntimeError
        else:
            

