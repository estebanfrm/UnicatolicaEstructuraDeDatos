def BubbleSort(arr):
    N=len(arr) #longitud de la lista
    i=0 #se comienza desde la primera posicion
    while i<N-1: #recorre la lista hasta el penultimo elemento
        j=0
        while j<N-i-1: #compara los elementos de al lado
            if arr[j]["code"] > arr[j+1]["code"]: #si el codigo es mayor que el del siguiente, lo intercambia
                temp = arr[j] #almacena temporalmente
                arr[j] = arr[j+1] #mueve el siguiente elemento a la posicion actual
                arr[j+1]= temp #coloca el elemento temporal en la posicion siguiente
            j += 1 #cada vez que se ejecute este while, se incrementa j
        i +=1 #cada vez que se ejecute este while, se incrementa i

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

BubbleSort(personas) #se llama a la funcion creada

for item in personas:
    print(item) #imprime el resultado ordenado
