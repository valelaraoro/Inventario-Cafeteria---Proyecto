# -------------------------------------------
# SISTEMA DE INVENTARIO - CAFETERÍA TECMILENIO
# -----------------------------------------------
# Lista de productos
Productos= [
    {"nombre": "Chilaquiles", "precio": 25, "cantidad": 20, "vendido": 0},
    {"nombre": "Molletes", "precio": 65, "cantidad": 15, "vendido": 0},
    {"nombre": "Pan dulce", "precio": 15, "cantidad": 30, "vendido": 0},
    {"nombre": "Vaso de fruta", "precio": 40, "cantidad": 30, "vendido": 0},
    {"nombre": "Elote en vaso", "precio": 35, "cantidad": 15, "vendido": 0},
    {"nombre": "Nachos con queso", "precio": 45, "cantidad": 20, "vendido": 0}
]
# print("Bienvenido a la cafetería")
# Mostrar menú principal
def menu():
    print("\n       MENÚ PRINCIPAL      ")
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Realizar ventas")
    print("4. Producto más vendido")
    print("5. Reporte Final")
    print("6. Salir")
# Opción 1 - Registrar Productos
# def registrar_productos():
# Pedir cantidad de productos a registrarse
# Registrar datos de productos: Nombre, precio, cantidades disponibles y vendidas
# Guardarlos en la lista de Productos

# Opción 2 - Mostrar Inventario
# def mostrar_inventario():
# Mostrar la lista de Productos

# Opción 3: Realizar ventas
# def registrar_venta():
# Mostrar los productos disponibles
# n = int(input("Cuántos productos deseas registrar?"))
# Pedir cantidad vendida
# Actualizar lista de Productos y contador de ventas

# Opción 4 - Producto más vendido
# def producto_mas_vendido():
# Identificar el producto con más ventas y mostrar sus respectivos datos e ingresos generados

# Opción 5 - Reporte Final
#def reporte_final():
# Mostrar resumen general del día (Total vendido, ingresos, inventario restante y producto más vendido)

# Bucle Principal
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
