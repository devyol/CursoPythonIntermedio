################ Método Recursivo Adivina Color
def adivinaColor(color, limite):
    if(limite>0 and color==4):
        return "Has ganado el juego"
    else:
        if(limite>1):
            print("¿Intenta de nuevo?")
            print("1. Azul")
            print("2. Verde")
            print("3. Rojo")
            print("4. Naranja")
            color = int(input())
            return adivinaColor(color, limite-1)
        else:
            return "Has Perdido"

################ ADIVINA QUE COLOR ESTOY PENSANDO ###################
print()
print("¿Que color estoy pensando?")
print("1. Azul")
print("2. Verde")
print("3. Rojo")
print("4. Naranja")
color = int(input())
print(adivinaColor(color,3))