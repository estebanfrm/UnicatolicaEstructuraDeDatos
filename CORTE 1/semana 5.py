class LinkedListNode:
    def __init__(self, value):
        self.value = value # Valor almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo en la lista

def linked_list_lookup(head, element_number):
    current = head  # Apunta al primer nodo de la lista
    count = 0  # Contador para llevar la cuenta de los nodos recorridos

    # Iteramos a través de la lista hasta encontrar la posición deseada o llegar al final
    while count < element_number and current is not None:
        current = current.next  # Avanzamos al siguiente nodo
        count += 1

    return current  # Retornamos el nodo encontrado o None si la posición no existe

# Se crean los nodos
node1 = LinkedListNode(10)
node2 = LinkedListNode(20)
node3 = LinkedListNode(30)
node4 = LinkedListNode(40)
node5 = LinkedListNode(50)

# Se enlazan los nodos
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#cabeza de la lista
head = node1

element_number = 2 #buscamos el elemento en la posicion 2


result= linked_list_lookup(head, element_number)
if result is not None:
    print(f"El valor en la posicion {element_number} es: {result.value})") #imprimir la busqueda
else:
    print(f"No se encontró un nodo en la posición {element_number}")