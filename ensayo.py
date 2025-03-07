def heapify(arr, n, i, key):
    #Reorganiza la lista desde el indice i para cumplir la propiedad de heap máximo
    largest = i  # Se nicializa el nodo más grande como la raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho
    
    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia valores
        heapify(arr, n, largest, key)  # Llamada recursiva

def heap_sort(lista, key):
    #Ordena una lista utilizando el algoritmo Heap Sort
    n = len(lista)
    
    # Construcción del heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, key)
    
    # Extrae elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0, key)

def merge_sort(lista, key):
    #Ordena una lista utilizando el algoritmo Merge Sort
    if len(lista) > 1:
        mid = len(lista) // 2  # Encuentra el punto medio
        izquierda = lista[:mid]
        derecha = lista[mid:]
        
        merge_sort(izquierda, key)
        merge_sort(derecha, key)
        
        i = j = k = 0  # Índices auxiliares
        
        while i < len(izquierda) and j < len(derecha):
            if key(izquierda[i]) <= key(derecha[j]):
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

def quick_sort(lista, key):
    #Ordena una lista utilizando el algoritmo Quick Sort
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]  # Seleccionamos el pivote
    izquierda = [x for x in lista if key(x) < key(pivote)]
    medio = [x for x in lista if key(x) == key(pivote)]
    derecha = [x for x in lista if key(x) > key(pivote)]
    
    return quick_sort(izquierda, key) + medio + quick_sort(derecha, key)

def busqueda_binaria(lista, valor, key):
    #Realiza una búsqueda binaria en una lista ordenada
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if key(lista[medio]) == valor:
            return medio  # Retorna el índice encontrado
        elif key(lista[medio]) < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Retorna -1 si no se encuentra

class Empleado:
    #Clase que representa un empleado con nombre, edad y salario
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def __repr__(self):
        return f"{self.nombre} | Edad: {self.edad} | Salario: {self.salario}"

# Lista de empleados actualizada
empleados = [
    Empleado("Luis", 32, 4000),
    Empleado("Elena", 27, 2800),
    Empleado("Marta", 28, 3200),
    Empleado("Pedro", 35, 4200),
    Empleado("Carlos", 29, 3000),
    Empleado("Sofía", 30, 3100),
    Empleado("Ana", 25, 3500),
    Empleado("Javier", 26, 3300)
]

# Menú
while True:
    print("\nHola, bienvenido a mi aplicación Empresarial, ¿Qué quieres hacer?:")
    print("1. Ordenar por edad")
    print("2. Ordenar por nombre")
    print("3. Ordenar por salario")
    print("4. Buscar por edad")
    print("5. Buscar por salario")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        heap_sort(empleados, key=lambda e: e.edad)
        print("Lista ordenada por edad:", empleados)
    elif opcion == "2":
        empleados = quick_sort(empleados, key=lambda e: e.nombre)
        print("Lista ordenada por nombre:", empleados)
    elif opcion == "3":
        merge_sort(empleados, key=lambda e: e.salario)
        print("Lista ordenada por salario:", empleados)
    elif opcion == "4":
        edad = int(input("Ingrese la edad a buscar: "))
        heap_sort(empleados, key=lambda e: e.edad)
        indice = busqueda_binaria(empleados, edad, key=lambda e: e.edad)
        print(empleados[indice] if indice != -1 else "Empleado no encontrado")
    elif opcion == "5":
        salario = float(input("Ingrese el salario a buscar: "))
        merge_sort(empleados, key=lambda e: e.salario)
        indice = busqueda_binaria(empleados, salario, key=lambda e: e.salario)
        print(empleados[indice] if indice != -1 else "Empleado no encontrado")
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
