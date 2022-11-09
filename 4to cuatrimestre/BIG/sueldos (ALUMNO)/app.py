from neo4j import GraphDatabase 
import json

def CargarDatos():
    grafodb = GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','test'))
    sesion= grafodb.session()
    with open('data/empleados.json') as archivo:
        filas = json.load(archivo)
        for fila in filas:
            q1= "CREATE (:Empleado { "+ f"dni: {fila['dni']}, nombre: '{fila['nombre']}', sueldo: {fila['sueldo']}" + "})"
            sesion.run(q1)
    with open('data/sectores.json') as archivo:
        filas = json.load(archivo)
        for fila in filas:
            q1= "CREATE (:Sectores { "+ f"nro: {fila['nro']}, nombre: '{fila['nombre']}'" + "})"
            sesion.run(q1)
############################ Relaciones ############################
    q1= "MATCH(e:Empleado) WHERE e.dni IN [101, 102]\
         MATCH(s:Sectores) WHERE s.nro = 1\
         CREATE (e)-[r:TRABAJA_EN]->(s)"
    sesion.run(q1)
    q1= "MATCH(e:Empleado) WHERE e.dni IN [103, 104]\
         MATCH(s:Sectores) WHERE s.nro = 2\
         CREATE (e)-[r:TRABAJA_EN]->(s)"
    sesion.run(q1)

    print('IMPORTE TOTAL DE SUELDOS EN SUCURSALES:')
    print('---------------------------------------')
    for x in [1,2]:
        q1 = f'MATCH(e:Empleado)-[r:TRABAJA_EN]->(s:Sectores) WHERE s.nro = {x}  RETURN SUM(e.sueldo) AS Total'
        nodos=sesion.run(q1)
        for nodo in nodos:
            total=nodo['Total']
            print(f'sucursal {x}: ${total}')
            print('-----------------------')
CargarDatos()