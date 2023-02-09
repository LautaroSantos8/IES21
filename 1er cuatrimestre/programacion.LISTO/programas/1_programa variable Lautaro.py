# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:57:53 2021

@author: Usuario
"""
print("ingrese dos n{umeros para realizar operaciones aritmeticas")

print("==========================================================")

a= int(input("ingrese el valor de A: "))

b= int(input("ingrese el valor de B: "))



VarSuma= a+b 
print(f"Suma = {VarSuma}")

VarResta= a-b 
print(f"Resta = {VarResta}")

VarProd= a*b 
print(f"Producto = {VarProd}")

VarDivDec= a/b 
print(f"División Decimal = {VarDivDec}")

VarDivEnt= a//b 
print(f"División entera = {VarDivEnt}")

VarRestDiv= a%b 
print(f"Resto de División = {VarRestDiv}")

VarPotencia= a**b 
print(f"Potencia = {VarPotencia}")