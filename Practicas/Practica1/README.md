# Análisis de Algoritmos - Práctica 1
### Adoquinamiento en Python
**Autor:** José Luis Raya Pérez  
**Matrícula:** 319659058

## 📌 Planteamiento del problema
Se busca adoquinar una cuadrícula de \( m \times m \) utilizando adoquines en forma de "L". Las condiciones son:
- \( m = 2^k \) es decir, \( m \) debe ser potencia de 2.
- Existirá un "cuadro especial" ubicado de manera arbitraria en la cuadrícula que no podrá ser cubierto por ninguna otra pieza.

## 🔍 Descripción
El programa recibe como entrada un entero positivo \( k \), que indicará el tamaño de la cuadrícula a adoquinar. La ejecución se realiza desde la carpeta `src`.

**Ejemplo de entrada:**
python3 AdoquinamientoApp.py 4


### Salida
Se mostrará en la terminal una representación gráfica del problema resolviéndose paso a paso, así como la solución final. Cada adoquín estará etiquetado para su identificación. Se puede optar por utilizar bibliotecas especiales para realizar una interfaz gráfica.

**Ejemplo de salida:** La respuesta final se verá similar al diagrama proporcionado. El cuadro rojo representa el cuadro especial generado al inicio del algoritmo, mientras que los demás colores o etiquetas representan el acomodo de las piezas "L" en la cuadrícula.

## ⚙️ Instrucciones de ejecución
1. Navegar hasta la carpeta `src`.
2. Ejecutar el archivo `AdoquinamientoApp.py`.
3. Asegurarse de contar con la biblioteca `Tkinter` instalada.

## ❗ Nota
En caso de utilizar interfaz gráfica y que el programa sea funcional, se otorgarán +2 puntos extra sobre la calificación del programa.
