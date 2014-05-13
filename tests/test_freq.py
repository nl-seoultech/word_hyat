# -*- coding: utf-8 -*-
from word_hyat import get_freq


def test_get_freq():
    a = ['a', 'b', 'c', 'b', 'a']
    assert {'a': 2, 'b': 2, 'c': 1} == get_freq(a)
