# -*- coding: utf-8 -*-
"""
Alumno: Lautaro Santos Da Silveira
Tema: TPN°1
fecha: 7/7/21
"""
###############################################################################   
def Procedimiento_1():
    p= float(input("ingrese el precio del producto: "))
    iva= 21*p/100
    pt= p+iva
    print(f"IVA: {iva}")
    print(f"Precio final del producto: {pt}")
###############################################################################   
def Procedimiento_2():
    a= int(input("Ingrese el valor del 1er número: "))
    b= int(input("Ingrese el valor del 2do número: "))
    if a<b:
        print("el valor del 2do número es mayor")
    else:
        print("el valor del 1er número es mayor ")
###############################################################################   
def Procedimiento_3():
    a= int(input("Ingrese el valor del 1er número: "))
    b= int(input("Ingrese el valor del 2do número: "))
    if a<b:
        print("el valor del 1er número es menor")
    else:
        print("el valor del 2do número es menor ")
###############################################################################   
def Procedimiento_4():
    a= int(input("Ingrese el valor del número: "))
    if a>=0 and a<=10:
        print("el valor ingresado está entre 0 y 10")
    else:
        print("el valor ingresado no está entre 0 y 10")    
###############################################################################   
def Procedimiento_5():
    a= int(input("Ingrese el valor del número: "))
    if a>=0 and a<=10:
        print("el valor ingresado está entre 0 y 10")
    elif a>=11 and a<=20:
        print("el valor ingresado está entre 11 y 20")    
    elif a>=21 and a<=30:
        print("el valor ingresado está entre 21 y 30")
    else:
        print("el valor ingresado es superior a 30")   
###############################################################################   
def Procedimiento_6():
    valor= float(input("Ingrese el valor de la compra que realizó: "))    
    forma= input("¿De que forma abonará?: ").lower()    
    if forma == str("contado"):
        imp= valor
        print(f"Su monto a pagar será de: {imp}")    
    elif forma == str("tarjeta de credito"):
        imp1= valor*1.02
        print(f"Su monto a pagar será de: {imp1}")    
    elif forma == str("cheque"):
        imp2= valor*1.03
        print(f"Su monto a pagar será de: {imp2}")        
    else :
        if forma == str("cuenta corriente"):
           imp3= valor*1.015
           print(f"Su monto a pagar será de: {imp3}")
###############################################################################   
def Procedimiento_7():
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    tr= a+b+c
    if tr==180:
        print("Las medidas ingresadas corresponden a un triángulo")
    else:
        print("las medidas ingresadas no corresponden a un triángulo")    
###############################################################################      
def Procedimiento_8():
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    tr= a+b+c
    if tr==180 and a>90 or b>90 or c>90: 
        print("Las medidas ingresadas corresponden a un obtusangulo")
    else:
        print("las medidas ingresadas no corresponden a un obtusangulo")    
###############################################################################         
def Procedimiento_9():    
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    tr= a+b+c
    if tr==180 and a==90 or b==90 or c==90:
        print("Las medidas ingresadas corresponden a un triángulo rectangulo")
    else:
        print("las medidas ingresadas no corresponden a un triángulo rectangulo")
###############################################################################      
def Procedimiento_10():
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    tr= a+b+c
    if tr==180 and a<90 and b<90 and c<90:
        print("Las medidas ingresadas corresponden a un triángulo acutángulo")
    else:
        print("las medidas ingresadas no corresponden a un triángulo acutángulo")
###############################################################################      
def Procedimiento_11():
    a= float(input("ingrese el valor del angulo A: "))
    b= float(input("ingrese el valor del angulo B: "))
    c= float(input("ingrese el valor del angulo C: "))
    tr= a+b+c    
    if tr==180 and a<90 and b<90 and c<90:
        print("Las medidas ingresadas corresponden a un triángulo acutángulo")
    elif tr==180 and a==90 or b==90 or c==90:
        print("las medidas ingresadas corresponden a un triángulo rectángulo")    
    elif tr==180 and a>90 or b>90 or c>90:
        print("las medidas ingresadas corresponden a un triángulo obtusángulo")
    else:
        print("las medidas ingresadas no corresponden a un triángulo")
