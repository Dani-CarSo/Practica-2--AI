#1
#Straight merging

def straight_merge(lista_A, lista_B):
    # Arreglo vacío donde guardaremos el resultado combinado
    resultado = []
    
    # Punteros para rastrear la posición actual en cada lista
    i = 0  # Puntero para lista_A
    j = 0  # Puntero para lista_B

    # Mientras ambas listas tengan elementos por comparar
    while i < len(lista_A) and j < len(lista_B):
        if lista_A[i] < lista_B[j]:
            resultado.append(lista_A[i])  # Agregamos el elemento de A por ser menor
            i += 1                        # Avanzamos el puntero de A
        else:
            resultado.append(lista_B[j])  # Agregamos el elemento de B por ser menor o igual
            j += 1                        # Avanzamos el puntero de B

    # Si la lista_B se terminó primero, agregamos lo que sobró de lista_A
    while i < len(lista_A):
        resultado.append(lista_A[i])
        i += 1

    # Si la lista_A se terminó primero, agregamos lo que sobró de lista_B
    while j < len(lista_B):
        resultado.append(lista_B[j])
        j += 1

    return resultado

# Bloque de ejecución 
A = [2, 5, 9]
B = [3, 6, 7]
lista_mezclada = straight_merge(A, B)
print("Resultado de Straight Merging:", lista_mezclada)