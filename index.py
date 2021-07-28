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

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def social_sec_nr(self):
        return self.__social_sec_nr

    @social_sec_nr.setter
    def social_sec_nr(self, new_nr):
        self.__social_sec_nr = new_nr

    def __str__(self):
        return f'{self.name} - {self.age} - {self.social_sec_nr}'


person = Person('Olga Matias', 24, 235234)
print(person)
