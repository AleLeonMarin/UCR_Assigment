from datetime import datetime

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Ventas:
    def __init__(self):
        self.productos = []
        self.ventas = []

    def agregar_producto(self):
        codigo = input("Digite el código del producto: ")
        codigo = int(codigo)
        nombre = input("Digite el nombre del producto: ")
        precio = input("Digite el precio del producto: ")
        precio = float(precio)
        cantidad = input("Digite la cantidad en inventario: ")
        cantidad = int(cantidad)

        producto = Producto(codigo, nombre, precio, cantidad)
        self.productos.append(producto)

        print("Producto agregado con éxito.")

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("La lista de productos está vacía.")
        else:
            print("Lista de Productos:")
            for producto in self.productos:
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: ${producto.precio}, Cantidad en Inventario: {producto.cantidad}")

    def registrar_venta(self):
        if not self.productos:
            print("No hay productos disponibles para vender.")
            return

        print("Lista de Productos disponibles para la venta:")
        self.mostrar_productos()

        codigo_producto = input("Digite el código del producto a comprar: ")
        cantidad_comprar = int(input("Digite la cantidad que desea comprar: "))

        for producto in self.productos:
            if producto.codigo == codigo_producto:
                if producto.cantidad >= cantidad_comprar:
                    producto.cantidad -= cantidad_comprar
                    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.ventas.append({
                        "Código": codigo_producto,
                        "Cantidad Vendida": cantidad_comprar,
                        "Total": cantidad_comprar * producto.precio,
                        "Fecha": fecha_venta
                    })
                    print(f"Venta registrada con éxito. Total: ${cantidad_comprar * producto.precio}")
                else:
                    print("No hay suficiente inventario para completar la venta.")
                return

        print("El producto con ese código no fue encontrado.")

    # Resto de métodos de la clase Ventas aquí

    def calcular_promedio_ventas(self):
        if not self.ventas:
            return 0.0
        total_ventas = sum(venta["Total"] for venta in self.ventas)
        return total_ventas / len(self.ventas)

    def mostrar_estadisticas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
        else:
            print("\nEstadísticas:")
            promedio_ventas = self.calcular_promedio_ventas()
            print(f"a. Promedio de Ventas: ${promedio_ventas:.2f}")

            self.mostrar_precio_mas_caro()
            self.mostrar_precio_mas_barato()
            self.mostrar_ventas_del_mes()
            self.mostrar_productos_escasos()

    def mostrar_precio_mas_caro(self):
        precios = [producto.precio for producto in self.productos]
        precio_mas_caro = max(precios)
        print(f"b. Precio más Caro: ${precio_mas_caro:.2f}")

    def mostrar_precio_mas_barato(self):
        precios = [producto.precio for producto in self.productos]
        precio_mas_barato = min(precios)
        print(f"c. Precio más Barato: ${precio_mas_barato:.2f}")

    def mostrar_ventas_del_mes(self):
        mes_actual = datetime.now().month
        ventas_mes_actual = [venta for venta in self.ventas if int(venta['Fecha'].split('-')[1]) == mes_actual]
        total_ventas_mes = sum(venta["Total"] for venta in ventas_mes_actual)
        print(f"d. Ventas del Mes: ${total_ventas_mes:.2f}")

    def mostrar_productos_escasos(self):
        productos_escasos = [producto for producto in self.productos if producto.cantidad < 5]
        if productos_escasos:
            print("e. Productos Escasos:")
            for producto in productos_escasos:
                print(
                    f"Código: {producto.codigo}, Nombre: {producto.nombre}, Cantidad en Inventario: {producto.cantidad}")


# Main
ventas_sistema = Ventas()

while True:
    print("\n--- Sistema de Ventas ---")
    print("1. Agregar producto")
    print("2. Registrar venta")
    print("3. Reportes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ventas_sistema.agregar_producto()
    elif opcion == "2":
        ventas_sistema.registrar_venta()
    elif opcion == "3":
        print("\n--- Reportes ---")
        print("a. Mostrar Promedio de Ventas")
        print("b. Mostrar Precio más Caro")
        print("c. Mostrar Precio más Barato")
        print("d. Mostrar Ventas del Mes")
        print("e. Mostrar Productos Escasos")
        opcion_reporte = input("Seleccione una opción de reporte: ")
        if opcion_reporte == "a":
            ventas_sistema.calcular_promedio_ventas
        elif opcion_reporte == "b":
            ventas_sistema.mostrar_precio_mas_caro()  # Llama a la función para mostrar el precio más caro
        elif opcion_reporte == "c":
            ventas_sistema.mostrar_precio_mas_barato # Llama a la función para mostrar el precio más barato
        elif opcion_reporte == "d":
           ventas_sistema.mostrar_ventas_del_mes()
        elif opcion_reporte == "e":
            ventas_sistema.mostrar_productos_escasos # Llama a la función para mostrar productos escasos
        else:
            print("Opción de reporte no válida.")
    elif opcion == "4":
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
