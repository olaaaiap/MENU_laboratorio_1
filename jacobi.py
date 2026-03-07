import numpy as np

#las ecuaciones lineasles se pasan por un lado un vector de A  y otro de B (el vector de terminos independientes) 
def jacobi(A, b, x0,  tol = 1.e-6, maxit = 100, verbose = True): 
    xk = x0.copy()
    for k in range(1, maxit+1):
        xprev = xk.copy()
        for i in range(len(A)):
            # xk[i] = b[i]
            # for j in range(len(A[i])):
            #     if j != i:
            #         xk[i] -= A[i][j]*xprev[j]
            # xk[i] = xk[i] / A[i][i]

            #modo optimizado. podemos usar taichi dot para paralelizar el bucle de fuera.
            suma = np.dot(A[i], xprev)
            xk[i] = xprev[i] + 1 / A[i,i]*(b[i]-suma)

        error = np.linalg.norm(xk-xprev, np.inf)
        if verbose:
            print(f"Iteración {k}: x = {xk}, error = {error}")
            
        if error < tol:
            break
    return xk
    

A = np.array([[10, 1], [1,8]])
b = np.array([23, 26])
x0 = np.zeros(len(b))
jacobi(A, b, x0)