###############################################################################      
def Procedimiento_12():
    a= float(input("ingrese el valor del lado A: "))
    b= float(input("ingrese el valor del lado B: "))
    c= float(input("ingrese el valor del lado C: "))
    if a+b<c or b+c<a or c+a<b :
        print("Las medidas ingresadas no corresponden a un Triángulo ")
    else: 
        if a==b and b==c and c==a: 
            print("Las medidas ingresadas corresponden a un Triángulo Equilátero")    
        elif a==b and b!=c or b==c and c!=a or c==a and a!=b:
            print("Las medidas ingresadas corresponden a un Triángulo Isósceles")
        else: 
            if a!=b and b!=c or b!=c and c!=a or c!=a and a!=b:
                print("Las medidas ingresadas corresponden a un Triángulo Escaleno")
###############################################################################      
def Procedimiento_13():
    a= float(input("Ingrese su peso: "))
    b= float(input("Ingrese su altura: "))
    IMC= a/b**2
    print(f"su IMC es = {IMC}")
    if IMC<20:
        print("Tiene el peso muy bajo, está delgado")
    elif IMC < 30:
        print("Tu peso es el adecuado")
    elif IMC < 40:
        print("Estás con un ligero sobrepeso")
    elif IMC < 50:
        print("Usted tiene sobrepeso")
    else: 
        print("Tienes obesidad")
###############################################################################      
def Procedimiento_14():
    a= int(input("Ingrese el 1er número entero: "))
    b= int(input("Ingrese el 2do número entero: "))
    if a>b:
        multiplo= a%b
        if multiplo == 0:
            print ("El valor de A es el mayor y es multiplo de B")
        else:
            if multiplo != 0:
                print("El valor de A es el mayor pero no es multiplo de B")
    else:
        if a<b:
            multiplo= b%a
            if multiplo == 0:
                print ("El valor de B es el mayor y es multiplo de A")
            else:
                if multiplo != 0:
                    print("El valor de B es el mayor pero no es multiplo de A")
###############################################################################      
def Procedimiento_15():
    from random import randint
    a= int(randint(1,10))
    b= int(randint(1,10))
    print(f"los numeros generados son {a} y {b}")
    c= int(randint(1,4))
    if c==1:
        print("oprtacion a realizar: suma (+)")
        correcto= a+b
    elif c==2:
        print("oprtacion a realizar: resta (-)")
        correcto= a-b
    elif c==3:
        print("oprtacion a realizar: multiplicación (*)")
        correcto= a*b
    else: 
        print("oprtacion a realizar: división (/)")
        correcto= a/b
    resultado = float(input("ingrese el resultado de la operación solicitada: ")) 
    if resultado == correcto:
        print("Felicitaciones, el resultado es el correcto")  
    else:
        print(f"La respuesta ingresada está mal, el correcto es {correcto}")
###############################################################################        
print("Ingrese la opción que quiera realizar")
print(" ")
print("1- Programa que el usuario ingrese el precio de un producto y se informe su IVA y su precio final.")
print(" ")
print("2- Programa que el usuario ingrese dos números y el programa deberá indicar cual es el mayor.")
print(" ")
print("3- Programa que el usuario ingrese dos números y el programa deberá indicar cual es el menor.")
print(" ")
print("4- Programa que el usuario ingrese un número entero y el programa debe informar si está entre 0 y 10.")
print(" ")
print("5- Programa que el usuario ingrese un número entero y el programa debe informar si está entre 0 y 10, esta entre 11 y 20, si esta entre 21 y 30, o si es mayor a 30.")
print(" ")
print("6- Programa que el usuario ingrese el importe de una compra e informar la forma de pago.")
print(" ")
print("7- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un triangulo.")
print(" ")
print("8- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un obtusángulo.")
print(" ")
print("9- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un rectángulo.")
print(" ")
print("10- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un acutángulo.")
print(" ")
print("11- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un triangulo y también que tipo de triangulo es segun sus angulos.")
print(" ")
print("12- Programa que el usuario ingrese tres medidas de los angulos de un triangulo y este debe determinar si es un triangulo y también que tipo de triangulo es segun sus lados.")
print(" ")
print("13- Programa que calcule el indice de masa corporal.")
print(" ")
print("14- programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor")
print(" ")
print("15- Programa que genere dos numeros aleatorios y realizar una operacion matematica con ellos, siendo 1:+; 2:-; 3:*; 4:/")
print(" ")
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
else:
    print("la opción indicada no se encuentra disponible")








