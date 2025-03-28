class Stack:
    def __init__(self, array_size):
        self.array_size = array_size  # Tamaño máximo de la pila
        self.top = -1  # Índice del último elemento en la pila (vacío al inicio)
        self.array = [None] * array_size  # Lista para almacenar los valores

    def push(self, value):
        if self.top == self.array_size - 1:
            # Expandir el tamaño del array (doblar el tamaño)
            self.array_size *= 2
            self.array.extend([None] * (self.array_size - len(self.array)))

        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.top > -1:
            value = self.array[self.top]
            self.top -= 1
            return value
        return None  # Retorna None si la pila está vacía

    #Ejemplo de uso:

stack = Stack(5)  # Crear pila con tamaño inicial de 5
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)  # Se expande la pila aquí

print(stack.pop())  
print(stack.pop())
print(stack.array)