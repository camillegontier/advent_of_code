# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import itertools
import numpy as np

file_name = "10_input.txt"
n_line = 0
with open(file_name, 'r') as f:
    for line in f:
        n_line += 1
        
goals = {}
inputs = {}
        
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        temp = []
        for i in line[:-1].split(' ')[0][1:-1]:
            if i == ".":
                temp.append(0)
            elif i == "#":
                temp.append(1)
                
        goals[line_idx] = temp
        temp = []
        for i in line[:-1].split(' ')[1:-1]:
            temp_ = []
            for j in i[1:-1].split(","):
                temp_.append(int(j))
            temp.append(temp_)
        inputs[line_idx] = temp


count = 0
for line in range(n_line):            
    goal = goals[line]
    solved = False
    n = 0
    while solved == False:
        n = n +1
        for input_ in itertools.combinations_with_replacement(inputs[line], n):
            res = np.zeros(len(goal),int)
            for i in input_:
                for j in i:
                    res[j] = res[j] + 1
                    res[j] = res[j]%2
            if np.all(res==np.array(goal)):
               solved = True
    count = count + n
print(count)

###############################################################################

import scipy.optimize as optim

file_name = "10_input.txt"
n_line = 0
with open(file_name, 'r') as f:
    for line in f:
        n_line += 1
        
goals = {}
inputs = {}
        
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        line
        temp = []
        for i in line[:-1].split(' ')[-1][1:-1].split(","):
            temp.append(int(i))
                
        goals[line_idx] = temp
        temp = []
        for i in line[:-1].split(' ')[1:-1]:
            temp_ = []
            for j in i[1:-1].split(","):
                temp_.append(int(j))
            temp.append(temp_)
        inputs[line_idx] = temp


count = 0
for line in range(n_line):       
    print(line)     
    goal = goals[line]
    input_ = inputs[line]
    c = np.asarray([1]*len(input_))
    A = np.zeros((len(goal),len(input_)))
    for i in range(len(input_)):
        A[input_[i],i] = 1     
    opt = optim.linprog(c, A_eq=A,b_eq = goal,integrality=1)
    
   
    count = count + opt.fun
print(count)
    
