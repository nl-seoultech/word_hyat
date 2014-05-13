def get_freq(l):
    r = {}
    for x in l:
        if x in r:
            r[x] += 1
        else:
            r[x] = 1
    return r
