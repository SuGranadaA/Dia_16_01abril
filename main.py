#Abrimos el archivo
archivo = open('archivo.txt', 'w+')

#Escribimos el archivo
archivo.write("Hola\n")
archivo.write("Buenos días\n")
archivo.write("Hoy es un buen día\n")

#Imprimimos el archivo
print(archivo)

#Cerramos el archivo
archivo.close()

#Abrimos el archivo
archivo = open('archivo.txt', 'r')

#Definimos las funciones
letras = archivo.read()
lista = archivo.readlines()

#Imprimimos las funciones
print(lista)
print(letras)

#Cerramos el archivo
archivo.close()

#Abrimos el archivo
archivito = open('archivito.txt', 'r')

#Mostramos el contenido del archivo
print(archivito.tell())

#Ubicamos el puntero al inico del archivo
archivito.seek(0, 0)
primeralinea = archivito.readline()
segundalinea = archivito.readline()

#Imrimimos las líneas del archivo
print(primeralinea)
print(segundalinea)

#Movemos el puntero al final del archivo
archivito.seek(0, 2)

#Imprimimos el archivo
print(archivito)

#Cerramos el archivo
archivito.close()
