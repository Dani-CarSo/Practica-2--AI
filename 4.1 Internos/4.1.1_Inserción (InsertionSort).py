#1
#Inserción (InsertionSort)


def ordenamiento_insercion(lista):
    # Recorremos desde el segundo elemento (índice 1) hasta el final de la lista
    # El primer elemento (índice 0) se considera inicialmente ya ordenado
    for i in range(1, len(lista)):
        
        # Guardamos el elemento actual que queremos insertar en la posición correcta
        llave = lista[i]
        
        # Inicializamos 'j' como el índice del elemento justo a la izquierda de la llave
        j = i - 1
        
        # Movemos los elementos de la lista[0..i-1] que son mayores que la llave
        # a una posición adelante de su posición actual
        # El ciclo continúa mientras no lleguemos al inicio de la lista (j >= 0)
        # y el elemento de la izquierda sea mayor que nuestra llave
        while j >= 0 and lista[j] > llave:
            
            # Desplazamos el elemento mayor una posición hacia la derecha
            lista[j + 1] = lista[j]
            
            # Decrementamos 'j' para seguir comparando con los elementos de más a la izquierda
            j -= 1
            
        # Cuando el ciclo termina, insertamos la llave en su posición correcta
        # Se usa 'j + 1' porque 'j' disminuyó una vez de más en la última validación
        lista[j + 1] = llave
        
    # Devolvemos la lista ya completamente ordenada
    return lista

# Ejemplo de uso 
# Creamos una lista desordenada para probar el algoritmo
mi_lista = [12, 11, 13, 5, 6]

print("Lista original:", mi_lista)

# Llamamos a la función y guardamos el resultado
lista_ordenada = ordenamiento_insercion(mi_lista)

print("Lista ordenada:", lista_ordenada)