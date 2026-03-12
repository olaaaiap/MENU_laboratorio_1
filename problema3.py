import numpy as np
import time
import jacobi
from scipy import sparse
from scipy.sparse.linalg import spsolve



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

    for n in n_values:      
        start_time = time.perf_counter()

        resolverSistema(n)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"\nTiempo de ejecución scipy: {duration} segundos")
        
