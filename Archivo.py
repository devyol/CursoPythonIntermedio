import os

def pintaSeparador():
    print("#######################################################")


#LEE TODAS LAS LINEAS DEL ARCHIVO
pintaSeparador()
print("LEYENDO TODAS LAS LINEAS DEL ARCHIVO demofile.txt")
pintaSeparador()
f = open("demofile.txt","r")
print(f.read())

#LEYENDO LOS PRIMEROS 5 CARACTERES DEL ARCHIVO demofile.txt
pintaSeparador()
print("LEYENDO LOS PRIMEROS 5 CARACTERES DEL ARCHIVO demofile.txt")
pintaSeparador()
f = open("demofile.txt","r")
print(f.read(5))

#LEYENDO LINEAS
pintaSeparador()
print("LEYENDO LINEAS")
pintaSeparador()
f = open("demofile.txt","r")
print(f.readline())

#CIERRE DEL ARCHIVO AL TERMINAR DE LEERLO
pintaSeparador()
print("CIERRE DEL ARCHIVO AL TERMINAR DE LEERLO")
pintaSeparador()
f = open("demofile.txt","r")
print(f.readline())
f.close

#ABRIENDO EL ARCHIVO Y AGREGANDO CONTENIDO
pintaSeparador()
print("ABRIENDO EL ARCHIVO Y AGREGANDO CONTENIDO")
pintaSeparador()
f = open("demofile.txt","a")
f.write("\nNow the file has more content!")
f.close()

#ABRIENDO EL ARCHIVO CON EL CONTENIDO AGREGADO
pintaSeparador()
print("ABRIENDO EL ARCHIVO CON EL CONTENIDO AGREGADO")
pintaSeparador()
f = open("demofile.txt","r")
print(f.read())

#ELIMINAR ARCHIVO - SE DEBE IMPORTAR EL MODULO DEL SISTEMA OPERATIVO Y VALIDAR SI EXISTE

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("the file does exist")


#CREANDO UN ARCHIVO NUEVO
pintaSeparador()
print("CREANDO UN ARCHIVO NUEVO")
pintaSeparador()
f = open("myfile.txt","x")