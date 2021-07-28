#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created at Thur Jul 29 2021 05:20:35

@author: Januario Cipriano
"""

class BankAcc:
    def __init__(self, name, acc_nr, balance=None):
        self.__name = name
        self.__acc_nr = acc_nr
        self.__balance = balance

    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, new_name):
        self.__name = new_name 

    @property
    def acc_nr(self):
        return self.__acc_nr

    @acc_nr.setter
    def acc_nr(self, new_nr):
        self.__acc_nr = new_nr

acc = BankAcc('Olga Matias', 706714264, 0)
print(acc.name)
print(acc.acc_nr)

acc.name = 'Reinata Mauricio'
acc.acc_nr = 706714523
print(acc.name)
print(acc.acc_nr)