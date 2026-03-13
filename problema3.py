import numpy as np
import time
from scipy import sparse
from scipy.sparse.linalg import spsolve

####CODIGOS DE LA PARTE 1####
def construir_A(n):
    """
    Construir la matriz cíclica tridiagonal A de tamaño n x n

    :param n: tamaño de la matriz
    :return: matriz A
    """

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
    return np.array(A)


def construir_B(n):
    """
    Construir el vector b de tamaño n.

    :param n: tamaño del vector
    :return: vector b
    """
    array_b = np.full(n, 1)
    return np.array(array_b)
###########################################

################### CODIGOS PARTE 2######################
def jacobi_cíclico(n, tol = 1.e-6, maxit=100, verbose=True):
    """
    Función para resolver el sistema de ecuaciones lineales Ax = b utilizando el método de Jacobi cíclico.

    :param n: tamaño del sistema
    :param tol: tolerancia
    :param maxit: número máximo de iteraciones
    :param verbose: si es True, imprime información de cada iteración
    :return: solucion x
    """
    x0 = np.zeros(n)
    xk=x0.copy()
    for k in range(1, maxit+1):
        xprev = xk.copy()
        xk[0]= 1/4*(1+xprev[1]+xprev[n-1])
        for i in range(1, n-1):
            xk[i] = 1/4*(1+xprev[i-1]+xprev[i+1])
        xk[n-1] = 1/4*(1+xprev[0]+xprev[n-2])
        error = np.linalg.norm(xk-xprev, np.inf)
        #if verbose:
          #  print(f"Iteración {k}: x = {xk[:5]}, error = {error}")
            
        if error < tol:
            break
    return xk
#################################################################

def resolverSistema(n):
    
    # Diagonales
    diag_principal = 4.0 * np.ones(n)
    diag_superior = -1.0 * np.ones(n - 1)
    diag_inferior = -1.0 * np.ones(n - 1)
    # Matriz tridiagonal
    A_sparse = sparse.diags(
    [diag_inferior, diag_principal, diag_superior],
    offsets=[-1, 0, 1],
    shape=(n, n),
    format="lil"
    )
    # Elementos cíclicos (esquinas)
    A_sparse[0, n - 1] = -1.0
    A_sparse[n - 1, 0] = -1.0
    A_sparse = A_sparse.tocsc()
    b = np.ones(n)
    x = spsolve(A_sparse, b)

if __name__ == "__main__":
       #PARTE 3
    n_values = [10,20,100,200,1000,2000,10000,20000]
    #iterar sobre los valores de n...
    for n in n_values:     

        #Calculo los valores usando las funcion de la parte 1
        start_time = time.perf_counter()
        matrix = construir_A(n)
        b = construir_B(n)
        end_time = time.perf_counter()
        duration = end_time - start_time
        #print(f"\nTiempo de ejecución de enfoque denso para {n}: {duration} segundos")

        #calcular tiempo de ejecución de jacobi cíclico
        start_time_jacobi = time.perf_counter()
        xk = jacobi_cíclico(n)
        end_time_jacobi = time.perf_counter()
        duration_jacobi = end_time_jacobi - start_time_jacobi
        #print(f"\nTiempo de ejecución de jacobi para {n}: {duration} segundos")

        #Calculo los valores usando las funcion de la parte 3
        start_time = time.perf_counter()
        resolverSistema(n)
        end_time = time.perf_counter()
        durationScipy = end_time - start_time

        diff = 0
        speedup_pct = 0
        
        duration = round(duration,5)
        durationScipy = round(durationScipy,5)
               

        print(f"Para {n}")
        print(f"Duracion jacobi: {duration:.5f}")
        print(f"Duracion de scipy: {durationScipy:.5f}")


        if(duration > durationScipy):

            diff = duration - durationScipy
            speedup_pct = (diff / duration) * 100   
            print(f"Scipy supone una mejoría de:")  
        else:        
            diff = durationScipy - duration
            speedup_pct = (diff / durationScipy) * 100
            print(f"Jacobi supone una mejoría de:") 

        print(f"Diferencia: {diff:.5f} s")
        print(f"Mejora de velocidad: {speedup_pct:.2f}% \n")
        
