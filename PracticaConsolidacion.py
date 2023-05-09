nombres = ['Harry Houdini','Newton','David Blaine','Hawking','Messi','Teller','Einstein','Pele','Juanes']
magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre == 'Harry Houdini' or nombre == 'David Blaine' or nombre == 'Teller':
        magos.append(nombre)
    elif nombre == 'Newton' or nombre == 'Hawking' or nombre == 'Einstein':
        cientificos.append(nombre)
    else:
        otros.append(nombre)


def hacer_grandioso():
    for contador in range(len(magos)):
        magos[contador] = "El gran " + magos[contador]

def imprimir_nombres():
    for nombre in nombres:
        print(nombre)

print(nombres)
hacer_grandioso()
print(magos)
print(cientificos)
print(otros) 