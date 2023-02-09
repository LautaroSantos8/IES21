# -*- coding: utf-8 -*-
"""
fecha: 15/5/21

@author: Lautaro Santos Da Silveira
"""
######################## inicio de sector de procedimientos ##################        
def Procedimiento_1():
    from random import randint
    a= int(randint(1,6))
    print(f"el valor que sacó el jugador 1 es {a}")
    print(" ")
    b= int(randint(1,6))
    print(f"el valor que sacó el jugador 2 es {b}")
    print(" ")
    if a>b:
        print("el ganador es el jugador 1")
    elif a<b:
        print("el ganador es el jugador 2")
    else: 
        print("empate")
######################## fin de procedimiento 1 ###############################        
def Procedimiento_2():
    from random import randint
    a= int(randint(1,6))
    print(f"el valor del 1er dado que sacó el jugador 1 es {a}")
    print(" ")
    b= int(randint(1,6))
    print(f"el valor del 2do dado que sacó el jugador 1 es {b}")
    print(" ")
    c= int(randint(1,6))
    print(f"el valor del 1er dado que sacó el jugador 2 es {c}")
    print(" ")
    d= int(randint(1,6))
    print(f"el valor del 2do dado que sacó el jugador 2 es {d}") 
    print(" ")
    Jugador1= a+b 
    Jugador2= c+d
    if Jugador1 > Jugador2:
        print("el ganador es el jugador 1")
    elif Jugador1 < Jugador2:
        print("el ganador es el jugador 2")
    else:
        if a>c or a>d or b>c or b>d:
            print("el ganador es el jugador 1")
        elif a<c or a<d or b<c or b<d:
            print("el ganador es el jugador 2")
        else:
            print("empate")
######################## fin de procedimiento 2 ###############################        
def resolucion(opcion1, opcion2):
    if opcion1 == 1:
        elección1 = "piedra"
    elif opcion1 == 2:
        elección1 = "papel"
    elif opcion1 == 3:
        elección1 = "tijera"
    print("Jugador 1 eligió: ", elección1)

    if opcion2 == 1:
        elección2 = "piedra"
    elif opcion2 == 2:
        elección2 = "papel"
    elif opcion2 == 3:
        elección2 = "tijera"
    print("Jugador 2 eligió: ", elección2)
    print("...")

    if elección2 == "piedra" and elección1 == "papel":
        respuesta="Ganaste jugador 1"
        return respuesta
    elif elección2 == "papel" and elección1 == "tijera":
        respuesta="Ganaste jugador 1"
        return respuesta
    elif elección2 == "tijera" and elección1 == "piedra":
        respuesta="Ganaste jugador 1"
        return respuesta
    if elección2 == "papel" and elección1 == "piedra":
        respuesta="Ganaste jugador 2"
        return respuesta
    elif elección2 == "tijera" and elección1 == "papel":
        respuesta="Ganaste jugador 2"
        return respuesta
    elif elección2 == "piedra" and elección1 == "tijera":
        respuesta="Ganaste jugador 2"
        return respuesta
    elif elección2 == elección1:
        respuesta="empate"
        return respuesta
######################## fin de funcion    #    ##############################        
def Procedimiento_3():
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    opcion1 = int(input("Que elijes jugador 1: "))
    opcion2 = int(input("Que elijes jugador 2: "))
    print(resolucion(opcion1, opcion2))
    
######################## fin de procedimiento 3 ###############################        
def Procedimiento_4():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    if a>b :
        print(f"el valor mas grande es {a}")
    else:
        print(f"el valor mas grande es {b}")

######################## fin de procedimiento 4 ###############################        
def Procedimiento_5():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    c= int(input("ingrese el valor de C: "))
    
    if a>b and a>c:
        print(f"el valor mas grande es {a}")
    elif b>a and b>c:
        print(f"el valor mas grande es {b}")
    else:
        if c>a and c>b:
            print(f"el valor mas grande es {c}")
######################## fin de procedimiento 5 ###############################        
def Procedimiento_6():
    palabra=str(input("ingrese un caracter: "))
    if palabra == "a" or palabra == "e" or palabra == "i" or palabra == "o" or palabra == "u":
        print("el caracter ingresado es un caracter")
    else:
        print("el caracter ingresado no es un caracter")
