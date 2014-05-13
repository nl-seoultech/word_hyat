# -*- coding: utf-8 -*-
from word_hyat import read


def test_read():
    assert ['1', '2', '3', '4', '5'] == list(read('./assets/abc.txt'))
