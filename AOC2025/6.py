# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator
from collections import Counter


##############################################################################


file_name = "6_input.txt"
n_line = 0
n_col = 0
with open(file_name, 'r') as f:
    for line in f:
        print(line.split(" "))
        if n_line == 0:
            for i in line.split(" "):
                if i != '' and i != '\n':
                
                    n_col += 1
        n_line += 1
       
res = np.zeros((n_line-1,n_col))
ops = []
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        if line_idx < n_line-1:
            row_idx = 0
            print(line.split(" "))
            for  row in (line.split(" ")):
                if row != '' and row != '\n':
                    res[line_idx,row_idx] = int(row)
                    row_idx = row_idx +1
        elif line_idx == n_line-1:
            for  row in (line.split(" ")[:-1]):
                if row != '':
                    ops.append(row)
                    
count = 0
for idx_i,i in enumerate(ops):
    if i == '+':
        count = count + sum(res[:,idx_i])
    elif i == '*':
        count = count + reduce(operator.mul, [k for k in res[:,idx_i]], 1)
print(count)

##############################################################################

n_line = 0
n_col = 0
with open(file_name, 'r') as f:
    for line in f:
        
        if n_line == 0:
            aa = line
            n_col = len(line[:-1])
                    
        n_line += 1 
        
res2 = np.zeros((n_line-1,n_col))
columns = np.zeros(n_col)

with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        if line_idx < n_line-1:
            for row_idx,row in enumerate(line[:-1]):
                if row != ' ':
                    res2[line_idx,row_idx] = int(row)
                    
idx_zeros = np.where(~res2.any(axis=0))[0]
idx_column = 0
for i in range(len(columns)):
    columns[i] = idx_column
    if i in idx_zeros:
        idx_column += 1
        
def extract_number(matrix):
    numbers = []
    for i in range(matrix.shape[1]):
        if np.any(matrix[:,i]):
            num = []
            for j in range(matrix.shape[0]):
                num.append(int(matrix[j,i]))
            num = num[next(x for x, val in enumerate(num) if val > 0):]
            idx = np.max(np.nonzero(num))
            num = num[:(idx+1)]
            numbers.append(sum(j*10**(len(num)-(idx_j+1)) for idx_j,j in enumerate(num)))
    return numbers

count = 0
for i in np.unique(columns):
    i = int(i)
    idx = np.where(columns==i)[0]
    matrix = res2[:,idx]
    numbers = extract_number(matrix)
    if ops[i] == '+':
        count = count + sum(numbers)
    elif ops[i] == '*':
        count = count + reduce(operator.mul, [k for k in numbers], 1)
print(count)
    
                
                    
          

            