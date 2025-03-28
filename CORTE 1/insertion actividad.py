def InsertionSort(A):
    N = len(A)  # Longitud de elementos
    i = 1  # Comenzamos desde el segundo número

    while i < N:  # Se recorre la lista desde el segundo elemento hasta el último
        current = A[i]  # Se almacena el elemento actual temporalmente
        j = i - 1
        
        while j >= 0 and A[j] > current:  # Se mueve hacia la izquierda si el elemento anterior es mayor que el actual
            A[j + 1] = A[j]  # Se desplaza el elemento hacia la derecha
            j -= 1  # Se define para comparar
        
        A[j + 1] = current  # Se coloca en su posición correcta
        i += 1  # Se pasa al siguiente elemento en la lista

# Arreglo a ordenar
array = [5, 1, 8, 9, 12]

# Se llama a la función InsertionSort
InsertionSort(array)

# Se mprime el arreglo ordenado
print("Arreglo ordenado:", array)