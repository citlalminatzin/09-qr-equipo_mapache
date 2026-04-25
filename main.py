#!/usr/bin/env python

from collections.abc import Sequence
import numbers
from math import pi

from eigenvalues import eigenvals
from qr import qr_simple

# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(Sequence):
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  

def main():
    A = [
        [5, -2],
        [-2, 8]
    ]

    # Otra matriz de ejemplo:
   # A = [
   # [4, 1, 1],
   # [1, 3, 0],
   # [1, 0, 2]
   # ]

    #Ejercicio 1
    print("\n**** Ejercicio 1: Eigenvalores esperados ****")
    vals = eigenvals(A, n=100)
    print("Eigenvalores:", [round(v, 6) for v in vals])

    #Ejercicio 2
    print("\n**** Ejercicio 2: Método QR con n iteraciones ****")
    Ak = qr_simple(A, 10)
    print("Matriz final:", Ak)
    print("Diagonal (eigenvalores):", [Ak[i][i] for i in range(len(Ak))])

    #Ejercicio 3
    print("\n**** Ejercicio 3: Método QR con tolerancia ****")
    vals = eigenvals(A, n=1000, tolerance=1e-10)
    print("Eigenvalores:", [round(v, 6) for v in vals])

if __name__ == "__main__":
    main()
