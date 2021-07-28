#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created at Thur Jul 29 2021 05:07:23

@author: Januario Cipriano
"""

import time

print(time.ctime())


class Person(object):
    def __init__(self, name, age, social_sec_nr):
        self.__name = name
        self.__age = age
        self.__social_sec_nr = social_sec_nr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


person = Person('Olga Matias', 24, 235234)
print(person.name)
