#6
# MergeSort

def mergesort(arr):
    # Condición de parada: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(arr) > 1:
        
        # 1. DIVIDIR: Encontramos el punto medio del arreglo
        medio = len(arr) // 2
        
        # Creamos dos subarreglos temporales (mitad izquierda y mitad derecha)
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Llamadas recursivas para seguir dividiendo ambas mitades
        mergesort(izquierda)
        mergesort(derecha)

        # 2. COMBINAR (MERGE): Inicializamos los punteros para recorrer las listas
        i = 0  # Puntero para la mitad izquierda
        j = 0  # Puntero para la mitad derecha
        k = 0  # Puntero para el arreglo original (donde guardaremos el resultado)

        # Comparamos elemento por elemento de ambas mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]  # Ponemos el de la izquierda porque es menor
                i += 1                 # Avanzamos en la lista izquierda
            else:
                arr[k] = derecha[j]    # Ponemos el de la derecha porque es menor o igual
                j += 1                 # Avanzamos en la lista derecha
            k += 1                     # Avanzamos en el arreglo final

        # Si quedaron elementos sueltos en la mitad izquierda, los copiamos todos
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedaron elementos sueltos en la mitad derecha, los copiamos todos
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

#  Bloque de ejecución 
datos = [4, 2, 1, 3]
mergesort(datos)
print("Arreglo ordenado por MergeSort:", datos)
