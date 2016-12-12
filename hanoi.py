# En esta torre poner los discos
Torre1 = ([], "Torre 1")
Torre2 = ([], "Torre 2")
Torre3 = ([], "Torre 3")

def solve(n, t1, t2, t3):
    if n > 0:
        solve(n - 1, t1, t3, t2)
        if t1[0]:
            disk = t1[0].pop()
            print("Movido disco [" + str(disk) + "] de la " + t1[1] + " a la " + t3[1])
            t3[0].append(disk)
            # Comentar la siguiente línea si se quiere desactivar la visualización del
            # estado de las torres a cada paso
            printTowers()
        solve(n - 1, t2, t1, t3)

def printTowers():
    print(Torre1[1],Torre1[0])
    print(Torre2[1],Torre2[0])
    print(Torre3[1],Torre3[0])

def fillTowers(size):
    for i in range(size):
        Torre1[0].append(size)
        size = size - 1

# Pregunta la cantidad de discos e inicializa
size = int(input("Cuántos discos quieres poner? "))
fillTowers(size)

# Muestra el estado inicial de las torres
printTowers()

# Llamada a la función de resolución
solve(len(Torre1[0]),Torre1,Torre2,Torre3)

# Muestra el estado final de las torres
#printTowers()
