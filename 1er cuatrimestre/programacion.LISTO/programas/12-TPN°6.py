# -*- coding: utf-8 -*-
"""
alumno: Lautaro Santos Da Silveira
tema: Procesamiento de archivos
fecha: 23/06/2021
curso: Programación 1-IA
"""
##############################################################################
def lista1():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    antiguedad = float(0)
    presentismo = float(0)
    total = float(0)
    
    print("Listado de lo solicitado".center(99, " "))
    print("".center(99, "="))
    print("    Nombre".ljust(22," ")+"    Categoría".ljust(25," ")+"Basico".ljust(12," ")+"Antigüedad".ljust(15," ")+"Presentismo".ljust(15," ")+"Total".rjust(10," "))
    
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        antiguedad= float(fila[6]) * float(fila[5]) * 1.2 / 100
        presentismo= (float(fila[6]) + float(fila[5]))*8.35/100
        total= float(fila[6]) + antiguedad + presentismo
        print(fila[1].ljust(22," ")+fila[2].ljust(25," ")+fila[6].ljust(12," ")+format(antiguedad,'0.2f').ljust(15," ")+format(presentismo,'0.2f').ljust(15," ")+format(total,'0.2f').rjust(10," "))
##############################################################################
def lista2():
    cat= int(input("ingrese un valor de antigüedad: "))
    print(" ")
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    print("lista".center(59," "))
    print("".center(59,"="))
    print("Nombre".ljust(22," ") + "Categoría".ljust(25," ") + "Básico".rjust(12," "))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        if cat<int(fila[5]):
            print(fila[1].ljust(22," ") + fila[2].ljust(25," ") + format(fila[6]).rjust(12," ")) 
##############################################################################
def lista3():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    antiguedad = float(0)
    presentismo = float(0)
    total = float(0)
    
    print("Listado.csv".center(99, " "))
    print("".center(99, "="))
    print("    Nombre".ljust(22," ")+"    Categoría".ljust(25," ")+"Basico".ljust(12," ")+"Antigüedad".ljust(15," ")+"Presentismo".ljust(15," ")+"Total".rjust(10," "))
    Salida=open("Datos Salida.csv", "tw")
    Salida.write("Nombre;Categoría;Básico;Adicional por antigüedad;Presentismo;Total")
    Salida.write("\n")
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        antiguedad= float(fila[6]) * float(fila[5]) * 1.2 / 100
        presentismo= (float(fila[6]) + float(fila[5]))*8.35/100
        total= float(fila[6]) + antiguedad + presentismo
        Salida.write(fila[1])
        Salida.write(";")
        Salida.write(fila[2])
        Salida.write(";")
        Salida.write(fila[6])
        Salida.write(";")
        Salida.write(format(antiguedad, '0.2f').replace(".", ","))
        Salida.write(";")
        Salida.write(format(presentismo, '0.2f').replace(".", ","))
        Salida.write(";")
        Salida.write(format(total, '0.2f').replace(".", ","))
        Salida.write("\n")
    Salida.close()
##############################################################################
def lista4():
    cat= input("ingrese una categoría: ").capitalize()
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    salida=open("Datos Salida.csv", "tw")
    salida.write("Nombre;Categoría;Básico")
    salida.write("\n")
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        if cat == fila[2]:
            salida.write(fila[1])
            salida.write(";")
            salida.write(fila[2])
            salida.write(";")
            salida.write(fila[6])
            salida.write("\n")
    salida.close()
##############################################################################
def lista5():
    cat= int(input("ingrese un valor de antigüedad: "))
    print(" ")
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    salida=open("por antiguedad.csv", "tw")
    salida.write("Nombre;Categoría;Básico")
    salida.write("\n")
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        if cat<int(fila[5]):
             salida.write(fila[1])
             salida.write(";")
             salida.write(fila[2])
             salida.write(";")
             salida.write(fila[6])
             salida.write("\n")
    salida.close()
##############################################################################
def lista6():
    cat= int(input("ingrese el número de legajo: "))
    print(" ")
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    print("Usuario".center(99," "))
    print("".center(99,"="))
    print("    Nombre".ljust(22," ")+"    Categoría".ljust(25," ")+"Basico".ljust(12," ")+"Antigüedad".ljust(15," ")+"Presentismo".ljust(15," ")+"Total".rjust(10," "))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        antiguedad= float(fila[6]) * float(fila[5]) * 1.2 / 100
        presentismo= (float(fila[6]) + float(fila[5]))*8.35/100
        total= float(fila[6]) + antiguedad + presentismo
        if cat==int(fila[0]):
            print(fila[1].ljust(22," ")+fila[2].ljust(25," ")+fila[6].ljust(12," ")+format(antiguedad,'0.2f').ljust(15," ")+format(presentismo,'0.2f').ljust(15," ")+format(total,'0.2f').rjust(10," "))
