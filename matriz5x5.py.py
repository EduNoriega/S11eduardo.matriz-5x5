# Universidad: UEA
# Estudiante: Eduardo Luis Noriega Peñafiel
# Paralelo: S
# Tarea: Semana 11 - Matriz 5x5

matriz = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        valor = int(
            input(f"Ingrese el valor para la posicion [{i}][{j}]: ")
        )
        matriz[i][j] = valor

print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()

print("\nEduardo Noriega - Paralelo c - UEA - Tarea Semana 11")

