# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

from collections import Counter
import numpy as np

##############################################################################

file_name = "5_input.txt"
ranges = []
items = []

is_item = False
with open(file_name, 'r') as f:
    for line in f:
        if line[:-1] == '':
           is_item = True
        else:
            if is_item:
                items.append(line[:-1])
            else:
                ranges.append(line[:-1])
            
##############################################################################

def is_fresh(items,ranges,idx):
    
    item = items[idx]
    fresh = False
    for i in ranges:
        low = int(i.split("-")[0])
        high = int(i.split("-")[1])
        if low <= int(item) <= high:
            fresh = True
    return fresh

##############################################################################

count = 0
for idx in range(len(items)):
    if is_fresh(items,ranges,idx):
        count += 1
        
print(count)

##############################################################################

starts = []
ends = []

for i in ranges:
    starts.append(int(i.split("-")[0]))
    ends.append(int(i.split("-")[1]))
    
starts = np.array(starts)
ends = np.array(ends)
idx = np.argsort(starts)
starts = starts[idx]
ends = ends[idx]

    
starts_uniq = []
ends_uniq = []

for idx_i, i in enumerate(starts):
    if idx_i == 0:
        starts_uniq.append(i)
        ends_uniq.append(ends[idx_i])
    else:
        
        if i > ends_uniq[-1]:
            starts_uniq.append(i)
            ends_uniq.append(ends[idx_i])
        else:
            ends_uniq[-1] = max(ends_uniq[-1],ends[idx_i])
            
count = 0
for i in range(len(starts_uniq)):
    count = count + (ends_uniq[i] - starts_uniq[i] + 1)
    
print(count)
       