######################## fin de procedimiento 6 ###############################        
def Procedimiento_7():
    i=int(1)
    while i <= 100:
        print(i)
        i=i+1
######################## fin de procedimiento 7 ###############################        
def Procedimiento_8():
    for x in range (100):
        print(x)
######################## fin de procedimiento 8 ###############################        
def Procedimiento_9():
    cad= input("ingrese una palabra: ")
    l=0
    for i in cad:
        l=l+1
    print(f"la palabra contiene {l} cantidad de letras")
######################## fin de procedimiento 9 ###############################        
def Procedimiento_10():
    texto= input("ingrese una palabra: ")
    for x in texto:
        print(x)
######################## fin de procedimiento 10 ###############################        
def Procedimiento_11():
    texto= input("ingrese una palabra: ")
    for x in texto:
        x=x.upper()
        print(f"Dame una {x}")
    print(texto.upper())
######################## fin de procedimiento 11 ###############################        
def Procedimiento_12():
    suma=0
    for x in [1, 2, 2]:
        suma= suma+x
    print(f"el valor de la suma de los datos da: {suma}")
######################## fin de procedimiento 12 ###############################        
def Procedimiento_13():
    producto=0
    for x in [2, 2, 2]:
        producto= producto*x
    print(f"el valor de la multiplicación de los datos da: {producto}")
######################## fin de procedimiento 13 ###############################        
def Procedimiento_14():
    n=int(input("ingrese el número: "))
    texto= " "
    c= "*"
    for i in range (n):
        texto = texto + c
    print(texto)
######################## fin de procedimiento 14 ###############################        
def Procedimiento_15():
    n=int(input("ingrese el número: "))
    c= input("ingrese un caracter: ")
    texto= " "
    for i in range (n):
        texto = texto + c
    print(texto)
######################## fin de procedimiento 15 ###############################        
def Procedimiento_16():
    for x in [2, 5, 5]:
        print(x * "*")
######################## fin de procedimiento 16 ###############################   
     
######################## fin de sector de procedimiento #####################

print("ingrese la opción que quiera realizar")

print("1- Programa de 2 jugadores que tiran un dado")
print("2- Programa de 2 jugadores que tiren 2 dados")
print("3- Programa que simula el piedra papel o tijeras")
print("4- Programa que toma 2 números y devuelve el mayor")
print("5- Programa que toma 3 números y devuelve el mayor")
print("6- Programa que determina si un caracter es una vocal")
print("7- Programa que muestra con bucle while el rango del 1 al 100")
print("8- Programa que muestra con bucle for el rango del 1 al 100")
print("9- Programa que cuente la cantidad de letras en una palabra")
print("10- Programa que muestra una palabra letra por letra")
print("11- Programa que te pida una palabra y que dame una, seguida de la letra")
print("12- Programa que sume todos los números de una lista de datos")
print("13- Programa que multiplique todos los números de una lista de datos ")
print("14- Programa que tome un numero y devuelva tantos * como el número")
print("15- Programa que tome un numero y un caracter y devuelva tantas veces el caracter como el número")
print("16- Programa que dibuje un histograma tomando los datos de una lista de números enteros")

op= int(input("ingrese la opción que quiera realizar: "))
print(" ")

if op == 1:
    print(Procedimiento_1())
    
elif op == 2 :
    print(Procedimiento_2())

elif op == 3 :
    print(Procedimiento_3())

elif op == 4 :
    print(Procedimiento_4())

elif op == 5 :
    print(Procedimiento_5())

elif op == 6 :
    print(Procedimiento_6())

elif op == 7 :
    print(Procedimiento_7())

elif op == 8 :
    print(Procedimiento_8())

elif op == 9 :
    print(Procedimiento_9())

elif op == 10 :
    print(Procedimiento_10())

elif op == 11 :
    print(Procedimiento_11())

elif op == 12 :
    print(Procedimiento_12())

elif op == 13 :
    print(Procedimiento_13())

elif op == 14 :
    print(Procedimiento_14())
    
elif op == 15 :
    print(Procedimiento_15())   
    
elif op == 16 :
    print(Procedimiento_16())    
    
else:
    print("la opción indicada no se encuentra disponible")