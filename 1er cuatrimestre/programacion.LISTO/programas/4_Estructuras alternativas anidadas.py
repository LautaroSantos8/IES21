# -*- coding: utf-8 -*-
"""
Autor: Lautaro Santos Da Silveira 
Fecha: 29/04/21
Tema:Estructuras alternativas anidadas
Curso: Programación 1 - IA
Programa a desarrollar: Progtrama que calcula el IMC de una persona

"""

a= float(input("Escriba su peso: "))

b= float(input("Escriba su altura: "))

IMC= a/b**2

print(f"su IMC es = {IMC}")

if IMC<18.5:
    print("Tienes poco peso")
    
elif IMC < 24.9:
    print("Tu peso es el adecuado")
    
elif IMC < 29.9:
    print("Estás con sobrepeso")
    
elif IMC < 34.9:
    print("Tienes obesidad de 1°")
    
elif IMC < 39.9:
    print("Tienes obesidad de 2°")
    
elif IMC < 49.9:
    print("Tienes obesidad de 3°")
    
else: 
    print("Tienes obesidad de 4°")