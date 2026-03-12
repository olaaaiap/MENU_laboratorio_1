import numpy as np
import time

#jacobi para el sistema cíclico
def jacobi_cíclico(n, tol = 1.e-6, maxit=100, verbose=True):
    x0 = np.zeros(n)
    xk=x0.copy()
    for k in range(1, maxit+1):
        xprev = xk.copy()
        xk[0]= 1/4*(1+xprev[1]+xprev[n-1])
        for i in range(1, n-1):
            xk[i] = 1/4*(1+xprev[i-1]+xprev[i+1])
        xk[n-1] = 1/4*(1+xprev[0]+xprev[n-2])
        error = np.linalg.norm(xk-xprev, np.inf)
        if verbose:
            print(f"Iteración {k}: x = {xk[:5]}, error = {error}")
            
        if error < tol:
            break
    return xk


if __name__ == "__main__":
    n_values = [10,20,100,200,1000,2000,10000,20000,50000]

    for n in n_values:
        start_time_jacobi = time.perf_counter()
        xk = jacobi_cíclico(n)
        end_time_jacobi = time.perf_counter()
        duration_jacobi = end_time_jacobi - start_time_jacobi

        error_jacobi = np.linalg.norm(xk - 0.5*np.ones(len(xk)), np.inf)

        print(f"\nCon n: {n}")
        print(f"Tiempo de ejecución Jacobi cíclico: {duration_jacobi} segundos")
        print(f"Error Jacobi cíclico: {error_jacobi}")

        print(f"\nTamaño xk: {xk.nbytes}")
        print(f"Tamaño total: {xk.nbytes * 2}")

        
        print(f"Tamaño xk (MB): {xk.nbytes / (1024 * 1024)}")
        print(f"Tamaño total (MB): {(xk.nbytes * 2) / (1024 * 1024)}")

        
        print(f"Tamaño xk (GB): {xk.nbytes / (1024 * 1024 * 1024)}")
        print(f"Tamaño total (GB): {(xk.nbytes * 2) / (1024 * 1024 * 1024)}")
