#!/usr/bin/env python

#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100, tolerance=1e-10)->list[float]:
#Realiza n iteraciones del algoritmo QR para calcular los eigenvalores de A
#Devuelve la estimación de los eigenvalores
    
    Ak = [row[:] for row in A]
    
    for _ in range(n):
        Q, R = qr(Ak)
        
        Ak = matmul(R, Q)
        
        casi_diagonal = True
        
        for i in range(len(Ak)):
            for j in range(len(Ak)):
                if i != j and abs(Ak[i][j]) > tolerance:
                    casi_diagonal = False
                    break
            if not casi_diagonal:
                break
        
        if casi_diagonal:
            break
    
    return [Ak[i][i] for i in range(len(Ak))]