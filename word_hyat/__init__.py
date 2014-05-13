# -*- coding: utf-8 -*-


def get_freq(l):
    """ 리스트로 들어온 단어들의 빈번도를 체크합니다.

    .. sourcecode::python

       >>> from word_hyat import get_freq
       >>> get_freq(['a', 'b', 'c', 'a'])
       {'a': 2, 'b': 1, 'c': 1}

    :param list l: 단어들이 나열되있는 리스트
    :return: 빈번도를 나타내는 dict
    :rtype: dict
    """
    r = {}
    for x in l:
        if x in r:
            r[x] += 1
        else:
            r[x] = 1
    return r


def read(p):
    """ 파일을 읽어들여서, 라인 별로 텍스트를 내보냅니다.

    :param str p: 읽을 파일의 경로
    :return: 공백을 제거한 텍스트를 한줄씩 반환
    :rtype: generator
    """
    with open(p, 'r') as f:
        x = f.readline()
        while x:
            yield x.strip()
            x = f.readline()
