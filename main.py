import numpy as np


def construir_A(n):
    array_4 = np.full(n, 4)
    array_1 = np.full(n-1, -1)

    #Generar diagonales
    diagonal = np.diag(array_4)
    diagonal_superior = np.diag(array_1, k=1)
    diagonal_inferior = np.diag(array_1, k=-1)

    A = diagonal + diagonal_superior + diagonal_inferior
    return A


if __name__ == "__main__":
    print("Hello, World!")
    matrix = construir_A(4)
    print(matrix)
