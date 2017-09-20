#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:26:57 2017

@author: tanay
"""

import monkdata as m
import dtree as d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


# Variables
## ATTRIBUTES
A1 = m.attributes[0]
A2 = m.attributes[1]
A3 = m.attributes[2]
A4 = m.attributes[3]
A5 = m.attributes[4]
A6 = m.attributes[5]
## DATASET
monk1 = m.monk1
monk2 = m.monk2
monk3 = m.monk3
monktest1 = m.monk1test
monktest2 = m.monk2test
monktest3 = m.monk3test
# Number of Iterations
frac = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
max_iter = 2
## ERROR FOR EACH FRACTION
itr_error = np.zeros(max_iter)

## Array for saving mean and variance values for each frac
mean_m1 = np.zeros(len(frac))
var_m1 = np.zeros(len(frac))

mean_m2 = np.zeros(len(frac))
var_m2 = np.zeros(len(frac))

mean_m3 = np.zeros(len(frac))
var_m3 = np.zeros(len(frac))




print("---------------------------MONK1---------------------------")
# The loop for the fraction
for x in range(len(frac)):
    print("#----------- Fraction: ", frac[x]," -----------#")
    # Loop for the iterations
    for itr in range(0, max_iter):
        print("# Iteration: ", itr)
        
        current_error = 1
        best_tree_id = 0
        best_error = 1
        flag = 1        
        
        # Divide monk1 into training and validation for pruning
        monk1train, monk1val = d.partition(monk1, frac[x])
        # Create tree for the train data
        best_tree = d.buildTree(monk1train, m.attributes)
        
        while (flag == 1):
            print("------------------------------------------------------")
            current_error = 1
            
            # Prune the test_tree
            prune_tree = d.allPruned(best_tree)
            print("Number of pruned tree generated: ", len(prune_tree))
            
            for i in range(len(prune_tree)):
                    error = 1 - d.check(prune_tree[i], monk1val)
                    print(error)
                    if (current_error > error):
                        current_error = error
                        best_tree_id = i
                    
            print("The current best tree is:", best_tree_id)
            print("The current best error is:", current_error)
            if(best_error > current_error):
                print("Running it again")
                best_error = current_error
                flag = 1
                best_tree = prune_tree[best_tree_id]
                
            else:
                flag = 0  
                    
        
        # Checking the best tree error against the whole dataset
        print(" ")        
        print("Error for the best pruned tree against complete Monk1: ", (1- d.check(best_tree, monktest1)))
        itr_error[itr] = 1 - d.check(best_tree, monktest1)
       

    # Calulate the mean for each iteration
#    print(itr_error)
    mean_m1[x] = np.mean(itr_error)
    var_m1[x] = np.var(itr_error)
    print("Mean", mean_m1[x])
    print("Variance", var_m1[x])


## Plots
## Plotting mean
#fig, ax1 = plt.subplots()
#plt.grid(linestyle='dotted')
#width = 0.05 # width of the bar
#ax1.axis([0.2, 0.9, 0.1, 0.25])
#ax1.set_ylabel("Mean Error")
#plt.title("Performance Chart for MONK1 dataset")
#ax1.set_xlabel("Fractions")
#ax1.bar(frac, mean_m1, width, color = 'r')
#
#
#ax2 = ax1.twinx()
#ax2.set_ylabel("Error Variance")
#ax2.axis([0.2, 0.9, 0.0005, 0.004])
#ax2.plot(frac, var_m1, 'ko', frac, var_m1, 'k', label = "Variance")
#
#red_patch = mpatches.Patch(color='red', label='Mean Error')
#blue_line = mlines.Line2D([], [], color='black', marker='o', label='Variance')
#plt.legend(handles=[red_patch, blue_line])
#
#
#print("")
#print("")
#print("---------------------------MONK2---------------------------")
## The loop for the fraction
#for x in range(len(frac)):
#    print("#----------- Fraction: ", frac[x]," -----------#")
#    # Loop for the iterations
#    for itr in range(0, max_iter):
##        print("# Iteration: ", itr)
#        
#        current_error = 1
#        best_tree_id = 0
#        best_error = 1
#        flag = 1        
#        
#        # Divide monk1 into training and validation for pruning
#        monk2train, monk2val = d.partition(monk2, frac[x])
#        # Create tree for the train data
#        best_tree = d.buildTree(monk2train, m.attributes)
#        
#        while (flag == 1):
##            print("------------------------------------------------------")
#            current_error = 1
#            
#            # Prune the test_tree
#            prune_tree = d.allPruned(best_tree)
##            print("Number of pruned tree generated: ", len(prune_tree))
#            
#            for i in range(len(prune_tree)):
#                    error = 1 - d.check(prune_tree[i], monk2val)
##                    print(error)
#                    if (current_error > error):
#                        current_error = error
#                        best_tree_id = i
#                    
##            print("The best tree is:", best_tree_id)
##            print("The best error is:", current_error)
#            if(best_error > current_error):
##                print("Running it again")
#                best_error = current_error
#                flag = 1
#                best_tree = prune_tree[best_tree_id]
#                
#            else:
#                flag = 0  
#                    
#        
#        # Checking the best tree error against the whole dataset
##        print(" ")        
##        print("Error for the best pruned tree against Monk2: ", (1- d.check(best_tree, monktest2)))
#        itr_error[itr] = 1 - d.check(best_tree, monktest2)
#       
#
#    # Calulate the mean for each iteration
##    print(itr_error)
#    mean_m2[x] = np.mean(itr_error)
#    var_m2[x] = np.var(itr_error)
#    print("Mean", mean_m2[x])
#    print("Variance", var_m2[x])
#
### Plots
### Plotting mean
##fig, ax1 = plt.subplots()
##plt.grid(linestyle='dotted')
##width = 0.05 # width of the bar
##ax1.axis([0.2, 0.9, 0.33, 0.34])
##ax1.set_ylabel("Mean Error")
##plt.title("Performance Chart for MONK2 dataset")
##ax1.set_xlabel("Fractions")
##ax1.bar(frac, mean_m2, width, color = 'r')
##
##
##ax2 = ax1.twinx()
##ax2.set_ylabel("Error Variance")
##ax2.axis([0.2, 0.9, 0.00012, 0.0003])
##ax2.plot(frac, var_m2, 'ko', frac, var_m2, 'k', label = "Variance")
##
##red_patch = mpatches.Patch(color='red', label='Mean Error')
##blue_line = mlines.Line2D([], [], color='black', marker='o', label='Variance')
##plt.legend(handles=[red_patch, blue_line])
##    
##    
##    
##print("")
##print("")
#print("---------------------------MONK3---------------------------")
## The loop for the fraction
#for x in range(len(frac)):
#    print("#----------- Fraction: ", frac[x]," -----------#")
#    # Loop for the iterations
#    for itr in range(0, max_iter):
##        print("# Iteration: ", itr)
#        
#        current_error = 1
#        best_tree_id = 0
#        best_error = 1
#        flag = 1        
#        
#        # Divide monk1 into training and validation for pruning
#        monk3train, monk3val = d.partition(monk3, frac[x])
#        # Create tree for the train data
#        best_tree = d.buildTree(monk3train, m.attributes)
#        
#        while (flag == 1):
##            print("------------------------------------------------------")
#            current_error = 1
#            
#            # Prune the test_tree
#            prune_tree = d.allPruned(best_tree)
##            print("Number of pruned tree generated: ", len(prune_tree))
#            
#            for i in range(len(prune_tree)):
#                    error = 1 - d.check(prune_tree[i], monk3val)
##                    print(error)
#                    if (current_error > error):
#                        current_error = error
#                        best_tree_id = i
#                    
##            print("The best tree is:", best_tree_id)
##            print("The best error is:", current_error)
#            if(best_error > current_error):
##                print("Running it again")
#                best_error = current_error
#                flag = 1
#                best_tree = prune_tree[best_tree_id]
#                
#            else:
#                flag = 0  
#                    
#        
#        # Checking the best tree error against the whole dataset
##        print(" ")        
##        print("Error for the best pruned tree against Monk2: ", (1- d.check(best_tree, monktest2)))
#        itr_error[itr] = 1 - d.check(best_tree, monktest3)
#       
#
#    # Calulate the mean for each iteration
##    print(itr_error)
#    mean_m3[x] = np.mean(itr_error)
#    var_m3[x] = np.var(itr_error)
#    print("Mean", mean_m3[x])
#    print("Variance", var_m3[x])
#
### Plots
### Plotting mean
##fig, ax1 = plt.subplots()
##plt.grid(linestyle='dotted')
##width = 0.05 # width of the bar
##ax1.axis([0.2, 0.9, 0.01, 0.1])
##ax1.set_ylabel("Mean Error")
##plt.title("Performance Chart for MONK3 dataset")
##ax1.set_xlabel("Fractions")
##ax1.bar(frac, mean_m3, width, color = 'r')
##
##
##ax2 = ax1.twinx()
##ax2.set_ylabel("Error Variance")
##ax2.axis([0.2, 0.9, 0.0008, 0.005])
##ax2.plot(frac, var_m3, 'ko', frac, var_m3, 'k', label = "Variance")
##
##red_patch = mpatches.Patch(color='red', label='Mean Error')
##blue_line = mlines.Line2D([], [], color='black', marker='o', label='Variance')
##plt.legend(handles=[red_patch, blue_line])
#
#
### Plotting all togther
##plt.title("Performance Chart for All Dataset")
##plt.ylabel("Mean Error")
##plt.xlabel("Fractions")
##p1, = plt.plot(frac, mean_m1, 'r', label = "MONK1")
##p2, = plt.plot(frac, mean_m2, 'b', label = "MONK2")
##p3, = plt.plot(frac, mean_m3, 'g', label = "MONK3")
##plt.legend(handles = [p1, p2, p3])