##############################################################################
def lista7():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    basico= float(0)
    total = float(0)
    print("Total de Sueldo Básico".center(25," "))
    print("".center(27,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        basico= float(fila[6])
        total = total + basico 
    print(format(total, '0.2f').rjust(27," "))
##############################################################################
def lista8():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    basico= float(0)
    total = float(0)
    acumulado= int(0)
    print("Promedio de Sueldo Básico".center(27," "))
    print("".center(27,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        basico= float(fila[6])
        total = total + basico 
        acumulado= acumulado+1
        promedio= total/acumulado
    print(format(promedio, '0.2f').rjust(27," "))
##############################################################################
def lista9():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    
    print("Empleados con mayor sueldo".center(25, " "))
    print("".center(25,"="))
    nombre= " "
    Maximo= float(0)
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        if float(Maximo) < float(fila[6]) :
            Maximo=fila[6]
            nombre=fila[1]
    print(nombre)
##############################################################################
def lista10():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    antiguedad= float(0)
    suma = float(0)
    print("Total de Adicional por Antigüedad".center(36," "))
    print("".center(36,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        antiguedad = float(fila[6])*float(fila[5])*1.2/100
        suma= suma + antiguedad 
    print(format(suma, '0.2f').rjust(36," "))
##############################################################################
def lista11():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    antiguedad= float(0)
    total = float(0)
    acumulado= int(0)
    print("Promedio de Adicional por Antigüedad".center(36," "))
    print("".center(36,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        antiguedad = float(fila[6])*float(fila[5])*1.2/100
        total = total + antiguedad
        acumulado= acumulado+1
        promedio= total/acumulado
    print(format(promedio, '0.2f').rjust(36," "))
##############################################################################
def lista12():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    presentismo= float(0)
    suma = float(0)
    print("Total de Presentismo".center(25," "))
    print("".center(27,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        presentismo = (float(fila[6])+float(fila[5]))*8.35/100
        suma= suma + presentismo 
    print(format(suma, '0.2f').rjust(27," "))
##############################################################################
def lista13():
    Archivo = open("DatosPrograma.csv", "tr")
    Datos = Archivo.readlines()
    Archivo.close()
    presentismo= float(0)
    total = float(0)
    acumulado= int(0)
    print("Promedio de Adicional por Antigüedad".center(36," "))
    print("".center(36,"="))
    for x in Datos:
        x = x.replace("\n", " ")
        fila = x.split(";") 
        presentismo = (float(fila[6])+float(fila[5]))*8.35/100
        total = total + presentismo
        acumulado= acumulado+1
        promedio= total/acumulado
    print(format(promedio, '0.2f').rjust(36," "))
##############################################################################
print("BIENVENIDOS".center(50, " "))
print(" ".center(50,"="))
print("1-Lista de: Nombre, Categoria, Sueldo básico, Adicional por antigüedad, Presentismo y Total.")
print(" ")
print("2-listado de los empleados que tengan una antigüedad mayor a un valor ingresado por el usuario")
print(" ")
print("3-programa que genere un archivo CSV con: nombre, categoría, sueldo básico, adicional por antigüedad, presentismo y total.  ")
print(" ")
print("4-programa que genere un archivo CSV de los empleados que correspondan a una categoría en particular, indicada por el usuario, y se grabará: Nombre, Categoría y sueldo básico.")
print(" ")
print("5-programa que genere un archivo CSV de los empleados que tengan una antigüedad mayor a un valor ingresado por el usuario, y se grabará: Nombre, Categoría y sueldo básico.")
print(" ")
print("6-programa que muestre nombre, categoría, sueldo básico, adicional por antigüedad, presentismo y total cuando el usuario ingrese un número de legajo.")
print(" ")
print("7-programa que muestre la suma total de los sueldos básicos.")
print(" ")
print("8-programa que muestre el promedio de los sueldos básicos.")
print(" ")
print("9-programa que muestre el nombre de los empleados que tienen el mayor sueldo básico.")
print(" ")
print("10-programa que muestre la suma total a pagar por adicionales por antigüedad.")
print(" ")
print("11-programa que muestre el promedio de los adicionales por antigüedad.")
print(" ")
print("12-programa que muestre la suma total a pagar por presentismo.")
print(" ")
print("13-programa que muestre el promedio de los presentismo.")
print(" ")

op= int(input("¿Qué actividad desea realizar?: "))

if op==1:
    print(" ")
    print(lista1())
elif op==2:
    print(" ")
    print(lista2())
elif op==3:
    print(" ")
    print(lista3())
elif op==4:
    print(" ")
    print(lista4())
elif op==5:
    print(" ")
    print(lista5())
elif op==6:
    print(" ")
    print(lista6())
elif op==7:
    print(" ")
    print(lista7())
elif op==8:
    print(" ")
    print(lista8())
elif op==9:
    print(" ")
    print(lista9())
elif op==10:
    print(" ")
    print(lista10())
elif op==11:
    print(" ")
    print(lista11())
elif op==12:
    print(" ")
    print(lista12())
elif op==13:
    print(" ")
    print(lista13())
else:
    print(" ")
    print("opción no valida")




















