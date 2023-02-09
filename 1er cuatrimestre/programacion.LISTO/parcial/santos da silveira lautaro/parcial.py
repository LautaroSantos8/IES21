# -*- coding: utf-8 -*-
"""
Alumno: Lautaro Santos Da Silveira 
Materia: Programacion 1
Tema: Instancia Evaluativa 1
"""
######################## inicio de sector de procedimientos ##################        
def caracer(cad, caracter):
    respuesta=int(0)
    for x in cad:
        if x == caracter:
            respuesta= respuesta+1
    return respuesta
    
######################## fin de función caracter ##############################
def ContarCaracter():
    cad= input("ingrese una cadena de texto: ")
    caracter= input("ingrese un caracter: ")
    print(caracer(cad, caracter))
######################## fin de procedimiento ContarCaracter #################       

def suma(x):
    suma=0
    for i in range(1,x+1):
        suma=suma+i
    return suma
######################## fin de función suma ##################################
def CalcularSumatoria():
    x=int(input("ingrese un numero entero del 1 al 10: "))
    print(suma(x))
######################## fin de procedimiento CalcularSumatoria ##############

def precios(edad):
    if edad < 4:
        res= "el valor de la entrada es $25"
        return res
    elif edad>4 and edad<18:
        res="el valor de la entrada es $75"
        return res
    else:
        res="el valor de la entrada es $100"
        return res
######################## fin de función precios ###############################
def ConsultarPrecio():
    edad= int(input("ingrese su edad: "))
    print(precios(edad))
######################## fin de procedimiento ConsultarPrecio #################  

def calificacion(nota):
    if nota == 1 or nota == 2 or nota == 3:
        res="No Satisfactorio"
        return res
    elif nota == 4:
        res="Suficiente"
        return res
    elif nota == 5 or nota == 6:
        res="Satisfactorio"
        return res
    elif nota == 7:
        res="Bueno"
        return res
    elif nota == 8 or nota == 9:
        res="Muy Bueno"
        return res
    elif nota == 10:
        res="Excelente"
        return res
    else: 
        res="Valor No Valido"
        return res
######################## fin de función calificacion #########################
def CalificarAlumno():
    nota= int(input("Ingrese el valor de la nota como número entero y considerando del 1 al 10: "))
    print(calificacion(nota))
######################## fin de procedimiento CalificarAlumno #################  

######################## fin de sector de procedimiento #######################

print("En este programa puedes hacer las siguientes operaciones: ")
print("1 – Conocer cuántos caracteres de un tipo tiene un texto.")
print("2 - Conocer la sumatoria de 0 hasta un número ingresado por el usuario.")
print("3 - Conocer el precio de una entrada.")
print("4 - Conocer cuál es la calificación cualitativa de un alumno.")

op= int(input("Ingresa el número que corresponde a tu elección: "))

if op==1:
    print(ContarCaracter())
elif op == 2:
    print(CalcularSumatoria())
elif op == 2:
    print(ConsultarPrecio())
elif op == 2:
    print(CalificarAlumno())
else:
    print("Esa opción no está disponible")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    