#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:32:33 2017

@author: tanay
"""

from cvxopt.solvers import qp
from cvxopt.base import matrix
import math
import kernal as k

class Classifier:
    def __init__ (self, data):
        self.data = data
        
        self.alpha = []
        self.non_zero_alpha = []
        self.landmarks = []
        self.result = 0
    
    def optimizer(self,P, q, G, h):
        r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
        self.alpha = list(r['x']) 
        return self.alpha
    

    def indicator(self, x, y):
        for i in range(len(self.alpha)):
            if(self.alpha[i] > math.pow(10, -5)):
                self.non_zero_alpha.append(self.alpha[i])
                self.landmarks.append(self.data[i][0:3])
        
        for j in range(len(self.non_zero_alpha)):
            self.result = self.result + self.non_zero_alpha[j]*self.landmarks[j][3]*k.radicalbasekernal((x,y), self.landmarks[j][0:2], 1)
        
        return self.result
        
    