nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", 
    "Messi", "Teller", "Einstein", "Pele", "Juanes"
]

# List
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

# Separando
def clasificar_nombres():
    for nombre in nombres:
        if nombre in magos:
            continue
        elif nombre in cientificos:
            continue
        else:
            otros.append(nombre)

# Agrega El Gran
def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Print
def imprimir_nombres(lista, titulo):
    print(f"\n{titulo}:")
    for nombre in lista:
        print(nombre)

# Print List
print("Lista completa de nombres:")
imprimir_nombres(nombres, "Todos los nombres")
clasificar_nombres()

# Grandioso
hacer_grandioso()

# Print
imprimir_nombres(magos, "Grandes Magos")
imprimir_nombres(cientificos, "Científicos")
imprimir_nombres(otros, "Otros")