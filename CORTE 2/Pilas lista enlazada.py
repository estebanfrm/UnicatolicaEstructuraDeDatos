class Node: 
    def __init__(self, value):
        self.value = value #Almacena el valor del nodo
        self.next = None #apunta al siguiente nodo en la pila, inicialmente es None

class Stack:
    def __init__(self):
        self.head = None  # Inicializa la pila vacia, sin nodos

    def push(self, value):
        node = Node(value)  # Crea un nuevo nodo con el valor dado
        node.next = self.head  # Apunta el nuevo nodo al anterior head
        self.head = node  # Actualiza head al nuevo nodo

    def pop(self):
        value = None #se inicializa en None
        if self.head is not None: #Verifica si la pila no esta vacia
            value = self.head.value #guarda el valor del nodo en la cima
            self.head = self.head.next #Mueve la cabeza al siguiente nodo
        return value #Devuelve el valor eliminado

    #Ejemplo de uso:

stack = Stack()  #Crea la pila
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.pop())  #Se llama a la funcion pop
print(stack.pop()) #Se llama a a la funcion pop con nuevo elemento en la cima