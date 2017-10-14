
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:43:53 2017

@author: tanay
"""

from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy as np
import pylab , random, math
import kernal as k


" --- Input Variables --- "
t = 10        # Variable for polynomial power or sigma
slack1 = 0.1    # Slack variable 1
slack2 = 10     # Slack variable 2
# Variable to choose the kernal
case = 3       # 1: Linear      2: Polynomial      3: Radial     Others: Idoit!

## Also check for the kernal used in line28, line35 and line55.
## All the kernals should be same!! 



def kernal(case, data1, data2, t = 1):
    if case == 1:
        return k.linearkernal(data1, data2)
    elif case == 2:
        return k.polynomialkernal(data1, data2, t)
    elif case == 3:
        return k. radicalbasekernal(data1, data2, t)
    else:
        print("Wrong Input")
        


# Indicator funtion
def indicator(x, y):
    result = 0
    for j in range(len(non_zero_alpha)):
             result = result + non_zero_alpha[j]*landmarks[j][2]*kernal(case, (x,y), landmarks[j][0:2], t)
#             result = result + non_zero_alpha[j]*landmarks[j][2]*k.radicalbasekernal((x,y), landmarks[j][0:2], t)
    return result




" --- Generate Training Data --- "
random.seed (100)
classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range (5)] + [(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range (5)]
classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5, 0.5), -1.0) for i in range (10)]
train_data = classA + classB
random.shuffle(train_data)



# Variables
P = np.zeros((len(train_data), len(train_data)))
" --- The P matrix ---"
for i in range (len(train_data)):
    for j in range (len(train_data)):
        P[i][j] = train_data[i][2]*train_data[j][2]*kernal(case, train_data[i][0:2], train_data[j][0:2], t)
#        P[i][j] = train_data[i][2]*train_data[j][2]*k.radicalbasekernal(train_data[i][0:2], train_data[j][0:2], t)

" ------------------------- Without Slack variable -------------------------- "
" --- The q, G and h matrix ---"
q = -1 * np.ones(len(train_data))
h = np.zeros(len(train_data))
G = -1 * np.eye(len(train_data))




" --- Convex Optimization ---"
print("")
print("Without Slack")
r = qp(matrix(P), matrix(np.transpose(q)), matrix(G), matrix(h))
alpha = list(r['x']) 





# Variables
landmarks = []
non_zero_alpha = []
" --- Indicator function ---"
for i in range(len(alpha)):
    if(alpha[i] > math.pow(10, -5)):
        non_zero_alpha.append(alpha[i])
        landmarks.append(train_data[i][0:3])
        
        
" --- Plot Data without slack ---"
pylab.figure(1)
pylab.xlim(-7, 7)
pylab.ylim(-7, 7)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('Training Data', fontsize = 15)
pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
pylab.savefig("Radial/TrainngData.png")

xrange = np.arange(-7, 7, 0.05)
yrange = np.arange(-7, 7, 0.05)
pylab.title('Radial Kernel Sigma = 10', fontsize = 15)
grid = matrix([[indicator(x , y) for y in yrange] for x in xrange])
CS = pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black','blue'), linewidths = (1,3,1))
pylab.clabel(CS, inline = 1, fontsize = 8)
pylab.savefig("Radial/Radial Kernel Sigma_10.png")



#" -------------------------- Adding Slack variable -------------------------- "
## Indicator funtion with slack
#def indicator_slk(x, y):
#    result = 0
#    for j in range(len(non_zero_alpha_slk)):
#             result = result + non_zero_alpha_slk[j]*landmarks_slk[j][2]*kernal(case, (x,y), landmarks_slk[j][0:2], t)
##             result = result + non_zero_alpha_slk[j]*landmarks_slk[j][2]*k.radicalbasekernal((x,y), landmarks_slk[j][0:2], t)
#    return result
#
#
#" --- The G and h matrix ---"
#upper_G = +1*np.eye(len(train_data))
#lower_G = -1*np.eye(len(train_data))
#G_slk = np.concatenate((upper_G, lower_G), axis = 0)
#
#
#upper_h = slack1*np.ones(len(train_data))
#lower_h = np.zeros(len(train_data))
#h_slk = np.concatenate((upper_h, lower_h), axis = 0)
#
#" --- Convex Optimization on slack variable matrix ---"
#print("")
#print("With Slack")
#r = qp(matrix(P), matrix(np.transpose(q)), matrix(G_slk), matrix(h_slk))
#alpha_slk = list(r['x']) 
#
#
## Variables
#landmarks_slk = []
#non_zero_alpha_slk = []
#" --- Indicator function ---"
#for i in range(len(alpha)):
#    if(alpha_slk[i] > math.pow(10, -5)):
#        non_zero_alpha_slk.append(alpha_slk[i])
#        landmarks_slk.append(train_data[i][0:3])
#
#
#print("")
#print("")
#print("Landmarks wihout slack: ", len(landmarks))
#print("Landmarks with slack: ", len(landmarks_slk))
#
#
#
#" --- Plot Data with slack ---"
#pylab.figure(2)
#pylab.xlabel('x')
#pylab.ylabel('y')
#pylab.title('Radial Kernel Sigma = 10 Slack = 0.1', fontsize = 15)
#pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
#pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
#
#xrange = np.arange(-7, 7, 0.05)
#yrange = np.arange(-7, 7, 0.05)
#grid = matrix([[indicator_slk(x , y) for y in yrange] for x in xrange])
#CS = pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black','blue'), linewidths = (1,3,1))
#pylab.clabel(CS, inline = 1, fontsize = 8)
#pylab.savefig("Radial/Radial Kernel Sigma_10_Slack_0.1.png")
#
#
#
#
#
#
#
#" --- The G and h matrix ---"
#upper_G = +1*np.eye(len(train_data))
#lower_G = -1*np.eye(len(train_data))
#G_slk = np.concatenate((upper_G, lower_G), axis = 0)
#
#
#upper_h = slack2*np.ones(len(train_data))
#lower_h = np.zeros(len(train_data))
#h_slk = np.concatenate((upper_h, lower_h), axis = 0)
#
#" --- Convex Optimization on slack variable matrix ---"
#print("")
#print("With Slack")
#r = qp(matrix(P), matrix(np.transpose(q)), matrix(G_slk), matrix(h_slk))
#alpha_slk = list(r['x']) 
#
#
## Variables
#landmarks_slk = []
#non_zero_alpha_slk = []
#" --- Indicator function ---"
#for i in range(len(alpha)):
#    if(alpha_slk[i] > math.pow(10, -5)):
#        non_zero_alpha_slk.append(alpha_slk[i])
#        landmarks_slk.append(train_data[i][0:3])
#
#
#print("")
#print("")
#print("Landmarks wihout slack: ", len(landmarks))
#print("Landmarks with slack: ", len(landmarks_slk))
#
#
#
#" --- Plot Data with slack ---"
#pylab.figure(3)
#pylab.xlabel('x')
#pylab.ylabel('y')
#pylab.title('Radial Kernel Sigma = 10 Slack = 10', fontsize = 15)
#pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
#pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
#
#xrange = np.arange(-7, 7, 0.05)
#yrange = np.arange(-7, 7, 0.05)
#grid = matrix([[indicator_slk(x , y) for y in yrange] for x in xrange])
#CS = pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black','blue'), linewidths = (1,3,1))
#pylab.clabel(CS, inline = 1, fontsize = 8)
#pylab.savefig("Radial/Radial Kernel Sigma_10_Slack_10.png")