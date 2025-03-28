personas = [ #el listado con nombre y codigo
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


def InsertionSort(A):
    N = len(A) #longitud de elementos
    i=1 #comenzamos desde el segundo numero

    while i<N: #se recorre la lista desde el segundo elemento hasta el ultimo
        current = A[i] #se almacena el elemento actual temporalmente
        j = i-1
        
        while j >= 0 and A[j]["code"] > current["code"]: #Se mueve hacia la izquierda si el elemento anterior es mayor que el actual 
            A[j+1]=A[j] # Se desplaza el elemento hacia la derecha
            j -= 1 #se define para comparar
        
        A[j+1]=current # Se coloca en su posición correcta
        i += 1 # Se pasa al siguiente elemento en la lista

InsertionSort(personas) #se llama a la funcion creada
print("Arreglo ordenado:", personas) #se imprime en orden
