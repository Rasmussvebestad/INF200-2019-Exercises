# -*- coding: utf-8 -*-

__author__ = 'rasmus svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'

# Task B


# Importing pytest for the test_empty_list function
import pytest


def median(data):
    """"
    The function is fetched from the INF200 exercise repository on GitHub
    """

    sdata = sorted(data)
    n = len(sdata)
    if n % 2 == 1:
        return sdata[n//2]
    elif n == 0:
        raise ValueError
    else:
        return 0.5 * (sdata[n//2 - 1] + sdata[n//2])


def test_one_element():
    assert median([2]) == 2


def test_odd():
    data = [1, 3, 5, 7]
    assert median(data) == 4


def test_even():
    data = [2, 4, 6, 8]
    assert median(data) == 5


def test_ordered():
    data = [1, 2, 3]
    assert median(data) == 2


def test_reversed():
    data = [3, 2, 1]
    assert median(data) == 2


def test_unordered():
    data = [2, 1, 3]
    assert median(data) == 2


def test_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    data = [1, 2, 3]
    median(data)
    assert data == [1, 2, 3]


def test_tuples():
    data = (1, 2, 3, 4, 5)
    assert median(data) == 3
