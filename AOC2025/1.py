# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np

##############################################################################

file_name = "1_input.txt"

with open(file_name, 'r') as f:
    lines = f.readlines()
    inputs = [entry.strip() for entry in lines]
    
##############################################################################

init = 50
count = 0
count2 = 0

for entry in inputs:
    
    init_prev = init
    
    if entry[0] == "L":
        init = init - int(entry[1:])% 100
    elif entry[0] == "R":
        init = init + int(entry[1:])% 100
        
    count2 += int(entry[1:]) // 100
    
    if init < 0:
        if init_prev != 0:
            count2 += 1
        init = init % 100
        
    elif init >= 100:
        if init > 100:
            count2 += 1
        init = init % 100
        
    if init == 0:
        count += 1
        count2 += 1
    
###############################################################################

print(count)
print(count2)