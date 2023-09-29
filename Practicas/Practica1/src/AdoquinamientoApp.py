from tkinter import Tk, Frame
import random
from Adoquin import *
from Piso import *
import sys

class AdoquinamientoApp:
    """Clase principal que administra la aplicación de adoquinamiento.

    Esta clase orquesta la creación de una interfaz gráfica para ilustrar el algoritmo de adoquinamiento, 
    demostrando una disposición matricial de adoquines con colores asignados dinámicamente.

    Atributos:
        ventanaAdoquin (Tk): El contenedor principal de la aplicación.
        instanciaPiso (Piso): Objeto que representa la estructura de adoquinamiento del piso.
        cuadricula (Frame): Un marco que hospeda las unidades de adoquines en la GUI.
    """
    
    def __init__(self, inicioVentana):
        """Crea una nueva instancia de la aplicación AdoquinamientoApp.

        Inicializa los atributos y métodos necesarios para poner en marcha la aplicación.
        
        Args:
            inicioVentana (Tk): El contenedor principal de la aplicación.
        """
        self.ventanaAdoquin = inicioVentana
        self.cuadricula = self.generarCuadricula()
        self.instanciaPiso = Piso(int(sys.argv[1]))
        self.coloresDiccionario = self.obtenerDiccionarioColores()
        self.mostrarAdoquines(self.instanciaPiso.M)
    
    def generarCuadricula(self):
        """Crea un marco para alojar las unidades de adoquines en la GUI.

        Returns:
            Frame: Un marco donde se ubicarán las unidades de adoquines.
        """
        return Frame(self.ventanaAdoquin, pady=4, padx=4).grid(column=0, row=0)
    
    def obtenerDiccionarioColores(self):
        """Produce un diccionario de colores en formato hexadecimal.

        Returns:
            dict: Un mapeo de números enteros a colores en formato hexadecimal.
        """
        return {i: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for i in range(1, 201)}

    def mostrarAdoquines(self, matriz):
        """Ilustra los adoquines en la GUI conforme a la matriz de adoquinamiento indicada.

        Args:
            matriz (list): Una estructura de lista de listas que representa la matriz adoquinada.
        """
        dimension = len(matriz)
        cuadricula = [[Adoquin(padre=self.cuadricula, numColor=valor, listaColores=self.coloresDiccionario) for valor in fila] for fila in matriz]

        for i, fila in enumerate(cuadricula):
            for j, adoquin in enumerate(fila):
                adoquin.cuadro.grid(row=i, column=j)

if __name__ == "__main__":
    inicioVentana = Tk()
    inicioVentana.title('Adoquinamiento')
    
    if int(sys.argv[1]) > 4:
        print('Intenta con números más bajos.')
        exit(1)
    
    aplicacion = AdoquinamientoApp(inicioVentana)
    inicioVentana.mainloop()
