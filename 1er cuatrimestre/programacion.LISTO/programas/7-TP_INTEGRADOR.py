# -*- coding: utf-8 -*-
"""
Autor: Lautaro Santos Da Silveira 
Fecha: 20/05/21
Tema: PT integrador
Curso: Programación 1 - IA
"""
def max_de_tres(a, b, c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        if c<a and c<b:
            return c
#################### fin de función min de tres #############################
def DescubrirMenor():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    c= int(input("ingrese el valor de C: "))
    
    print(max_de_tres(a, b, c))
#################### fin de procedimiento descubrir menor ####################
def tipo(a, b, c):
    
    tr= a+b+c
    
    if tr==180: 
        if a<90 and b<90 and c<90:
            res="Las medidas ingresadas corresponden a un triángulo acutángulo"
            return res

            
    
        elif  a==90 or b==90 or c==90:
            res="las medidas ingresadas corresponden a un triángulo rectángulo"
            return res
        else: 
            res="las medidas ingresadas corresponden a un triángulo obtusángulo"
            return res
    else:
        res="las medidas ingresadas no corresponden a un triángulo"
        return res
############################ fin de función tipo #############################
def TipoDeTriangulo():
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    print(tipo(a, b, c))
#################### fin de procedimiento tipo de triangulo ###################
def contador(texto):
    res= int(0)
    for x in texto:
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
            res=res+1
    return res
############################ fin de función contador #########################
def ContarVocales():
    texto= input("ingrese un texto: ")
    print(contador(texto))
#################### fin de procedimiento contar vocales ######################
def palindromo(palabra):
    cadNueva=str("")
    res=str("")
    for x in palabra:
        cadNueva= x+cadNueva
        
    if palabra==cadNueva:
        res="verdadera"
    else:
        res="falsa"
    return res
############################ fin de función palindromo #########################
def EsPalindromo():
    palabra=input("ingrese una palabra: ")
    print(palindromo(palabra))

#################### fin de procedimiento es palindromo ######################

#################### fin de procedimientos ##################################
print("En este programa puedes hacer las siguientes operaciones:")
print("1 - Conocer cuál es el menor de tres números.")
print("2 - Conocer cuál es el tipo de triángulo.")
print("3 - Conocer cuántas vocales tiene una oración.")
print("4 - Conocer si una palabra es un palíndromo.")
op= int(input("Ingresa el número que corresponde a tu elección: "))

if op==1:
    print(DescubrirMenor())
elif op == 2 :
    print(TipoDeTriangulo())
elif op == 3 :
    print(ContarVocales())
elif op == 4 :
    print(EsPalindromo())
else:
    print("Esa opción no está disponible")