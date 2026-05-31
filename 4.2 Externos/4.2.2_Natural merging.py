#2
# Natural merging

def natural_merge_sort(lista):
    # Si la lista tiene 1 elemento o está vacía, ya está ordenada.
    if len(lista) <= 1:
        return lista

    # Bucle principal: se repite hasta que toda la lista esté en un solo tramo ordenado.
    while True:
        runs = []  # Lista para almacenar los índices de inicio de cada tramo ordenado.
        i = 0  # Inicializamos el índice para recorrer la lista desde el principio.

        # --- FASE 1: Identificar los tramos (runs) naturalmente ordenados ---
        while i < len(lista):
            runs.append(i)  # Guardamos el índice donde comienza este tramo ordenado.
            # Avanzamos mientras el siguiente elemento sea mayor o igual al actual (esté ordenado).
            while i + 1 < len(lista) and lista[i] <= lista[i + 1]:
                i += 1  # Incrementamos el índice para incluir el elemento en el tramo.
            i += 1  # Nos movemos al primer elemento del siguiente tramo.

        # Si solo encontramos un tramo (empieza en 0), significa que toda la lista ya está ordenada.
        if len(runs) <= 1:
            break  # Salimos del bucle principal.

        # --- FASE 2: Fusionar los tramos identificados de dos en dos ---
        # Recorremos la lista de tramos saltando de 2 en 2 para fusionar parejas.
        for j in range(0, len(runs) - 1, 2):
            inicio_izq = runs[j]  # Índice donde empieza el tramo izquierdo.
            inicio_der = runs[j + 1]  # Índice donde empieza el tramo derecho.

            # El tramo derecho termina donde empieza el siguiente, o al final de la lista si es el último.
            fin_der = runs[j + 2] if j + 2 < len(runs) else len(lista)

            # Creamos una sublista temporal fusionando el tramo izquierdo y el derecho.
            sublista_fusionada = merge(
                lista[inicio_izq:inicio_der], lista[inicio_der:fin_der]
            )

            # Reemplazamos la sección original de la lista con la sublista ya ordenada y fusionada.
            lista[inicio_izq:fin_der] = sublista_fusionada

    return lista  # Retornamos la lista completamente ordenada.


def merge(izquierda, derecha):
    resultado = []  # Lista vacía para ir armando el tramo combinado y ordenado.
    i = 0  # Puntero/índice para recorrer la sublista izquierda.
    j = 0  # Puntero/índice para recorrer la sublista derecha.

    # Comparamos elementos de ambas listas mientras ninguna se haya agotado.
    while i < len(izquierda) and j < len(derecha):
        # Si el elemento de la izquierda es menor o igual, va primero al resultado.
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])  # Agregamos el elemento izquierdo.
            i += 1  # Avanzamos el puntero de la lista izquierda.
        else:
            resultado.append(derecha[j])  # Agregamos el elemento derecho.
            j += 1  # Avanzamos el puntero de la lista derecha.

    # Si quedaron elementos sueltos en la lista izquierda, los agregamos todos al final.
    resultado.extend(izquierda[i:])
    # Si quedaron elementos sueltos en la lista derecha, los agregamos todos al final.
    resultado.extend(derecha[j:])

    return resultado  # Devolvemos la lista combinada y perfectamente ordenada.


# Ejemplo de Uso 
if __name__ == "__main__":
    # Lista desordenada de prueba (notarás que [1, 5], [2, 8] y [3, 9] ya tienen orden natural)
    datos = [1, 5, 2, 8, 3, 9, 4]
    print("Lista original:", datos)

    # Llamamos a la función de ordenamiento
    lista_ordenada = natural_merge_sort(datos)
    print("Lista ordenada:", lista_ordenada)
