class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Inicializa la pila con head como None

    def push(self, value):
        node = Node(value)  # Crea un nuevo nodo con el valor
        node.next = self.head  # Apunta el nuevo nodo al anterior head
        self.head = node  # Actualiza head al nuevo nodo

    def pop(self):
        value = None
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
        return value

    #Ejemplo de uso:

stack = Stack()  #Crea pila con tamaño inicial de 5
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.pop())  #Se llama a la funcion pop
print(stack.pop()) #Se llama a a la funcion pop con nuevo elemento en la cima