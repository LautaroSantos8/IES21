# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:28:51 2021

@author: Usuario
"""
######################## inicio de sector de procedimientos ##################        
def suma():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    r=0
    r= a+b
    return r
######################## fin de procedimiento suma ############################        
def resta():
    
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    if a>b:
        r = 0
        r= a-b
        return r
    else:
        if a<b:
            r = 0
            r= b-a
        return r
######################## fin de procedimiento resta ############################        
def producto():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    r=0
    r= a*b
    return r
######################## fin de procedimiento producto ########################      
def maximo():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    if a>b :
        r=a
        return r 
    else:
        r=b
        return r
######################## fin de procedimiento máximo #########################      
def minimo():
    
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    if a<b :
        return a 
    else:
        return b
######################## fin de procedimiento mínimo ##########################      
def max_de_tres():
    a= int(input("ingrese el valor de A: "))

    b= int(input("ingrese el valor de B: "))
    
    c= int(input("ingrese el valor de C: "))
    
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        if c>a and c>b:
            return c
######################## fin de procedimiento mas grande de 3 ################     
def vocal():
    c= str(input("ingrese el caracter: "))
    
    a= str("true")
    
    b=str("false")
    
    if c==str("a" or "e" or "i" or "o" or "u"):
        return a
    
    else:
        if c!=str("a" or "e" or "i" or "o" or "u"):
            return b 
######################## fin de procedimiento vocal ##########################      
def inversa():
    a= input("ingresa una palabra: ")
    CadNueva= str(" ")
    res= str(" ") 
    for x in a:
        CadNueva= x+CadNueva
    res= CadNueva
    return res
######################## fin de procedimiento inversa ########################      
def es_palindromo():
    palabra=input("ingrese la palabra: ").upper().replace(" ", "")
    inver= ""
    x=len(palabra)
    while x>0:
        x=x-1
        inver=inver+palabra[x]
    
    if palabra == inver:
        respuesta="true"
        return respuesta
    else:
        respuesta="false"
        return respuesta
######################## fin de procedimiento palindromo ######################      
def LongCadena():
    
    cad= input("ingrese un texto: ")
    l=0
    for x in cad:
        l=l+1
    return l 
######################## fin de procedimiento LongCadena ######################      
def superposicion():
    a= [1, 3, 5]
    b= [1, 7, 6]
    for i in range(len(a)):
        for j in range (len (b)):
            if a[i] == b [j]:
                res= "true"
                return res
            else:
                res= "false"
                return res
######################## fin de procedimiento superpocisión ##################      
def generar_n_caracteres():
    n= int(input("ingrese el valor deseado: "))
    c= input("ingrese el caracter que desea repetir: ")
    
    texto=""
    for x in range (n):
        texto= texto + c
    return texto
######################## fin de procedimiento generar caracteres #############

######################## fin de sector de procedimiento #####################
print("¿que programa decea ejecutar?")
print("1: suma")
print("2: restar")
print("3: multiplicar")
print("4: encontrar el mas grande")
print("5: encontrar el mas chico")
print("6: encontrar el mas grande entre 3 valores")
print("7: determinar si el caracter ingresado es una vocal")
print("8: devolver un conjunto de palabras pero dadas vueltas")
print("9: identificar palíndromos")
print("10: calcular la longitud de un texto")
print("11: ingresar cadena de textos y ver si hay miembros en común")
print("12: ingresar un valor numerico y devuelva la misma cantidad de letras ")

opcion= int(input("escriba la operacion que desea realizar: "))

if opcion==1:
    print(f"la suma es: {suma()}")
    
elif opcion==2:
    print(f"la resta es: {resta()}")
    
elif opcion==3:
    print(f"la multiplicación es: {producto()}")
    
elif opcion==4:
    print(f"el numero mas grande de los dos es: {maximo()}")
    
elif opcion==5:
    print(f"el numero mas pequeño de los dos es: {minimo()}")
    
elif opcion==6:
    print(f"el numero mas grande de los tres números es: {max_de_tres()}")
    
elif opcion==7:
    print(f"{vocal()}")
    
elif opcion==8:
    print(f"{inversa()}")
    
elif opcion==9:
    print(f"{es_palindromo()}")
    
elif opcion==10:
    print(f"La longitud de ese texto es: {LongCadena()}")
    
elif opcion==11:
    print(f"{superposicion()}")
    
elif opcion==12:
    print(f"{generar_n_caracteres()}")
    
else:  
    print("datos ingresados incorrectamente")
