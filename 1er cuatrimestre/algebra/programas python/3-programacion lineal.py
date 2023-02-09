# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:15:20 2021

@author: Usuario
"""


from scipy.optimize import linprog

c=[-2,-3]

A_ub=[[-3, 2],
      [-7, 4],
      [ 1, 0]]

b_ub=[-300,
      3500,
        370]

res=linprog(c, A_ub, b_ub, bounds=((0,None),(0,None)))
print(res)
