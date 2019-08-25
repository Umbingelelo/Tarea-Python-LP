file = open("Estudiantes.csv","r")

cosas = file.readlines()
info = []

for i in cosas:
    i = i.strip("\n").split(",")
    info.append(i)

def sel
