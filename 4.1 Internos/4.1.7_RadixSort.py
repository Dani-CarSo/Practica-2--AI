#7
#RadixSort

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n      # Arreglo de salida que guardará los números ordenados temporalmente
    count = [0] * 10      # Inicializamos los 10 "baldes" (del 0 al 9) para contar los dígitos

    # 1. Contamos cuántas veces aparece cada dígito en la posición actual (exp)
    for i in range(0, n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 2. Cambiamos count[i] para que contenga la posición real de este dígito en el arreglo final
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. Construimos el arreglo de salida colocando los elementos en su lugar correspondiente
    # Se recorre al revés para mantener la estabilidad del algoritmo (crucial en RadixSort)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 4. Copiamos el arreglo de salida a arr, para que arr contenga los números ordenados por este dígito
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontramos el número máximo para saber cuántos dígitos tiene
    max_val = max(arr)

    # Hacemos el ordenamiento por conteo para cada dígito.
    # 'exp' es 1 (unidades), luego 10 (decenas), luego 100 (centenas), etc.
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# --- Bloque de ejecución ---
datos = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(datos)
print("Arreglo ordenado por RadixSort:", datos)