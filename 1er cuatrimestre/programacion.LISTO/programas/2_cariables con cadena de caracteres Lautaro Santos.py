# -*- coding: utf-8 -*-
"""
Udusrio: Lautaro Santos Da Silveira
Tema: programa con datos tipo cadena de caracteres
fecha: 21/4/21

"""

a= input("pon tu nombre: ")

b= input("pon tu apellido: ")

NomCompleto= (a.strip()+" "+b.strip()).upper()

print(NomCompleto.replace("C", "Z"))