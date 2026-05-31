#3
#Balanced multiway merging

import heapq


def balanced_multiway_merge(vias_entrada):
    # vias_entrada es una lista de listas (simulando los archivos de entrada).
    # Ejemplo: [[3, 9], [1, 8], [2, 7]]

    archivo_salida = []  # Aquí guardaremos el resultado de la fusión masiva.
    min_heap = (
        []
    )  # Estructura (Heap) para comparar el frente de todas las vías.

    # --- FASE 1: Colocar el primer elemento de cada vía en el Heap ---
    for indice_via, via in enumerate(vias_entrada):
        if via:  # Aseguramos que la vía no esté vacía
            # Guardamos: (valor, de qué vía viene, posición del elemento en esa vía)
            heapq.heappush(min_heap, (via[0], indice_via, 0))

    # --- FASE 2: Fusión de las N vías simultáneamente ---
    while min_heap:
        # Extraemos el elemento más pequeño actual de todas las vías
        valor, indice_via, indice_elemento = heapq.heappop(min_heap)

        # Lo guardamos en el archivo/lista de salida
        archivo_salida.append(valor)

        # Calculamos la posición del siguiente elemento de esa misma vía
        siguiente_indice = indice_elemento + 1

        # Si esa vía todavía tiene más elementos, metemos el siguiente al Heap
        if siguiente_indice < len(vias_entrada[indice_via]):
            siguiente_valor = vias_entrada[indice_via][siguiente_indice]
            heapq.heappush(
                min_heap, (siguiente_valor, indice_via, siguiente_indice)
            )

    return archivo_salida  # Retorna el archivo final unificado y ordenado


# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Simulamos 3 archivos/vías de entrada cuyos elementos internos ya están ordenados
    archivo_via1 = [3, 9, 15, 21]
    archivo_via2 = [1, 8, 12, 25]
    archivo_via3 = [2, 7, 14, 18]

    mis_vias = [archivo_via1, archivo_via2, archivo_via3]

    print("Archivos (Vías) de entrada originales:")
    for i, via in enumerate(mis_vias):
        print(f" Vía {i+1}: {via}")

    # Ejecutamos la fusión multivía
    resultado_final = balanced_multiway_merge(mis_vias)

    print("\nArchivo de salida final (Fusionado y Ordenado):")
    print(" ", resultado_final)