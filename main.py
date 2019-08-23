#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

example = "INSERT INTO Estudiantes ( Nombre , Rut , Rol , Telefono , Edad ) VALUES ( ’ Sebastian Godinez ’ , ’19991933 -8 ’ , ’201673501 -1 ’ ,988881234 ,21) ;"

Select_table = re.findall(r"SELECT (.+|\*) FROM ([a-zA-Z]*)",example)

Inner = re.findall(r"INNER JOIN (\w*)",example)

Order = re.findall(r"ORDER BY (\w*) (ASC|DESC)",example)

Where = re.findall(r"WHERE (\w*)=(\w*) AND|OR (\w*)=(\w*)",example)#Falta que detecte los AND y FOR

#---------------------------------------------------------------

Insert = re.findall(r"INSERT INTO (\w*) \((.*)\) VALUES \((.*)\) ;",example)

#-------------------------------------------------------------------

Update = re.findall(r"UPDATE (\w*) SET (.*) WHERE (\w*)=(\w*) ;",example)#Falta que detecte los AND y FOR

print(Insert[0][2])