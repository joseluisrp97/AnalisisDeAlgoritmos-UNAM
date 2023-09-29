from numpy import array
import random

class Piso:
    def __init__(self, n):
        """Inicializa el objeto Piso y llama a los métodos para crear la matriz y adoquinarla.

        Args:
            n (int): La potencia de 2 que determina el tamaño de la matriz.
        """
        self.numeros = list(reversed(range(1, 90)))  
        self.M = self.creaMatriz(n)  
        self.adoquinamiento(self.M)  

    def creaMatriz(self, n):
        """Crea una matriz de tamaño 2^n x 2^n e inserta un valor especial -1 en una ubicación aleatoria.

        Args:
            n (int): La potencia de 2 que determina el tamaño de la matriz.

        Returns:
            array: La matriz creada.
        """
        m = 2**n
        self.M = array([[0] * m for _ in range(m)])
        x, y = random.randint(0, m-1), random.randint(0, m-1)
        self.M[y][x] = -1
        print(f"El cuadrado especial original está en: (c={x},r={y})")
        return self.M

    def buscaEspecial(self, M):
        """Encuentra y devuelve las coordenadas del cuadrado especial (-1) en la matriz.

        Args:
            M (array): La matriz en la que buscar.

        Returns:
            tuple: Las coordenadas del cuadrado especial.
        """
        return next((i, j) for i, row in enumerate(M) for j, col in enumerate(row) if col != 0)

    def adoquinamiento(self, M):
        """Adoquina la matriz utilizando un enfoque recursivo.

        Args:
            M (array): La matriz a adoquinar.
        """
        m = len(M)
        if m == 1: return

        x, y = self.buscaEspecial(M)  
        e = self.numeros.pop()  
        
        coords = [
            [(m//2, m//2), (m//2, m//2-1), (m//2-1, m//2)],
            [(m//2, m//2), (m//2, m//2-1), (m//2-1, m//2-1)],
            [(m//2, m//2), (m//2-1, m//2), (m//2-1, m//2-1)],
            [(m//2-1, m//2-1), (m//2, m//2-1), (m//2-1, m//2)]
        ][(x >= m//2) * 2 + (y >= m//2)]
        
        for coord in coords:
            if M[coord] == 0:
                M[coord] = e

        for i in [(0, m//2, 0, m//2), (0, m//2, m//2, m), (m//2, m, 0, m//2), (m//2, m, m//2, m)]:
            self.adoquinamiento(M[i[0]:i[1], i[2]:i[3]])

        if m == 2: print(M) 


