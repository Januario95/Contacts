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

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance



acc = BankAcc('Olga Matias', 706714264, 0)
acc.name = 'Reinata Mauricio'
acc.acc_nr = 706714523
print(acc.balance)
acc.deposit(1200)
print(acc.balance)
acc.deposit(300)
print(acc.balance)