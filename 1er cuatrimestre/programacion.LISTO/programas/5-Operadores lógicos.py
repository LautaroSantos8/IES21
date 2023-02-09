# -*- coding: utf-8 -*-
"""
Autor: Lautaro Santos Da Silveira 
Fecha: 29/04/21
Tema: Operadores lógicos
Curso: Programación 1 - IA
Programa a desarrollar: programa que diga el tipo de triangulo 
"""

a= float(input("ingrese el valor A: "))

b= float(input("ingrese el valor B: "))

c= float(input("ingrese el valor C: "))

if a==b and b==c: 
    print("Es un triangulo equilatero")

elif a==b and b!=c or b==c and c!=a or c==a and a!=b :
    print ("es un triangulo isosceles ")
    
else:
    print("es un triangulo escaleno")
    