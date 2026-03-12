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
     #PARTE 1
    print("-----------------------------PARTE 1---------------------------")
    # n=10000
    n_values = [10,20,100,200,1000,2000,10000,20000]

    for n in n_values: 
        start_time = time.perf_counter()
        matrix = construir_A(n)
        b = construir_B(n)
        end_time = time.perf_counter()

        print(f"\nValor de n: {n}")
        print(f"Tamaño A (bytes): {matrix.nbytes}")
        print(f"Tamaño b (bytes): {b.nbytes}")
        print(f"Tamaño A (MB): {matrix.nbytes / (1024 * 1024)}")
        print(f"Tamaño b (MB): {b.nbytes / (1024 * 1024)}")
        print(f"Tamaño A (GB): {matrix.nbytes / (1024 * 1024 * 1024)}")
        print(f"Tamaño b (GB): {b.nbytes / (1024 * 1024 * 1024)}")

        duration = end_time - start_time
        print(f"Tiempo de contrucción: {duration} segundos")

    
    #PARTE 2
    print("\n-----------------------------PARTE 2---------------------------")
    start_time_jacobi = time.perf_counter()
    x0 = np.zeros(len(b))
    x_jacobi = jacobi.jacobi(matrix, b, x0)

    end_time_jacobi = time.perf_counter()
    duration_jacobi = end_time_jacobi - start_time_jacobi
    print(f"\nTiempo de ejecución Jacobi: {duration_jacobi} segundos")

    error_jacobi = np.linalg.norm(x_jacobi - 0.5*np.ones(len(x_jacobi)), np.inf)
    print(f"Resultado Jacobi: {x_jacobi[:5]}, error: {error_jacobi}")


    #PARTE 3
    print("\n-----------------------------PARTE 3---------------------------")
    n_values = [10,20,100,200,1000,2000,10000,20000]

    for n in n_values:      
        start_time = time.perf_counter()

        matrix = construir_A(n)
        b = construir_B(n)

        res = np.linalg.solve(matrix, b)
        ones= np.ones(len(res))
        sol_exacta = 1/2 * ones
        error = np.linalg.norm(res - sol_exacta, np.inf)
    
        end_time = time.perf_counter()
        duration_linalg_solve = end_time - start_time
        print(f"Tiempo de ejecución linalg_solve: {duration_linalg_solve} segundos")
        print(f"Resultado: {res[:5]}, error: {error}")