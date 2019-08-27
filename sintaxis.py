import re

def insertSintaxis(example):
    aux =re.fullmatch(r"INSERT INTO (\w+) \(\s?([a-zA-Z0-9]+\s?|\s?\,\s?[A-Za-z0-9]+\s?)+\) VALUES \((\s?\'[a-zA-Z0-9]+\'\s?|\s?\,\s?\'[a-zA-Z0-9]+\'\s?|\s?\,[0-9]+\s?|\s?[0-9]+\s?)+\)\s?;",example)
    if(aux!=None):
        return True
    return False

def selectSintaxis(example):
    aux = re.fullmatch(r"SELECT (\*|\w+|\,\w+|\w+\,\w+)+ FROM (\w+)\s?(INNER JOIN \w+)?\s?(ORDER BY \w+ (ASC|DESC))?\s?(WHERE ([a-zA-Z0-9]+)\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9]+)(\s?(AND|OR) ([a-zA-Z0-9]+)\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9]+)\s?)*)?\s?;",example)
    if(aux!=None):
        return True
    return False

def updateSintaxis(example):
    aux = re.fullmatch(r"UPDATE (\w+) SET (\w+\s?=\s?\'[a-zA-Z0-9\s]+\'\s?|\,\w+\s?=\s?\'[a-zA-Z0-9\s]+\'\s?|\s?\w+\s?=\s?[0-9]+\s?|\s?\,\w+\s?=\s?[0-9]+\s?)+ WHERE ([a-zA-Z0-9]+)\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9]+)(\s?(AND|OR) [a-zA-Z0-9]+\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9])+)*\s?;",example) #Agregar los and y or
    if(aux!=None):
        return True
    return False

example_select = "SELECT tabla FROM tabla INNER JOIN jeje ORDER BY d ASC WHERE algo = '123' AND algo =123 OR algpo='123' AND hpss = 'a' ;"
a=selectSintaxis(example_select)
#example_insert = "INSERT INTO tabla ( columna1,columna2 , hola ,columna) VALUES ( 'aa' , '123',12 ) ;"
#b = insertSintaxis(example_insert)
#example_update = "UPDATE tabla SET algo = 'a' ,jeje='hola',hi=123 WHERE algo= 123 AND jeje = '12' OR hola =123 ;"
#c = updateSintaxis(example_update)

print(a)


