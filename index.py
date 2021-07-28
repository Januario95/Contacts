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