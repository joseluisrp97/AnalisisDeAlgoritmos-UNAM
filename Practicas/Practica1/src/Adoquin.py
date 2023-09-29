from tkinter import Canvas

class Adoquin:
    """Representa un adoquín en la gráfica de la matriz.
    
    Esta clase facilita la representación gráfica de cada adoquín individual en la matriz de adoquinamiento.
    
    Atributos:
        cuadro (Canvas): Un objeto canvas que representa gráficamente una unidad de adoquinamiento.
    """
    
    def __init__(self, padre, numColor, listaColores):
        """Inicializa una nueva instancia de la clase Adoquin.
        
        Utiliza los argumentos de numColor y listaColores para determinar el color de fondo del adoquín. 
        Se crea un diccionario de atributos de configuración y se utiliza para inicializar una nueva 
        instancia de Canvas que representa gráficamente el adoquín.
        
        Args:
            padre (Frame): El contenedor en el que se ubicará el adoquín.
            numColor (int): Una clave para buscar el color correspondiente en la lista de colores.
            listaColores (dict): Un diccionario que mapea las claves de color a sus respectivas representaciones en hexadecimal.
        """
        color_seleccionado = "red" if numColor == -1 else listaColores.get(numColor, "white")
        self.cuadro = Canvas(padre, bg=color_seleccionado, width=30, height=30)
