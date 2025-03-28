class Stack: # clase stack
    def __init__(self, array_size):
        self.array_size = array_size  # Tamaño maximo de la pila
        self.top = -1  # indice del último elemento en la pila (vacío al inicio)
        self.array = [None] * array_size  # Lista para almacenar los valores

    def push(self, value):
        if self.top == self.array_size - 1: #Comprueba si la pila esta llena
            #Expandir el tamaño del array (doblar el tamaño) si esta llena
            self.array_size *= 2
            self.array.extend([None] * (self.array_size - len(self.array))) #Expande agregando None

        self.top += 1 #mueve top una posicion arriba
        self.array[self.top] = value #guarda el nuevo valor en la posicion self.top

    def pop(self):
        if self.top > -1: #verifica que la pila no esta vacia
            value = self.array[self.top] #el valor que esta en la cima se guarda en value
            self.top -= 1 #mueve top una posicion hacia abajo
            return value #Devuelve el valor eliminado
        return None  # Retorna None si la pila está vacía

#Ejemplo de uso:
stack = Stack(5)  #Crea pila con tamaño inicial de 5
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)  # Se expande la pila aquí

print(stack.pop())  #Se llama a la funcion pop
print(stack.pop()) #Se llama a a la funcion pop con nuevo elemento en la cima
print(stack.array) #Imprime todo el array