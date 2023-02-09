# -*- coding: utf-8 -*-
"""
alumno: Lautaro Santos Da Silveira
tema: IEFI
fecha: 28/06/2021
curso: Programación 1-IA
"""
##############################################################################
def MostrarSueldos():
    archivo=open("IEFI.csv", "tr")
    datos=archivo.readlines()
    archivo.close()
    primer=float(0)
    segundo=float(0)
    print("lista de datos".center(60, " "))
    print("".center(60, "="))
    print("apellido".ljust(12, " ")+"Nombre".ljust(12, " ")+ "Basico".ljust(12, " ")+"1° aumento".ljust(12, " ")+ "2° aumento".ljust(12," "))
    for x in datos:
        x = x.replace("\n", " ")
        fila = x.split(";")
        primer= float(fila[5])*12/100
        segundo= primer + primer*14/100
        print(fila[1].ljust(12, " ")+fila[2].ljust(12, " ")+fila[5].ljust(12, " ")+format(primer, '0.2f').ljust(12, " ")+format(segundo, '0.2f').ljust(12, " "))
##############################################################################
def CalcularPromedio():
    archivo=open("IEFI.csv", "tr")
    datos=archivo.readlines()
    archivo.close()
    basico=float(0)
    total=float(0)
    acumulado= float(0)
    for x in datos:
        x = x.replace("\n", " ")
        fila = x.split(";")
        basico = float(fila[5])
        total = total+basico
        acumulado = acumulado + 1 
        promedio = total / acumulado
        return promedio
##############################################################################
def ExportarSueldos():
    archivo=open("IEFI.csv", "tr")
    datos=archivo.readlines()
    archivo.close()
    antiguedad=float(0)
    total=float(0)
    nuevo=open("DatosExportados.CSV", "tw")
    nuevo.write("Apellido y nombre;Sueldo Basico;Adicional por atigüedad;Total a  cobrar")
    nuevo.write("\n")
    for x in datos:
        x = x.replace("\n", " ")
        fila = x.split(";")
        antiguedad= float(fila[5])*float(fila[4])*1.5/100
        total = float(fila[5])+float(antiguedad)
        nuevo.write(fila[1]+","+ fila[2])
        nuevo.write(";")
        nuevo.write(fila[5])
        nuevo.write(";")
        nuevo.write(format(antiguedad, '0.2f').replace(".", ","))
        nuevo.write(";")
        nuevo.write(format(total, '0.2f').replace(".", ","))
        nuevo.write("\n")
    nuevo.close()
    print("exportados correctamente")
##############################################################################
def ConsultarUnAumentoDeSueldo():
    cat=int(input("ingrese el número de legajo del empleado: "))
    print(" ")
    archivo=open("IEFI.csv", "tr")
    datos=archivo.readlines()
    archivo.close()
    aumento=float(0)
    print("Apellido y Nombre".ljust(24, " ")+ "Basico".ljust(12, " ")+"sueldo con aumento".ljust(12, " "))
    print("".center(54, "="))

    for x in datos:
        x = x.replace("\n", " ")
        fila = x.split(";")
        nom= fila[1]+", "+fila[2]
        aumento= float(fila[5])+float(fila[5])*12/100
        if cat == int(fila[0]):
            rta= nom.ljust(24, " ") + fila[5].ljust(12, " ") + format(aumento, '0.2f')
        return rta
##############################################################################
print("En este programa puedes hacer las siguientes operaciones: ")
print("1 – Listar los sueldos. ")
print("2 – Exportar los sueldos.")
print("3 – Calcular el promedio de los sueldos básicos.")
print("4 – Consultar el aumento de sueldo de un empleado.")

op=int(input("Ingresa el número que corresponde a tu elección: "))
print(" ")
if op==1:
    print(MostrarSueldos())
elif op==2:
    print(f"El promedio de los sueldos basicos es: {CalcularPromedio()}")
elif op==3:
    print(ExportarSueldos())
elif op==4:
    print(f"{ConsultarUnAumentoDeSueldo()}")
else:
    print("Esa opción no está disponible")




















