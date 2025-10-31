#------------MONITOREO DE INVENTARIO DE CAFETERÍA-------------
#----------------MENÚ DE CAFETERÍA-----------------------
#----------------------------------------------------------
# print("bienvenido a a cafeteria")
# num_pedido =print("este es el menu: \n burrito\n chilaquiles \n molletes\n")

# burrito = 30
# chilaquiles = 10
# molletes = 10
# num_pedido = (input("que le gustaria ordenar: "))
# print ("esto ordeno:", num_pedido)
# if num_pedido == "burrito":
#     print ("hay 30 burritos en existencias")
# elif num_pedido == "chilaquiles":
#     print("hay 10 chilaquiles en existencia")
# elif num_pedido == "molletes":
#     print("hay 15 molletes en existencias")

# =====================================
# SISTEMA DE INVENTARIO - CAFETERÍA UNIVERSITARIA
# =====================================

print("Bienvenido a la cafetería")
print("Por favor, registre los productos del menú.")

# Paso 1: Registrar productos
num_productos = int(input("¿Cuántos productos tendrá el menú hoy? "))

inventario = {}   # {nombre: cantidad}

for i in range(num_productos):
    print(f"\n--- Registro del producto {i+1} ---")
    nombre = input("Nombre del producto: ").strip().lower()
    cantidad = int(input("Cantidad disponible: "))
    inventario[nombre] = cantidad

# Paso 2: Mostrar menú
print("\n=== MENÚ DISPONIBLE ===")
for producto in inventario:
    print(f"{producto.title()} - {inventario[producto]} disponibles")

# Paso 3: Consultar productos
while True:
    print("\n¿Deseas consultar un producto?")
    print("1. Sí")
    print("2. No (ver reporte final)")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        pedido = input("¿Qué producto deseas consultar?: ").strip().lower()

        if pedido in inventario:
            existencia = inventario[pedido]

            if existencia == 0:
                print("Ese producto no está disponible.")
            elif existencia <= 3:
                print(f"Quedan pocas unidades de {pedido} ({existencia} restantes).")
            else:
                print(f"Hay {existencia} unidades disponibles de {pedido}.")
        else:
            print("Ese producto no está en el menú.")
    elif opcion == "2":
        break
    else:
        print("Opción no válida, intenta de nuevo.")

# Paso 4: Reporte final
print("\n=== REPORTE FINAL ===")
for producto in inventario:
    existencia = inventario[producto]
    if existencia == 0:
        estado = "AGOTADO"
    elif existencia <= 3:
        estado = "POR AGOTARSE"
    else:
        estado = "DISPONIBLE"
    print(f"{producto.title()}: {estado} ({existencia} restantes)")

print("Gracias por usar el sistema de la cafetería.")
