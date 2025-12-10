# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:18:16 2022

@author: gontier
"""

import numpy as np
import matplotlib.pyplot as plt
import functools
# %matplotlib qt

file_name = "9_input.txt"
n_line = 0
with open(file_name, 'r') as f:
    for line in f:
        n_line += 1
        
inpt = np.zeros((n_line,2))
with open(file_name, 'r') as f:
    for line_idx, line in enumerate(f):
        inpt[line_idx,:] = line[:-1].split(',')
        
def area(X1,Y1,X2,Y2):
    return (np.abs(X1-X2)+1)*(np.abs(Y1-Y2)+1)

areas = np.zeros((n_line,n_line))
for i in range(n_line):
    for j in range(i):
        areas[i,j] = area(inpt[i,0],inpt[i,1],inpt[j,0],inpt[j,1])

print(np.max(areas))

###############################################################################

# inpt = np.array([[1,1],
#                  [10,1],
#                  [10,10],
#                  [1,10],
#                  [1,8],
#                  [8,8],
#                  [8,2],
#                  [1,2]])

def compute_line(inpt):
    line = np.array([inpt[0,0],inpt[0,1]])
    for i in range(1,inpt.shape[0]):
        print(i)
        if inpt[i,0] == inpt[i-1,0]:
            if inpt[i,1]-inpt[i-1,1]>0:
                for j in range(int(min(inpt[i,1],inpt[i-1,1])+1),int(max(inpt[i,1],inpt[i-1,1])+1)):
                    line = np.vstack((line,[inpt[i,0],int(j)]))
            else:
                for j in range(int(min(inpt[i,1],inpt[i-1,1])),int(max(inpt[i,1],inpt[i-1,1]))):
                    line = np.vstack((line,[inpt[i,0],int(j)]))
    
        elif inpt[i,1] == inpt[i-1,1]:
            if inpt[i,0]-inpt[i-1,0]<0:
                for j in range(int(min(inpt[i,0],inpt[i-1,0])),int(max(inpt[i,0],inpt[i-1,0]))):
                    line = np.vstack((line,[int(j),inpt[i,1]]))
            else:
                for j in range(int(min(inpt[i,0],inpt[i-1,0])+1),int(max(inpt[i,0],inpt[i-1,0])+1)):
                    line = np.vstack((line,[int(j),inpt[i,1]]))  
                    
    i = 0 
    if inpt[i,0] == inpt[i-1,0]:
        if inpt[i,1]-inpt[i-1,1]>0:
            for j in range(int(min(inpt[i,1],inpt[i-1,1])+1),int(max(inpt[i,1],inpt[i-1,1])+1)):
                line = np.vstack((line,[inpt[i,0],int(j)]))
        else:
            for j in range(int(min(inpt[i,1],inpt[i-1,1])),int(max(inpt[i,1],inpt[i-1,1]))):
                line = np.vstack((line,[inpt[i,0],int(j)]))
    
    elif inpt[i,1] == inpt[i-1,1]:
        if inpt[i,0]-inpt[i-1,0]<0:
            for j in range(int(min(inpt[i,0],inpt[i-1,0])),int(max(inpt[i,0],inpt[i-1,0]))):
                line = np.vstack((line,[int(j),inpt[i,1]]))
        else:
            for j in range(int(min(inpt[i,0],inpt[i-1,0])+1),int(max(inpt[i,0],inpt[i-1,0])+1)):
                line = np.vstack((line,[int(j),inpt[i,1]]))     
    return line

@functools.cache
def is_legal(x,y):
    idx = np.where(line[:,0] == x)[0]
    if (line[idx,1] <= y).any() and (line[idx,1] >= y).any() :
        truex=True
    else:
        truex=False
        
    idx = np.where(line[:,1] == y)[0]
    if (line[idx,0] <= x).any() and (line[idx,0] >= x).any() :
        truey=True
    else:
        truey=False
    return truex,truey
    

line = compute_line(inpt)          
plt.plot()
plt.scatter(line[:,0],line[:,1])

from shapely.geometry import LineString, Point, Polygon, box
import shapely

polygon = Polygon([(int(inpt[k,0]), int(inpt[k,1])) for k in range(inpt.shape[0])])
polygon_ext = LineString(list(polygon.buffer(1e-2).exterior.coords))
            
max_area = 0
for i in range(n_line):
    print(i)
    for j in range(i+1,n_line):
        # print(j)
        area_temp = area(inpt[i,0],inpt[i,1],inpt[j,0],inpt[j,1])
        angles = np.array([[(inpt[i,0]),(inpt[i,1])],
                           [(inpt[j,0]),(inpt[i,1])],
                  [(inpt[j,0]),(inpt[j,1])],
                  [(inpt[i,0]),(inpt[j,1])]])
        
        # Check angles
        line_candidate = angles
        truex = []
        truey = []
        for k in range(line_candidate.shape[0]):
            x = line_candidate[k,0]
            y = line_candidate[k,1]
            [truex_,truey_] = is_legal(x,y)
            truex.append(truex_)
            truey.append(truey_)
            
            
     
            
            
            
         
        
        point_a = Point(int(inpt[i,0]), int(inpt[i,1]))
        point_b = Point(int(inpt[j,0]), int(inpt[i,1]))
        segment = LineString([point_a, point_b]) 
        line1 = shapely.intersection(polygon_ext, segment).is_empty
        
        point_a = Point(int(inpt[j,0]), int(inpt[i,1]))
        point_b = Point(int(inpt[j,0]), int(inpt[j,1]))
        segment = LineString([point_b, point_a])
        line2 = shapely.intersection(polygon_ext, segment).is_empty
        
        point_a = Point(int(inpt[j,0]), int(inpt[j,1]))
        point_b = Point(int(inpt[i,0]), int(inpt[j,1]))
        segment = LineString([point_a, point_b])
        line3 = shapely.intersection(polygon_ext, segment).is_empty
        
        point_a = Point(int(inpt[i,0]), int(inpt[j,1]))
        point_b = Point(int(inpt[i,0]), int(inpt[i,1]))
        segment = LineString([point_a, point_b])
        line4 = shapely.intersection(polygon_ext, segment).is_empty
        
        
        # point_a = Point(int(40000), int(80000))
        # point_b = Point(int(60000), int(80000))
        # segment = LineString([point_a, point_b])
        # line4 = shapely.intersection(polygon_ext, segment).is_empty
        
        if line1 and line2 and line3 and line4:
            print(i)
            print(j)
        
        
        
        if np.all(truey) and np.all(truey) and line1 and line2 and line3 and line4:
            if area_temp > max_area:
                max_area = area_temp
      
           
                
        # if np.all(truey) and np.all(truey) and line1 and line2 and line3 and line4:
        #     if area_temp > max_area:
        #         max_area = area_temp
        
        # top = max(inpt[i,1],inpt[j,1])
        # bottom = min(inpt[i,1],inpt[j,1])
        # left = min(inpt[i,0],inpt[j,0])
        # right = max(inpt[i,0],inpt[j,0])
        
        # # Test
        # angles = np.array([[(40000.),(60000.)],
        #                    [(60000.),(60000.)],
        #           [(60000.),(20000.)],
        #           [(40000.),(20000.)]])
        # idx1 = np.where((line[:,0] == angles[0,1]) & (line[:,1] >= 40000) & (line[:,1] <= 60000))[0]
        # line[idx1]
       
        
        
            
        # # Check line
        # idx = np.where((line[:,1] == top) & (line[:,0] >= left) & (line[:,0] <= right))[0]
        # temp = line[idx][:,0]
        # temp.sort()   
        # line1 = True
        # for k in np.where(np.diff(temp)>1)[0] :
        #     y = inpt[i,1]
        #     x = temp[k]+1
        #     if np.all(is_legal(x,y)):
        #         line1 = True
        #     else:
        #         line1 = False
                
        # idx = np.where((line[:,1] == bottom) & (line[:,0] >= left) & (line[:,0] <= right))[0]
        # temp = line[idx][:,0]
        # temp.sort()   
        # line2 = True
        # for k in np.where(np.diff(temp)>1)[0] :
        #     y = inpt[j,1]
        #     x = temp[k]+1
        #     if np.all(is_legal(x,y)):
        #         line2 = True
        #     else:
        #         line2 = False
                
        # idx = np.where((line[:,0] == left) & (line[:,1] >= bottom) & (line[:,1] <= top))[0]
        # temp = line[idx][:,1]
        # temp.sort()   
        # line3 = True
        # for k in np.where(np.diff(temp)>1)[0] :
        #     x = inpt[i,0]
        #     y = temp[k]+1
        #     if np.all(is_legal(x,y)):
        #         line3 = True
        #     else:
        #         line3 = False
                
        # idx = np.where((line[:,0] == right) & (line[:,1] >= bottom) & (line[:,1] <= top))[0]
        # temp = line[idx][:,1]
        # temp.sort()   
        # line4 = True
        # for k in np.where(np.diff(temp)>1)[0] :
        #     x = inpt[j,0]
        #     y = temp[k]+1
        #     if np.all(is_legal(x,y)):
        #         line4 = True
        #     else:
        #         line4 = False
        

        # if np.all(truey) and np.all(truey) and line1 and line2 and line3 and line4:
        #         if area_temp > max_area:
        #             max_area = area_temp

        
        # # Check angles
        # line_candidate = angles
        # truex = []
        # truey = []
        # for k in range(line_candidate.shape[0]):
        #     
            
        #     idx = np.where(line[:,0] == x)[0]
        #     if (line[idx,1] <= y).any() and (line[idx,1] >= y).any() :
        #         truex.append(True)
        #     else:
        #         truex.append(False)
                
        #     idx = np.where(line[:,1] == y)[0]
        #     if (line[idx,0] <= x).any() and (line[idx,0] >= x).any() :
        #         truey.append(True)
        #     else:
        #         truey.append(False)
        
        

     