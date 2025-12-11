# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import functools
import time

file_name = "11_input.txt"
        
childs = {}
        
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        temp = []
        for i in line[:-1].split(":")[-1][1:].split(' '):
            temp.append(i)
        childs[line[:-1].split(":")[0]] = temp
childs["out"] = []
        
@functools.cache
def recurs(n):
    if n == "out":
        return 1
    else:
        return sum(map(recurs,childs[n]))
    
def recurs2(n):
    if n == "out":
        return 1
    else:
        return sum(map(recurs,childs[n]))
    
print(recurs("you"))
print(recurs("svr"))

start = time.time()
recurs("you")    
end = time.time()
print(end - start)

start = time.time()
recurs2("you")    
end = time.time()
print(end - start)

###############################################################################

file_name = "11_input.txt"
        
childs = {}
        
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        temp = []
        for i in line[:-1].split(":")[-1][1:].split(' '):
            temp.append(i)
        childs[line[:-1].split(":")[0]] = temp
childs["out"] = []

@functools.cache
def recurs(in_,out):
    if in_ == out:
        return 1
    else:
        # return sum(map(recurs,[childs[in_],out]))
        return sum(map(lambda p: recurs(p, out), childs[in_]))
    
print(recurs("svr","fft")*recurs("fft","dac")*recurs("dac","out") + recurs("svr","dac")*recurs("dac","fft")*recurs("fft","out"))

