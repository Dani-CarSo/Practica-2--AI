#3
#Intercambio

def ordenamiento_intercambio(lista):
    # Obtenemos la longitud de la lista
    
    n = len(lista)
    # Este ciclo externo controla cuántas pasadas completas haremos a la lista
    # En cada pasada, el elemento más grande restante "flota" hasta el final
    for i in range(n):
        
        # Una bandera para optimizar: si en una pasada no hay cambios, la lista ya está ordenada
        intercambio_ocurrio = False
        
        # El ciclo interno compara los elementos vecinos (j y j+1)
        # Se resta 'i' porque los últimos 'i' elementos ya están en su lugar correcto
        # Se resta '1' para no salirnos del índice al hacer 'j + 1'
        for j in range(0, n - i - 1):
            
            # Comparamos el elemento actual con su vecino de la derecha
            if lista[j] > lista[j + 1]:
                
                # Si el de la izquierda es mayor, los intercambiamos inmediatamente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
                # Marcamos que sí hubo un movimiento en esta pasada
                intercambio_ocurrio = True
                
        # Si terminamos el ciclo interno y no se hizo ningún intercambio, 
        # significa que la lista ya está perfectamente ordenada y podemos salir antes
        if not intercambio_ocurrio:
            break
            
    # Devolvemos la lista ordenada
    return lista

# --- Ejemplo de uso ---

# Lista desordenada para la prueba
mi_lista = [5, 1, 4, 2, 8]

print("Lista original:", mi_lista)

# Llamamos a la función
lista_ordenada = ordenamiento_intercambio(mi_lista)

print("Lista ordenada:", lista_ordenada)