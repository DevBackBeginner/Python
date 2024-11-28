def QuickSort(lista):
    # Si la lista tiene 1 o menos elementos, ya está ordenada, por lo que se retorna tal cual.
    if len(lista) <= 1:
        return lista
    
    # Elegimos el primer elemento como pivote
    pivote = lista[0]

    # Inicializamos dos listas vacías, una para los elementos menores al pivote (left) y otra para los mayores (right)
    left = []
    right = []

    # Iteramos sobre el resto de la lista para distribuir los elementos en las listas correspondientes
    for i in range(1, len(lista)):
        # Si el elemento es menor que el pivote, lo agregamos a la lista "left", de lo contrario a "right"
        if lista[i] < pivote:
            left.append(lista[i])
        else:
            right.append(lista[i])

    # Llamamos recursivamente a QuickSort para ordenar las sublistas left y right,
    # y luego combinamos las sublistas con el pivote en el medio.
    return QuickSort(left) + [pivote] + QuickSort(right)

# Lista de números a ordenar
numeros = [100, 2.4, 2.3, 3, 40, 654]

# Llamamos a la función QuickSort con la lista de números
numerosOrdenados = QuickSort(numeros)

# Imprimimos la lista ordenada
print(numerosOrdenados)
