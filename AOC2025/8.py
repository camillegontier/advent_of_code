# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np

file_name = "8_input.txt"
n_line = 0
with open(file_name, 'r') as f:
    for line in f:
        n_line += 1
        
inpt = np.zeros((n_line,3))
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        inpt[line_idx,:] = line[:-1].split(',')
        
def distance(X1,Y1,Z1,X2,Y2,Z2):
    return np.sqrt((X1-X2)**2+(Y1-Y2)**2+(Z1-Z2)**2)

###############################################################################

# i = 0
# j = 1
# distance(inpt[i,0],inpt[i,1],inpt[i,2],inpt[j,0],inpt[j,1],inpt[j,2])
# X1= inpt[i,0]
# Y1=inpt[i,1]
# Z1=inpt[i,2]
# X2=inpt[j,0]
# Y2=inpt[j,1]
# Z2=inpt[j,2]

distances = np.zeros((n_line,n_line))
for i in range(n_line):
    for j in range(i):
        distances[i,j] = distance(inpt[i,0],inpt[i,1],inpt[i,2],inpt[j,0],inpt[j,1],inpt[j,2])
        distances[j,i] = np.inf
for i in range(n_line):
    distances[i,i] = np.inf
    
groups = {}

for t in range(1000):
    print(t)
    min_idx = np.unravel_index(np.argmin(distances, axis=None), distances.shape)
    idx_0 = np.nan
    idx_1 = np.nan
    for group_idx, group in enumerate(groups.values()):
        if min_idx[0] in group:
            idx_0 = group_idx
        if min_idx[1] in group:
            idx_1 = group_idx
            
    if (not np.isnan(idx_0)) and (not np.isnan(idx_1)):
        if not idx_0 == idx_1:
            new_group = groups[idx_0] + groups[idx_1]
            groups[idx_0] = new_group
            groups[idx_1] = []
        
    elif np.isnan(idx_0) and (not np.isnan(idx_1)):
        groups[idx_1].append(min_idx[0])
    elif np.isnan(idx_1) and (not np.isnan(idx_0)):
        groups[idx_0].append(min_idx[1])
    else:
        groups[len(groups)] = [min_idx[0],min_idx[1]]
    
    distances[min_idx] = np.inf

count = 1
for i in sorted(groups, key=lambda k: len(groups[k]), reverse=True)[:3]:
    count = count*len(groups[i])
print(count)

###############################################################################

distances = np.zeros((n_line,n_line))
for i in range(n_line):
    for j in range(i):
        distances[i,j] = distance(inpt[i,0],inpt[i,1],inpt[i,2],inpt[j,0],inpt[j,1],inpt[j,2])
        distances[j,i] = np.inf
for i in range(n_line):
    distances[i,i] = np.inf
    
groups = {}
finished = False
t = 0 
while finished == False:

    print(t)
    min_idx = np.unravel_index(np.argmin(distances, axis=None), distances.shape)
    idx_0 = np.nan
    idx_1 = np.nan
    for group_idx, group in enumerate(groups.values()):
        if min_idx[0] in group:
            idx_0 = group_idx
        if min_idx[1] in group:
            idx_1 = group_idx
            
    if (not np.isnan(idx_0)) and (not np.isnan(idx_1)):
        if not idx_0 == idx_1:
            new_group = groups[idx_0] + groups[idx_1]
            groups[idx_0] = new_group
            groups[idx_1] = []
        
    elif np.isnan(idx_0) and (not np.isnan(idx_1)):
        groups[idx_1].append(min_idx[0])
    elif np.isnan(idx_1) and (not np.isnan(idx_0)):
        groups[idx_0].append(min_idx[1])
    else:
        groups[len(groups)] = [min_idx[0],min_idx[1]]
        
    idxs = sorted(groups, key=lambda k: len(groups[k]), reverse=True)[:2]
    if len(idxs) > 1:
        if len(groups[idxs[0]]) == n_line and len(groups[idxs[1]]) == 0:
            finished = True
        else:
            finished = False
        
    if finished:
        break
    else:
        distances[min_idx] = np.inf
        t = t+1

print(inpt[min_idx[0],0]*inpt[min_idx[1],0])