# -*- coding: utf-8 -*-
"""
Autor: Lautaro Santos Da Silveira
Fecha: 6/06/21
Tema: Generar Archivos
El archivo generado tiene como funcionalidad generar una lista de compras.
"""


def CrearArchivo():
    Archiv=open("prueba.txt", "tw")
    Archiv.write("Lista de compras: ")
    Archiv.close()

def CompletarArchivo():
    palabra= input("ingrese los datos que desee enlistar: ")
    archivo = open("prueba.txt", "ta")
    archivo.write("\n")
    archivo.write(palabra)
    archivo.close()
    
def Leer():
    archivo=open("prueba.txt", "tr")
    dato=archivo.read()
    archivo.close()
    print(dato)

print("Este programa lo ayudará a que genere su lista de compras en el supermercado")
print("¿Desea agregar un articulo a la lista, empezar la lista de nuevo o leer lo ya anotado?")
print("1- eliminar toda la lista y empezarla de nuevo")
print("2- agregar un articulo a la lista existente")

res=int(input("ingrese lo que desea realizar: "))

if res==1:
    print(CrearArchivo())
elif res==2:
    print(CompletarArchivo()) 
else:
    print("respuesta no valida")

print(Leer())

