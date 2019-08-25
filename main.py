#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

def Select(Select_example):

    Select = re.findall(r"SELECT (.+) FROM ([a-zA-Z]*)",Select_example)

    Table = re.findall(r"(\w+|\*)",Select[0][0])

    Inner = re.findall(r"INNER JOIN (\w*)",Select_example)

    Order = re.findall(r"ORDER BY (\w*) (ASC|DESC)",Select_example)

    Where = re.findall(r"(AND|OR)?\s?([a-zA-Z.]*)\s?=\s?\’?([a-zA-Z0-9-\s.]*)\’?",Select_example)#problema aca, no encuentra numeros

    print("Se seleccionara: ",Table)
    print("De la tabla: ",Select[0][1])
    print("La lista where: ",Where)
    #print("Ordenado por ",Order[0][0]," By ",Order[0][1])

#---------------------------------------------------------------

def Insert(Insert_example):

    Insert = re.findall(r"INSERT INTO (\w*) \((.*)\) VALUES \((.*)\)",Insert_example)

    Tablas_a_insertar = re.findall(r"\,? (\w*) \,?",Insert[0][1])

    Valores_a_insertar = re.findall(r"(\d+)|\’(.*?)\’",Insert[0][2])#Problema aca, no encuentra las cosas bien, falla en los numeros

    print("La tabla a insertar: ",Insert[0][0])
    print("Los valores a insertar: ",Tablas_a_insertar)
    print("Valores: ",Valores_a_insertar)
#-------------------------------------------------------------------

def Update(Update_example):

    Update = re.findall(r"UPDATE (\w*) SET (.*) WHERE (.*);",Update_example)

    Update_set = re.findall(r"(\w*) =\s?\’?([a-zA-Z\s0-9]*)\’?",Update[0][1])

    Update_where = re.findall(r"(AND|OR)?\s?(\w*)\s?=\s?\’?([a-zA-Z0-9-]*)\’?",Update[0][2]) #Mismo error, los numeros

    print("La tabla a actualizar: ",Update[0][0])
    print("Set: ", Update_set)
    print("Where: ", Update_where,")")
#--------------------------------------------------------------------------------------

Example = str(input("Ingresa un query:"))
print(Example)
Estado = 1

if(Example.split()[0]=="SELECT"):
    Select(Example)
elif(Example.split()[0]=="INSERT"):
    Insert(Example)
elif(Example.split()[0]=="UPDATE"):
    Update(Example)
else:
    print("ERROR")
    