#4
#Polyphase sort

import heapq

def polyphase_sort(cinta1, cinta2):
    # Simulamos que cinta1 y cinta2 ya tienen bloques distribuidos en base a Fibonacci.
    # Cada sublista interna representa un bloque ('run') ya ordenado.
    t1 = cinta1  # Cinta de entrada 1
    t2 = cinta2  # Cinta de entrada 2
    t3 = []  # Cinta de salida (vacía al inicio)

    print("--- Distribución Inicial de Cintas ---")
    print(f"Cinta 1 ({len(t1)} bloques): {t1}")
    print(f"Cinta 2 ({len(t2)} bloques): {t2}")
    print(f"Cinta 3 ({len(t3)} bloques): {t3}\n")

    pasada = 1

    # El proceso continúa hasta que solo quede un bloque en total entre todas las cintas
    while (len(t1) + len(t2) + len(t3)) > 1:
        # Identificar cuál es la cinta vacía (salida) y cuáles son las de entrada
        if not t1:
            entrada_a, entrada_b, salida = t2, t3, t1
            nombre_salida = "Cinta 1"
        elif not t2:
            entrada_a, entrada_b, salida = t1, t3, t2
            nombre_salida = "Cinta 2"
        else:
            entrada_a, entrada_b, salida = t1, t2, t3
            nombre_salida = "Cinta 3"

        # Fusionamos bloques uno a uno hasta que una de las dos entradas se agote
        while entrada_a and entrada_b:
            bloque_a = entrada_a.pop(0)
            bloque_b = entrada_b.pop(0)

            # Fusionamos los dos bloques ordenados utilizando un min-heap rápido
            bloque_fusionado = list(heapq.merge(bloque_a, bloque_b))
            salida.append(bloque_fusionado)

        print(f"--- Fin de la Pasada {pasada} (Salida hacia {nombre_salida}) ---")
        print(f"Cinta 1: {t1}")
        print(f"Cinta 2: {t2}")
        print(f"Cinta 3: {t3}\n")
        pasada += 1

    # Retornamos la única cinta que se quedó con el bloque final completamente ordenado
    return t1[0] if t1 else (t2[0] if t2 else t3[0])


#  Ejemplo de Uso 
if __name__ == "__main__":
    # Distribución perfecta de Fibonacci: 3 bloques en Cinta 1, 2 bloques en Cinta 2
    cinta_inicial_1 = [[10, 25], [3, 9], [6, 18]]  # 3 bloques
    cinta_inicial_2 = [[1, 12], [2, 15]]  # 2 bloques

    resultado = polyphase_sort(cinta_inicial_1, cinta_inicial_2)
    print("Resultado Final Ordenado:", resultado)