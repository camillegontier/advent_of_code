# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np

##############################################################################

file_name = "2_input.txt"

values = []
with open(file_name, 'r') as f:
    for line in f:
        currentline = line.split(",")
        for i in currentline:
            values.append(i)
values[-1] = values[-1][:-1]
           
##############################################################################

def is_invalid(string):
    l_values = []
    for l in range(1,int(len(string)/2)+1):
        if int(len(string)) % l == 0:
               l_values.append(l)
    res = False
    for l in l_values:
        res_ = True
        for i in range(0,int(len(string)),l):
            # if i*l < len(string)/2:
                # print(i)
                if string[(i+l):(i+2*l)] != '':
                    res_ = (res_ and (string[i:(i+l)] == string[(i+l):(i+2*l)]))
        if res_:
            res = True

        
    return res

count = 0
for i in values:
    low = int(i.split("-")[0])
    high = int(i.split("-")[1])
    for j in range(low, high+1):
        if is_invalid(str(j)):
            count += j
            
print(count)

