import time

class Restaurante:
    def _init_(self):
        self.ordenes = []

class Menu(Restaurante):
    def _init_(self):
        super()._init_()
        self.menu_items = {
            1: {"nombre": "Hamburguesas con papas", "precio": 8.50},
            2: {"nombre": "Tacos de Birria", "precio": 9.00},
            3: {"nombre": "Nachos", "precio": 6.00},
            4: {"nombre": "Bebidas de industria la constancia", "precio": 2.50}
        }

    def mostrar_menu(self):
        print("Menú:")
        for i, item in self.menu_items.items():
            print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")

class Cocina(Restaurante):
    def ver_ordenes_pendientes(self):
        print("Órdenes pendientes:")
        for i, orden in enumerate(self.ordenes):
            print(f"{i+1}. {orden['nombre']}: {', '.join(orden['orden'])}")

    def cocinar_orden(self, orden):
        print(f"Cocinando orden para {orden['nombre']}...")
        time.sleep(2)
        print(f"La orden para {orden['nombre']} está lista.")

class Pedido(Restaurante):
    def _init_(self):
        super()._init_()
        self.menu = Menu()
        self.cocina = Cocina()

    def hacer_orden(self, nombre_cliente, numeros):
        elementos = []
        costo_total = 0
        for num in numeros:
            item = self.menu.menu_items.get(num)
            if item:
                elementos.append(item["nombre"])
                costo_total += item["precio"]
        self.ordenes.append({"nombre": nombre_cliente, "orden": elementos, "costo": costo_total})
        print(f"Se ha registrado la orden para {nombre_cliente} - Total: ${costo_total:.2f}")
        self.cocina.cocinar_orden({"nombre": nombre_cliente, "orden": elementos, "costo": costo_total})

    def entregar_orden(self, nombre_cliente):
        for i, orden in enumerate(self.ordenes):
            if orden["nombre"] == nombre_cliente:
                print(f"Orden para {nombre_cliente}: {', '.join(orden['orden'])} - Total: ${orden['costo']:.2f}")
                del self.ordenes[i]
                return
        print("No se encontró ninguna orden para ese nombre")

# Ejemplo de uso
restaurante = Restaurante()
pedido = Pedido()

for i in range(5):
    pedido.menu.mostrar_menu()
    nombre = input("Ingrese su nombre: ")
    numeros = input("Ingrese el número de los productos que desea separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    pedido.hacer_orden(nombre, numeros)
    pedido.entregar_orden(nombre)
    print("")