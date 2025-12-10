# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np
from collections import Counter

file_name = "7_input.txt"
n_line = 0
n_col = 0
with open(file_name, 'r') as f:
    for line in f:
        if n_line == 0:
            aa = line
            n_col = len(line)
        n_line += 1
        
current_state = np.zeros(n_col)
total_state =  np.zeros(n_col)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

counter = 0
counter2 = 1

with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        next_state = np.copy(current_state)
        if line_idx == 0:
            idx = find(line, 'S')
            next_state[idx] = 1
        else:
            idx = find(line, '^')
            idx2 = np.where(current_state == 1)[0]
            idx_ = list(set(idx) & set(list(idx2)))
            
            for i in idx_:
               next_state[i-1] = 1 
               next_state[i+1] = 1 
               next_state[i] = 0
               counter2 = counter2 + 1
            counter += len(idx_)
        current_state = next_state
        if '^' not in line:
            total_state = np.vstack((total_state,current_state))
 



def number_ancestor(total_state,i,j):
    cnt = 0
    js = []
    if total_state[i+1,j]==1:
        cnt += 1
        js.append(j)
    if j == 0:
        if total_state[i,j+1]==0 and total_state[i+1,j+1]==1:
            cnt += 1
            js.append(j+1)
    else:
        
        if total_state[i,j-1]==0 and total_state[i+1,j-1]==1:
            cnt += 1
            js.append(j-1)
        if total_state[i,j+1]==0 and total_state[i+1,j+1]==1:
            cnt += 1
            js.append(j+1)
    return cnt,js
    

total_state = total_state[::-1]

counter = 0
line = total_state[0,:]
idx =  np.where(line == 1)[0]
js_ = []

for k in idx:
    js_.append([k])
    unique_data = [list(x) for x in set(tuple(x) for x in js_)]
    n =  [js_.count(x) for x in unique_data]
for i in range(total_state.shape[0]-1):
    print(i)
    # lookuptable = {}
    # for j in range(n_col-1):
    #     lookuptable[j] = number_ancestor(total_state,i,j)
    
    # print(unique_data)
    js__ = []
    n_ = []
    
    for idx_j,j in enumerate(unique_data):
    # for idx_j,j in enumerate(js_):
        number = n[idx_j]
        for jj in j:
            cnt,js = number_ancestor(total_state,i,jj)
            # cnt,js = lookuptable[jj]

            # for l in range(number):
            js__.append(js)
            n_.append(number)
            # n_.append(js_.count(j)*n[idx_j])
    
    # n__ = []
    # for kk_idx,kk in enumerate(js__):
    #     n__.append(js__.count(kk)*n_[kk_idx])
        
    
    unique_data = [list(x) for x in set(tuple(x) for x in js__)]
    n = []
    for idx_x,x in enumerate(unique_data):
        idxs=[i for i, j in enumerate(js__) if j == x]
        n.append(sum(n_[p] for p in idxs))
    # n =  [js__.count(x) for x in unique_data]
    print(n)
    # n = n_
    
    
    # n = n_
    # print(js__)
    # js_ = list(set(js__))
    

# print(len(js_))