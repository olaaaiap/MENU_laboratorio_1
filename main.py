import numpy as np
import time
import sys

def construir_A(n):
    array_4 = np.full(n, 4)
    array_1 = np.full(n-1, -1)

    #Generar diagonales
    diagonal = np.diag(array_4)
    diagonal_superior = np.diag(array_1, k=1)
    diagonal_inferior = np.diag(array_1, k=-1)

    A = diagonal + diagonal_superior + diagonal_inferior
    return A


def construir_B(n):
    array_b = np.full(n, 1)
    return array_b


if __name__ == "__main__":
    n=50000
    
    start_time = time.perf_counter()
    matrix = construir_A(n)
    b = construir_B(n)
    end_time = time.perf_counter()

    print(f"Tamaño A (bytes): {matrix.nbytes}")
    print(f"Tamaño b (bytes): {b.nbytes}")
    print(f"Tamaño A (MB): {matrix.nbytes / (1024 * 1024)}")
    print(f"Tamaño b (MB): {b.nbytes / (1024 * 1024)}")
    print(f"Tamaño A (GB): {matrix.nbytes / (1024 * 1024 * 1024)}")
    print(f"Tamaño b (GB): {b.nbytes / (1024 * 1024 * 1024)}")

    duration = end_time - start_time
    print(duration)
    print(matrix)
