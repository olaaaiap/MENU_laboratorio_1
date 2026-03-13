import numpy as np

def jacobi(A, b, x0,  tol = 1.e-6, maxit = 100, verbose = True): 
    """
    Función para resolver el sistema de ecuaciones lineales Ax = b utilizando el método de Jacobi.

    :param A: matriz con los valores de los coeficientes
    :param b: vector con los términos independientes
    :param x0: vector inicial
    :param tol: tolerancia
    :param maxit: número máximo de iteraciones
    :param verbose: si es True, imprime información de cada iteración
    :return: solucion x
    """
    xk = x0.copy()
    for k in range(1, maxit+1):
        xprev = xk.copy()
        for i in range(len(A)):
            suma = np.dot(A[i], xprev)
            xk[i] = xprev[i] + 1 / A[i,i]*(b[i]-suma)

        error = np.linalg.norm(xk-xprev, np.inf)
        if verbose:
            print(f"Iteración {k}: x = {xk}, error = {error}")
            
        if error < tol:
            break
    return xk
    


