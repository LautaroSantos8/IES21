# -*- coding: utf-8 -*-
"""
Ejemplo función linprog para resolver Sistema Prog Lineal
Caso: SP3
"""

from scipy.optimize import linprog
c=[2,3]
A_ub=[[-1, 0],
      [ 0, 1],
      [ 1, -3]]
b_ub=[ -5,
        2,
        5] 
res=linprog(c, A_ub, b_ub, bounds=((0,None),(0,None)))
print(res)

