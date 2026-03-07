import numpy as np


def construir_A(n):
    array_4 = np.full(n, 4)
    array_1 = np.full(n-1, -1)

    #Generar diagonales
<<<<<<< HEAD
    diagonal = np.diag(array_4)
    diagonal_superior = np.diag(array_1, k=1)
    diagonal_inferior = np.diag(array_1, k=-1)

    A = diagonal + diagonal_superior + diagonal_inferior
    return A
=======
    diagonal = np.array(array_4)
    diagonal_superior = np.array(array_1)
    diagonal_inferior = np.array(array_1)

    diagonal_matrix=[]
    diagonal_matrix.append(np.diag(diagonal))
    diagonal_matrix.append(np.diag(diagonal_superior, k=1))
    diagonal_matrix.append(np.diag(diagonal_inferior, k=-1))
    print(diagonal_matrix)
    # return A
>>>>>>> 9795cc13f85db720b85e58ac43b571bff080eafd


if __name__ == "__main__":
    print("Hello, World!")
<<<<<<< HEAD
    matrix = construir_A(4)
    print(matrix)
=======
    construir_A(4)
>>>>>>> 9795cc13f85db720b85e58ac43b571bff080eafd
