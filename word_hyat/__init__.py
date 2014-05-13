# -*- coding: utf-8 -*-


def get_freq(l):
    r = {}
    for x in l:
        if x in r:
            r[x] += 1
        else:
            r[x] = 1
    return r


def read(p):
    with open(p, 'r') as f:
        x = f.readline()
        while x:
            yield x.strip()
            x = f.readline()
