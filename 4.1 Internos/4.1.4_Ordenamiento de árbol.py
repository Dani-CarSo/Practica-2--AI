#4
#Ordenamiento de árbol

# Primero definimos la estructura de un nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor       # Guarda el número
        self.izquierdo = None    # Conexión al hijo izquierdo (menores)
        self.derecho = None      # Conexión al hijo derecho (mayores)

# Función auxiliar para insertar un número en el árbol siguiendo las reglas
def insertar(raiz, valor):
    # Si el árbol está vacío (o llegamos a un espacio libre), creamos el nodo aquí
    if raiz is None:
        return Nodo(valor)
    
    # Si el valor es menor que la raíz actual, se va hacia la izquierda
    if valor < raiz.valor:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)
    # Si es mayor o igual, se va hacia la derecha
    else:
        raiz.derecho = insertar(raiz.derecho, valor)
        
    return raiz

# Función auxiliar para recorrer el árbol "en orden" (In-order) 
# y meter los números ya ordenados de vuelta en una lista
def recorrer_en_orden(raiz, lista_ordenada):
    if raiz is not None:
        # 1. Vamos lo más a la izquierda posible (los números más chicos)
        recorrer_en_orden(raiz.izquierdo, lista_ordenada)
        
        # 2. Guardamos el valor del nodo actual
        lista_ordenada.append(raiz.valor)
        
        # 3. Vamos hacia la derecha (los números más grandes)
        recorrer_en_orden(raiz.derecho, lista_ordenada)

# FUNCIÓN PRINCIPAL DE TREE SORT 
def ordenamiento_arbol(lista):
    if not lista:
        return lista
        
    # El primer elemento de la lista se convierte en la raíz del árbol
    raiz = Nodo(lista[0])
    
    # Insertamos el resto de los elementos de la lista en el árbol
    for i in range(1, len(lista)):
        insertar(raiz, lista[i])
        
    # Creamos una lista vacía para almacenar el resultado ordenado
    lista_ordenada = []
    
    # Recorremos el árbol para llenar nuestra nueva lista
    recorrer_en_orden(raiz, lista_ordenada)
    
    return lista_ordenada

#  Ejemplo de uso 
mi_lista = [42, 15, 20, 55, 8, 32]
print("Lista original:", mi_lista)

lista_ordenada = ordenamiento_arbol(mi_lista)
print("Lista ordenada:", lista_ordenada)