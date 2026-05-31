#5
#Distribution of initial runs

def distribuir_tramos_iniciales(archivo_gigante, capacidad_ram, num_vias):
    # Creamos una lista de listas vacías para simular nuestros archivos temporales en el disco.
    vias = [[] for _ in range(num_vias)]

    i = 0  # Inicializamos el puntero para saber en qué posición del archivo gigante estamos leyendo.
    via_actual = 0  # Inicializamos el selector de vía; empezaremos guardando en la primera vía (índice 0).
    total_elementos = (
        len(archivo_gigante)
    )  # Guardamos la cantidad total de elementos que tiene el archivo gigante.

    # Iniciamos un bucle que recorrerá todo el archivo gigante paso a paso.
    while i < total_elementos:

        # --- FASE 1: Cargar y Ordenar en RAM ---
        # Extraemos un fragmento del archivo gigante que sea del tamaño máximo que soporta nuestra RAM.
        bloque_ram = archivo_gigante[i : i + capacidad_ram]

        # Ordenamos los elementos de ese fragmento internamente en la memoria RAM (esto crea un "run" o tramo).
        bloque_ram.sort()

        # --- FASE 2: Distribución en Archivos Temporales ---
        # Guardamos el tramo ya ordenado en el archivo temporal (vía) que le corresponde en este turno.
        vias[via_actual].append(bloque_ram)

        # Avanzamos nuestro puntero principal para leer el siguiente bloque del archivo gigante en la próxima vuelta.
        i += capacidad_ram

        # Cambiamos a la siguiente vía usando el operador residuo (%), logrando un reparto equitativo tipo Round-Robin (0, 1, 0, 1...).
        via_actual = (via_actual + 1) % num_vias

    # Una vez procesado todo el archivo, devolvemos las vías con todos los tramos iniciales distribuidos.
    return vias


# --- Bloque de ejecución principal para probar el código ---
if __name__ == "__main__":
    # Definimos una lista desordenada que simula ser un archivo masivo almacenado en el disco duro.
    archivo_en_disco = [40, 12, 5, 88, 23, 7, 1, 99, 4, 15]

    CAPACIDAD_RAM = 3  # Restricción: Nuestra memoria RAM simulada solo puede procesar un máximo de 3 números a la vez.
    NUM_VIAS = 2  # Restricción: Contamos con 2 archivos temporales de entrada para distribuir los datos.

    # Imprimimos en la consola el estado original del archivo gigante antes de ser procesado.
    print("Archivo gigante original en disco:", archivo_en_disco, "\n")

    # Llamamos a la función pasándole el archivo, el límite de la RAM y la cantidad de vías disponibles.
    resultado_vias = distribuir_tramos_iniciales(
        archivo_en_disco, CAPACIDAD_RAM, NUM_VIAS
    )

    # Imprimimos el encabezado para mostrar cómo quedaron los archivos temporales en el disco duro simulado.
    print("\nResultado de los archivos temporales listos para el Merge:")

    # Recorremos cada una de las vías generadas para mostrar su contenido de forma ordenada en la consola.
    for indice, via in enumerate(resultado_vias):
        # Mostramos el número de vía (ajustado a base 1 para humanos) y los tramos ordenados que recibió.
        print(f" Archivo/Vía {indice + 1}: {via}")