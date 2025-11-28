print(" ----------MENÚ CAFETERÍA---------- ")

# Inventario inicial de productos
Productos = [
    {"nombre": "Chilaquiles", "precio": 25, "cantidad": 20, "vendido": 0},
    {"nombre": "Molletes", "precio": 65, "cantidad": 15, "vendido": 0},
    {"nombre": "Pan dulce", "precio": 15, "cantidad": 30, "vendido": 0},
    {"nombre": "Vaso de fruta", "precio": 40, "cantidad": 30, "vendido": 0},
    {"nombre": "Elote en vaso", "precio": 35, "cantidad": 15, "vendido": 0},
    {"nombre": "Nachos con queso", "precio": 45, "cantidad": 20, "vendido": 0}
]

# Menú principal
def menu():
    print("\n       MENÚ PRINCIPAL      ")
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Realizar ventas")
    print("4. Producto más vendido")
    print("5. Reporte Final")
    print("6. Salir")

# Registrar productos
def registrar_productos():
    print("\n--- Registro de productos ---")
    while True:
        try:
            n = int(input("¿Cuántos productos deseas registrar? "))
            break
        except:
            print("Ingresa un número válido")

    for i in range(n):
        print(f"\nProducto {i+1}:")
        nombre = input("Nombre: ")

        while True:
            try:
                precio = float(input("Precio: "))
                break
            except:
                print("Ingresa un número válido")

        while True:
            try:
                cantidad = int(input("Cantidad: "))
                break
            except:
                print("Ingresa un número válido")

        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "vendido": 0}
        Productos.append(producto)

    print("\nRegistro completado.")

# Mostrar inventario
def mostrar_inventario():
    if len(Productos) == 0:
        print("\nNo hay productos registrados")
        return

    print("\n--- Inventario ---")
    for i, p in enumerate(Productos, start=1):
        print(f"{i}. {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Vendido: {p['vendido']}")

# Registrar venta
def registrar_venta():
    if len(Productos) == 0:
        print("\nNo hay productos registrados.")
        return

    print("\n--- Registrar venta ---")
    for i, p in enumerate(Productos, start=1):
        print(f"{i}. {p['nombre']} (Stock: {p['cantidad']})")

    while True:
        try:
            opcion = int(input("Selecciona el número del producto: "))
            if 1 <= opcion <= len(Productos):
                break
            else:
                print("Opción inválida.")
        except:
            print("Ingresa un número válido.")

    producto = Productos[opcion-1]

    while True:
        try:
            cantidad = int(input("Cantidad vendida: "))
            if 0 <= cantidad <= producto["cantidad"]:
                break
            else:
                print(f"No hay suficiente stock. Disponible: {producto['cantidad']}")
        except:
            print("Ingresa un número válido.")

    producto["cantidad"] -= cantidad
    producto["vendido"] += cantidad
    print(f"\nVenta registrada: {cantidad} unidades de {producto['nombre']}")

# Producto más vendido
def producto_mas_vendido():
    if len(Productos) == 0:
        print("\nNo hay productos registrados.")
        return

    mas_vendido = max(Productos, key=lambda x: x["vendido"])
    if mas_vendido["vendido"] == 0:
        print("\nAún no se han registrado ventas.")
    else:
        print("\n--- Producto más vendido ---")
        print(f"Nombre: {mas_vendido['nombre']}")
        print(f"Unidades vendidas: {mas_vendido['vendido']}")
        print(f"Ingresos: {mas_vendido['vendido'] * mas_vendido['precio']}")

# Reporte final
def reporte_final():
    if len(Productos) == 0:
        print("\nNo hay productos registrados. No se puede generar reporte final")
        return

    print("\n--- REPORTE FINAL ---")
    total_ventas = 0
    total_ingresos = 0
    mas_vendido = Productos[0]

    for i, p in enumerate(Productos, start=1):
        ingresos = p['vendido'] * p['precio']
        total_ventas += p['vendido']
        total_ingresos += ingresos
        print(f"{i}. {p['nombre']} | Vendido: {p['vendido']} | Inventario restante: {p['cantidad']} | Ingresos: ${ingresos}")

        if p['vendido'] > mas_vendido['vendido']:
            mas_vendido = p

    print("\n--- RESUMEN ---")
    print(f"Total de productos vendidos: {total_ventas}")
    print(f"Ingresos totales: ${total_ingresos}")
    if mas_vendido['vendido'] > 0:
        print(f"Producto más vendido: {mas_vendido['nombre']} ({mas_vendido['vendido']} unidades)")
    else:
        print("Aún no se han registrado ventas.")

# Bucle principal
while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_productos()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        registrar_venta()
    elif opcion == "4":
        producto_mas_vendido()
    elif opcion == "5":
        reporte_final()
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
