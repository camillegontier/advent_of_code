# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np

##############################################################################

file_name = "3_input.txt"

values = []
with open(file_name, 'r') as f:
    for line in f:
        values.append(line[:-1])
           
##############################################################################
string = '818181911112111'
def find_max(string):
    idx_values = np.zeros(12,int)
    idx1 = -1
    while idx1 == -1:
        for i in range(9,0,-1):
            # print(i)
            # print(idx1)
            if (string.find(str(i)) < (len(string)-11)) and string.find(str(i)) >= 0:
                idx1 = string.find(str(i))
                break
    idx_values[0] = idx1
    
    for k in range(1,12):
        
        idxk = idx_values[k-1] + 1
        # while idx2 == idx1 + 1:
        for i in range(9,0,-1):
                # print(i)
                if (string[(idx_values[k-1] + 1):].find(str(i)) > -1) and (idx_values[k-1] + string[(idx_values[k-1] + 1):].find(str(i)) + 1)< (len(string)-(11-k)):
                    idxk = idx_values[k-1] + string[(idx_values[k-1] + 1):].find(str(i)) + 1
                    break
        idx_values[k] = idxk
            
            
        # idx2 = idx1 + 1
        # # while idx2 == idx1 + 1:
        # for i in range(9,0,-1):
        #         # print(i)
        #         if (string[(idx1 + 1):].find(str(i)) > -1) and (idx1 + string[(idx1 + 1):].find(str(i)) + 1)< (len(string)-10):
        #             idx2 = idx1 + string[(idx1 + 1):].find(str(i)) + 1
        #             break
             
    return sum(int(string[k])*10**(11-idx_k) for idx_k,k in enumerate(idx_values))
 # [string[k] for k in idx_values]      
    # return string[idx1],string[idx2]

count = 0
for idx_i,i in enumerate(values):
    # print(count)
    # print(idx_i)
    count = count + find_max(i)

print(count)

    