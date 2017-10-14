#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:33:15 2017

@author: tanay
"""

import numpy as np
import math

def linearkernal(x1, x2):
    # Here x1 and x2 are vectors
    return (np.dot(x1, x2) + 1)

def polynomialkernal(x1, x2, p):
    # Here x1 and x2 are vectors
    # p is the degree of polynomial
    eq = np.dot(x1, x2) + 1
    return math.pow(eq, p)

def radicalbasekernal(x1, x2, sigma = 1):
    # Return the radical base
    # First the subration of vector and then doing the dot product
    # a = np.dot(np.subtract(x1,x2), np.subtract(x1,x2))
    # Dividing by the sigma term
    # b = a / 2*math.pow(sigma,2)
    # Then calculting the exponent term
    # c = math.exp(-b)
    # Default for sigma is 1
    return math.exp(-((np.dot(np.subtract(x1,x2), np.subtract(x1,x2))) / 2*math.pow(sigma,2)))
    

