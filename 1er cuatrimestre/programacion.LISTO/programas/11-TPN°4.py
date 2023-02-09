# -*- coding: utf-8 -*-
"""
alumno: Lautaro Santos Da Silveira
tema: Procesamiento de archivos
fecha: 21/06/2021
curso: Programación 1-IA
"""
##############################################################################
def ListaMozos():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    total = float(0)
    print("listado de comisiones".center(35, " "))
    print(" ".center(36, "-"))
    print("Nombre".ljust(20, " ") + "Categoria".ljust(8, " ") + "importe".rjust(10, " "))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe = float(fila[3]) * float(fila[4]) / 100
        total = total+importe
        print(fila[1].ljust(20, " ") + fila[2].ljust(8, " ") + format(importe, '0.2f').rjust(10, " "))
    print(" ".center(36, "-"))
    print(format(total, '0.2f').rjust(36, " "))
##############################################################################
def ListaMozos2():
    cat=input()
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    total = float(0)
    
    print("listado de comisiones".center(35, " "))
    print(" ".center(36, "-"))
    print("Nombre".ljust(20, " ") + "Categoria".ljust(8, " ") + "importe".rjust(10, " "))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        if (fila[2])==cat:
            importe = float(fila[3]) * float(fila[4]) / 100
            total = total+importe
            print(fila[1].ljust(20, " ") + fila[2].ljust(8, " ") + format(importe, '0.2f').rjust(10, " "))
    print(" ".center(36, "-"))
    print(format(total, '0.2f').rjust(36, " "))
##############################################################################
def ListaMozos3():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    
    ArchivoSalida= open("Salida.csv", "tw")
    ArchivoSalida.write("Nombre;Catgoria;Importe")
    ArchivoSalida.write("\n")
    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe = float(fila[3]) * float(fila[4]) / 100
        ArchivoSalida.write(fila[1])
        ArchivoSalida.write(";")
        ArchivoSalida.write(fila[2])
        ArchivoSalida.write(";")
        ArchivoSalida.write(format(importe, '0.2f').rjust(10, " ").replace(".", ","))
        ArchivoSalida.write("\n")
    ArchivoSalida.close()
    print("datos exportados correctamente")
##############################################################################
def ListaMozos4():
    cat = input()
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)

    ArchSalida=open("prueba.csv", "tw")
    ArchSalida.write("Nombre;Catgoria;Importe")
    ArchSalida.write("\n")
    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        if (fila[2])==cat:
            importe = float(fila[3]) * float(fila[4]) / 100
            ArchSalida.write(fila[1])
            ArchSalida.write(";")
            ArchSalida.write(fila[2])
            ArchSalida.write(";")         
            ArchSalida.write(format(importe, '0.2f').rjust(10, " ").replace(".", ","))
            ArchSalida.write("\n")
    ArchSalida.close()
    print("datos exportados correctamente")
##############################################################################
def ListaMozos5():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    total = float(0)
    print("Total de ventas realizadas".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe =float(fila[4])
        total = total+importe
    print(format(total, '0.2f').ljust(36, " "))
##############################################################################
def ListaMozos6():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    valor=float(0)
    total = float(0)
    print("Promedio de ventas realizadas".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe =float(fila[4])
        total = total+importe
        valor = valor + 1
    promedio = total/valor
    print(format(promedio, '0.2f').ljust(36, " "))
##############################################################################
def ListaMozos7():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    Mayor= float(0)
    nombre=" "
    print("Mozo que logró la mayor venta".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        if float(Mayor)<float(fila[4]):
            Mayor = fila[4]
            nombre= str(fila[1])
    print(nombre)
##############################################################################
def ListaMozos8():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    total = float(0)
    print("Total a pagar por comisiones".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe = float(fila[3]) * float(fila[4]) / 100
        total = total+importe
    print(format(total, '0.2f').ljust(36, " "))

##############################################################################  
def ListaMozos9():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe = float(0)
    valor=float(0)
    total = float(0)
    print("Promedio de ventas realizadas".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe = float(fila[3]) * float(fila[4]) / 100
        total = total+importe
        valor = valor + 1
    promedio = total/valor
    print(format(promedio, '0.2f').ljust(36, " "))
##############################################################################
def ListaMozos10():
    archivo = open("Mozos.csv","tr" )
    dato = archivo.readlines()
    archivo.close()
    importe=float(0)
    Mayor= float(0)
    nombre=" "
    print("Mozo que logró la mayor venta".center(35, " "))
    print(" ".center(36, "="))

    for x in dato:
        x = x.replace("\n" , "")
        fila = x.split(";")
        importe = float(fila[3]) * float(fila[4]) / 100
        if float(Mayor)<importe:
            Mayor = fila[4]
            nombre= str(fila[1])
    print(nombre)
##############################################################################
print("BIENVENIDOS")
print("-----------")
print("1-Listado de todos los mozos con el nombre del mozo, categoría, importe a cobrar por la comisión de la venta.")
print(" ")
print("2-listado de los mozos que correspondan a una categoría en particular, indicada por el usuario")
print(" ")
print("3-programa que genere un archivo con extensión CSV de todos los mozos con: nombre del mozo, categoría, importe a cobrar por la comisión de la venta. ")
print(" ")
print("4-programa que genere un archivo con extensión CSV de los mozos que correspondan a una categoría en particular, indicada por el usuario.")
print(" ")
print("5-programa que muestre el total de las ventas.")
print(" ")
print("6-programa que muestre el promedio de las ventas.")
print(" ")
print("7-programa que muestre el nombre del mozo que logró la mayor venta.")
print(" ")
print("8-programa que muestre el total a pagar por comisiones de ventas.")
print(" ")
print("9-programa que muestre el promedio a pagar por comisiones de ventas.")
print(" ")
print("10-programa que muestre el mayor importe a pagar por comisiones de ventas.")
print(" ")
op= int(input("¿Qué actividad desea realizar?: "))

if op==1:
    print(" ")
    print(ListaMozos())
elif op==2:
    print(" ")
    print(ListaMozos2())
elif op==3:
    print(" ")
    print(ListaMozos3())    
elif op==4:
    print(" ")
    print(ListaMozos4())
elif op==5:
    print(" ")
    print(ListaMozos5())
elif op==6:
    print(" ")
    print(ListaMozos6())
elif op==7:
    print(" ")
    print(ListaMozos7())
elif op==8:
    print(" ")
    print(ListaMozos8())
elif op==9:
    print(" ")
    print(ListaMozos9())
elif op==10:
    print(" ")
    print(ListaMozos10())
else:
    print(" ")
    print("opción no valida")