# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np

##############################################################################

file_name = "4_input.txt"

values = []
with open(file_name, 'r') as f:
    for line in f:
        values.append(line[:-1])
        
n_row = len(values)
n_col = len(values[0])
input_ = np.zeros((n_row+2,n_col+2),int)
for idx_i,i in enumerate(values):
    for idx_j, j in enumerate(i):
        # print(j)
        if j == '.':
            input_[idx_i+1,idx_j+1] = 0
        elif j == '@':
            input_[idx_i+1,idx_j+1] = 1
        
        
           
##############################################################################

def number_neighbors(input_,i,j):
    s = input_[i-1,j-1] + \
    input_[i-1,j] + \
    input_[i-1,j+1] + \
    input_[i,j-1] + \
    input_[i,j+1] + \
    input_[i+1,j-1] + \
    input_[i+1,j] + \
    input_[i+1,j+1]
    return s

##############################################################################
# input__ = np.zeros((n_row,n_col))
count = 0
count_temp =1 
while count_temp > 0:
    # print(input_)
    count_temp = 0
    i_to_remove = []
    j_to_remove = []
    for i in range(1,n_row+1):
        for j in range(1,n_col+1):
            s = number_neighbors(input_,i,j)
            if s < 4 and input_[i,j] ==1:
                count_temp += 1 
                i_to_remove.append(i)
                j_to_remove.append(j)
    count = count + count_temp
    for k in range(len(i_to_remove)):
            input_[i_to_remove[k],j_to_remove[k]] = 0
    
    if count_temp == 0:
        break
            # input__[i-1,j-1] = 1
        # else:
        #     input__[i-1,j-1] = input_[i,j]
            
# print(input__)
print(count)
     

    