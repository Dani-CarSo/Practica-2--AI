#5
#QuickSort

# Definición de la función principal que se llamará recursivamente
def quicksort(arr, low, high):
    # Condición de parada: si 'low' es menor que 'high', significa que el subarreglo tiene al menos 2 elementos
    if low < high:
        
        # Se ejecuta la partición y se obtiene la posición final del pivote actual
        pi = partition(arr, low, high)

        # Llamada recursiva para ordenar los elementos que quedaron a la izquierda del pivote
        quicksort(arr, low, pi - 1)
        
        # Llamada recursiva para ordenar los elementos que quedaron a la derecha del pivote
        quicksort(arr, pi + 1, high)

# Función encargada de acomodar los elementos menores a la izquierda y mayores a la derecha
def partition(arr, low, high):
    # Elegimos el último elemento del subarreglo actual como el "pivote"
    pivot = arr[high]
    
    # 'i' rastrea la posición del último elemento que sabemos que es menor o igual al pivote.
    # Comienza antes del inicio del subarreglo porque aún no hemos revisado nada.
    i = low - 1  
    
    # El puntero 'j' recorre todo el subarreglo actual de principio a fin (sin incluir el pivote)
    for j in range(low, high):
        
        # Si el elemento actual arr[j] es menor o igual al pivote...
        if arr[j] <= pivot:
            # ...avanzamos el índice 'i' para abrir un espacio seguro...
            i += 1
            
            # ...e intercambiamos el elemento arr[i] con arr[j] para mover el menor a la izquierda
            arr[i], arr[j] = arr[j], arr[i] 
            
    # Al terminar el bucle, todos los menores están a la izquierda (hasta el índice i).
    # Intercambiamos el pivote (arr[high]) con el elemento que le sigue a los menores (arr[i + 1])
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Devolvemos la posición exacta en la que quedó el pivote para que quicksort sepa dónde dividir
    return i + 1

#  Bloque de ejecución de ejemplo 
# Creamos una lista desordenada de prueba
datos = [8, 2, 4, 7, 1, 3]

# Llamamos a quicksort pasando la lista, el índice inicial (0) y el índice final (longitud - 1)
quicksort(datos, 0, len(datos) - 1)

# Imprimimos el resultado final en la consola
print("Arreglo ordenado:", datos)