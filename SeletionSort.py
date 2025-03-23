def SelectionSort(arr):
    N = len(arr)  # Longitud de la lista
    i = 0  # Comenzamos desde la primera posición
    while i < N - 1:  # Se recorre la lista hasta el penúltimo elemento
        min_idx = i  # el elemento actual es el mínimo
        j = i + 1  # Se compara con el siguiente elemento
        while j < N:  # Busca el elemento más pequeño en el resto de la lista
            if arr[j]["code"] < arr[min_idx]["code"]:  # Si encuentra un código más pequeño
                min_idx = j  # Se actualiza el índice del mínimo
            j += 1  # iguiente elemento
        # Intercamba el elemento actual con el mínimo encontrado
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        i += 1  #siguiente elemento

# Lista de personas con nombre y código
personas = [
    {"name": "Felipe", "code": 10},
    {"name": "Carlos", "code": 6},
    {"name": "Isabella", "code": 7},
    {"name": "Juan", "code": 4},
    {"name": "Andrés", "code": 8},
    {"name": "Valentina", "code": 5},
    {"name": "Sofía", "code": 3},
    {"name": "Daniel", "code": 2},
    {"name": "Mariana", "code": 9},
    {"name": "Camila", "code": 1}
]

# Llamamos a la función SelectionSort para ordenar la lista
SelectionSort(personas)

# Imprimimos el resultado ordenado
for item in personas:
    print(item)