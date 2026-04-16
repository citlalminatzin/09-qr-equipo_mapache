#!/usr/bin/env python

#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100, tolerance=1e-10)->list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Devuelve la estimación de los eigenvalores
    """
    
    Ak = [row[:] for row in A]
    
    for _ in range(n):
        Q, R = qr(Ak)
        
        Ak = matmul(R, Q)
        
        off_diag_small = True
        for i in range(len(Ak)):
            for j in range(len(Ak)):
                if i != j and abs(Ak[i][j]) > tolerance:
                    off_diag_small = False
                    break
        
        if off_diag_small:
            break
    
    eigenvalues = [Ak[i][i] for i in range(len(Ak))]
    
    return eigenvalues