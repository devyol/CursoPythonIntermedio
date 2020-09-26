#ARGUMENTOS ARBITRARIOS, * argumentos

'''
Si no sabe cuántos argumentos se pasarán a su función
agregue un *antes del nombre del parámetro en la definición de la funcion

De esta forma, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia'''

def my_function(*kids):
    print("The youngest child is "+ kids[2])

my_function("Emil","Tobias","Linus")


#ARGUMENTOS DE PALABRAS CLAVE

'''También puede enviar arguntos con la sintaxis clave=valor'''

def my_function2(child3, child2,child1):
    print("The youngest child is "+ child3)

my_function2(child1="Emil",child2="Tobias",child3="Linus")


#ARGUMENTOS DE PALABRAS CLAVE ARBITRARIAS, **kwargs
'''Si no sabe cuántos argumentos de palabras clave se pasarán a su
función, agregue dos asteriscos: **antes del nombre del parámetro
en la definición de la función.'''

def my_function3(**kid):
    print("His last name is " + kid["lname"])

my_function3(fname= "Tobias", lname="Refsnes")


