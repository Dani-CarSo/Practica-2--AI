#2
#Selección (SelectionSort).

def ordenamiento_seleccion(lista):
    # Obtenemos la longitud total de la lista
    n = len(lista)
    
    # Recorremos la lista desde el primer elemento hasta el penúltimo
    # No es necesario llegar al último porque para entonces ya estará ordenado
    for i in range(n - 1):
        
        # Suponemos inicialmente que el elemento actual (i) es el mínimo de la sublista
        indice_minimo = i
        
        # Este ciclo interno busca el verdadero valor mínimo en el resto de la lista desordenada
        # Comienza desde 'i + 1' hasta el final de la lista
        for j in range(i + 1, n):
            
            # Si encontramos un elemento que es menor que nuestro mínimo actual...
            if lista[j] < lista[indice_minimo]:
                
                # Actualizamos el índice para apuntar al nuevo elemento más pequeño
                indice_minimo = j
                
        # Una vez terminado el ciclo interno, si el índice del mínimo cambió, 
        # significa que encontramos un número más pequeño que el que estaba en la posición 'i'
        if indice_minimo != i:
            
            # Intercambiamos los valores en Python de forma directa (Swap)
            # El valor en 'i' pasa a la posición del mínimo, y el mínimo pasa a la posición 'i'
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
            
    # Devolvemos la lista completamente ordenada
    return lista

#  Ejemplo de uso 
# Creamos una lista desordenada para la prueba
mi_lista = [64, 25, 12, 22, 11]

print("Lista original:", mi_lista)

# Llamamos a la función
lista_ordenada = ordenamiento_seleccion(mi_lista)

print("Lista ordenada:", lista_ordenada)