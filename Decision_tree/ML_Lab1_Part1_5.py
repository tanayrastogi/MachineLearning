# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import monkdata as m
import dtree as d
import drawtree_qt5 as draw


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



print("#---------------- Assignment 1 and 2 ----------------#")
print (" ")
# Entropy Calculation from Monk dataset on training variables
print ("Entropy Monk1 dataset: ", d.entropy(monk1))
print ("Entropy Monk2 dataser: ", d.entropy(monk2)) 
print ("Entropy Monk3 dataset: ", d.entropy(monk3)) 
print (" ")


print("#---------------- Assignment 3 and 4 ----------------#")
print (" ")
print("Information gain for the MONK1 dataset")
for i in range (0,6):
    print(" Info Gain ", m.attributes[i],":", d.averageGain(monk1, m.attributes[i]))
print (" ")
print("Information gain for the MONK2 dataset")
for i in range (0,6):
    print(" Info Gain ", m.attributes[i],":", d.averageGain(monk2, m.attributes[i]))
print (" ")
print("Information gain for the MONK3 dataset")
for i in range (0,6):
    print(" Info Gain ", m.attributes[i],":", d.averageGain(monk3, m.attributes[i]))
print (" ")


print("#----------------Assignment 5 ----------------#")
print (" ")
# Splitting the tree for MONK1 data
print("#---- For MONK1 dataset -----#")
for i in (1,2,3,4):
    for j in range(0,6):
        print("Information gain for split for A5 at value ", i," at", m.attributes[j]," :", d.averageGain(d.select(monk1, A5, i), m.attributes[j]))
    print(" ")
    
    
print (" ")
# Build Tree using PyQT graph

# MONK1 Tree
#draw.drawTree(d.buildTree(monk1, m.attributes))
print("Classification error for dataset [in fraction]")
print("MONK1 with train data ", (1- d.check(d.buildTree(monk1, m.attributes), monk1)))
print("MONK1 with test  data ", (1- d.check(d.buildTree(monk1, m.attributes), monktest1)))
# MONK2 Tree
#draw.drawTree(d.buildTree(monk2, m.attributes))
print("MONK2 with train data ", (1- d.check(d.buildTree(monk2, m.attributes), monk2)))
print("MONK2 with test  data", (1- d.check(d.buildTree(monk2, m.attributes), monktest2)))
# MONK3 Tree
#draw.drawTree(d.buildTree(monk3, m.attributes, 2))
print("MONK3 with train data ", (1- d.check(d.buildTree(monk3, m.attributes), monk3)))
print("MONK3 with test  data", (1- d.check(d.buildTree(monk3, m.attributes), monktest3)))



