import numpy as np
import time
import jacobi

def construir_A(n):
    array_4 = np.full(n, 4)
    array_1 = np.full(n-1, -1)

    #Generar diagonales
    diagonal = np.diag(array_4)
    diagonal_superior = np.diag(array_1, k=1)
    diagonal_inferior = np.diag(array_1, k=-1)

    A = diagonal + diagonal_superior + diagonal_inferior
    #poner valor -1 al ultimo elemento de la fila 1
    A[0, -1] = -1
    #poner valor -1 al primer elemento de la ultima fila
    A[-1, 0] = -1
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

    print(f"\nTamaño A (bytes): {matrix.nbytes}")
    print(f"Tamaño b (bytes): {b.nbytes}")
    print(f"Tamaño A (MB): {matrix.nbytes / (1024 * 1024)}")
    print(f"Tamaño b (MB): {b.nbytes / (1024 * 1024)}")
    print(f"Tamaño A (GB): {matrix.nbytes / (1024 * 1024 * 1024)}")
    print(f"Tamaño b (GB): {b.nbytes / (1024 * 1024 * 1024)}")

    duration = end_time - start_time
    print(duration)
    print(matrix)
    


    start_time_jacobi = time.perf_counter()
    x0 = np.zeros(len(b))
    jacobi.jacobi(matrix, b, x0)
    
    end_time_jacobi = time.perf_counter()
    duration_jacobi = end_time_jacobi - start_time_jacobi
    print(f"\nTiempo de ejecución Jacobi: {duration_jacobi} segundos")
