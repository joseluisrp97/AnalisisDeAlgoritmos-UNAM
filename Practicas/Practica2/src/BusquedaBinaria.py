def busqueda_binaria(lista):
    """
    Busca un índice i tal que lista[i] = i usando búsqueda binaria.

    Args:
    - lista (list): Lista de enteros.

    Returns:
    - int or None: Índice i si existe, de lo contrario None.
    """
    inicio, fin = 0, len(lista) - 1
    contador_iteraciones = 0  # Contador de iteraciones

    while inicio <= fin:
        contador_iteraciones += 1  # Incrementar contador de iteraciones
        medio = (inicio + fin) // 2

        # Mostrar el espacio de búsqueda actual
        print(f"Iteración {contador_iteraciones}: {lista[inicio:fin+1]}")

        if lista[medio] == medio:
            return medio, contador_iteraciones
        elif lista[medio] < medio:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None, contador_iteraciones


def main():
    nombre_archivo = input("Introduce el nombre del archivo (.txt): ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = archivo.read().strip().split(',')
            lista = [int(x) for x in datos]

        print(f"Secuencia: {', '.join(map(str, lista))}")

        idx, iteraciones = busqueda_binaria(lista)

        if idx is not None:
            print(f"Elemento encontrado: {idx}")
        else:
            print("No se encontró un índice i tal que lista[i] = i.")
        
        print(f"Número total de iteraciones realizadas: {iteraciones}")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica el nombre y vuelve a intentarlo.")


if __name__ == '__main__':
    main()
