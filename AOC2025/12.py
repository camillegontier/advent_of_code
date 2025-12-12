#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 10:32:54 2025

@author: camille
"""

from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

file_name = "12_input.txt"

n = 0
with open(file_name, 'r') as f:
    for line in f:
        maxm = reduce(operator.mul, (int(line[:-1].split(":")[0].split("x")[0]),
                                     int(line[:-1].split(":")[0].split("x")[1])), 1)
        minm = (5*int(line[:-1].split(":")[1][1:].split(" ")[0])+
        6*int(line[:-1].split(":")[1][1:].split(" ")[1])+
        7*int(line[:-1].split(":")[1][1:].split(" ")[2])+
        7*int(line[:-1].split(":")[1][1:].split(" ")[3])+
        7*int(line[:-1].split(":")[1][1:].split(" ")[4])+
        7*int(line[:-1].split(":")[1][1:].split(" ")[5]))
        
        if maxm >= minm:
            n += 1
        
        