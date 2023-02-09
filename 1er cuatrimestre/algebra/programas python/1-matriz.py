# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:23:40 2021

@author: Usuario
"""

import numpy as np

a= np.array([[], [5, 2]])
              
b= np.array ([[0], [8]])
               
resultado= (np.linalg.solve(a, b))

print(f"los valores de las incognitas son: {resultado}")