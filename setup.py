# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


install_requires = [
]

test_requires = [
    'pytest >= 2.3.5'
]


setup(name='word_hyat',
      description=u'단어의 빈도를 분석해주는 분석기',
      author='Hyojun Kang',
      author_email='hyojun@admire.kr',
      packages=find_packages(),
      install_requires=install_requires,
      test_require=test_requires)
