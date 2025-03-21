import time

class RouteNode:
    def __init__(self, location):
        self.location=location
        self.next= None
    # Se define el nodo

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        new_node=RouteNode(location)
        if not self.head: 
            self.head=new_node #si la lista esta vacia, el nuevo nodo se convierte en la cabeza
        else:
            current=self.head
            while current.next:
                current=current.next #recorremos la lista hastas el ultimo nodo desde la variable temporal
            current.next=new_node 
        # TODO Implementar este método

    def show_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta definida.")
            return
        print("🛣️ Ruta definida:")
        while current is not None:
            print(f"➡️ {current.location}")
            current = current.next

    def navigate_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta para navegar.")
            return

        print("🚗 Iniciando recorrido...")

        def show_next_step(node):
            if not node:
                print("🏁 Fin del recorrido.")
                return
            time.sleep(1.5)
            print(f"🛑 Llegaste a: {node.location}")
            show_next_step(node.next)

        show_next_step(current)

        
locations = [
    "Avenida Central", #0 par
    "Calle 5", #1 impar
    "Plaza Mayor", #2 par
    "Avenida del Río", #3 impar
    "Estación Norte", #4 par
    "Parque Sur", #5 impar
    "Museo Nacional", #6 par
    "Teatro Municipal", #7 impar
    "Universidad Central", #8 par
    "Biblioteca Pública" #9 impar
]

if __name__ == "__main__":
    codigo= "407137"
    city_route = Route()
    for i in range(len(locations)):
        if i % 2 == 1:  # Índices impares
            city_route.add_location(locations[i])

    # Agregar rutas de manera iterativa dependiento de si su último número del código es par o impar
    city_route.show_route()

    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()