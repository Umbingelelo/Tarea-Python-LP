def InsertCSV(archivo, columnas_insertar,valores_insertar):
    file = open(archivo,"r")

    cosas = file.readlines()
    info = []
    
    for i in cosas:
        i = i.strip("\n").split(";")
        info.append(i)

    file.close()

    columnas = info[0]
    nueva_columna = []

    for i in range(len(columnas)):
        if(columnas[i] in columnas_insertar):
            nueva_columna.append(valores_insertar[columnas_insertar.index(columnas[i])])
        else:
            nueva_columna.append("")
    
    output = "\n"
    for i in range(len(nueva_columna)-1):
        agregar = str(nueva_columna[i]) + ";"
        output = output + agregar
    output = output + str(nueva_columna[len(nueva_columna)-1])
    
    #Escribir en archivo
    file = open(archivo,"a")
    file.write(output)
    file.close()


columnas_insertar = ["Nombre","Rut","Rol","Telefono","Edad"]
valores_insertar = ["Cristobal Alvarez", "20382677-2","201873629-5",91783240,19]
InsertCSV("Estudiantes.csv",columnas_insertar,valores_insertar)