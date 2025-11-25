print(" ----------MENÚ CAFETERÍA---------- ")
Productos = []

# Pedir cuántos productos se registrarán
while True:
    try:
        Num_productos = int(input("¿Cuántos productos se registrarán? "))
        break
    except:
        print("Ingresa un número válido.")


def menu():
    print("\n       MENÚ PRINCIPAL      ")
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Realizar ventas")
    print("4. Reporte Final")
    print("5. Salir")


# ---------------------------
#   OPCIÓN 1: Registrar productos
# ---------------------------
def opcion1(Productos):
    print("\n----- Registro de productos -----")

    for i in range(Num_productos):
        print(f"\nProducto {i+1}:") 
        
        nombre = input("Nombre del producto: ").strip()

        # Precio
        while True:
            try:
                precio = float(input("Precio por unidad: "))
                break
            except:
                print("Ingresa un número válido.")

        # Cantidad
        while True:
            try:
                cantidad = int(input("Cantidad disponible: "))
                break
            except:
                print("Ingresa un número entero válido.")

        producto = {
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad,
            "Vendido": 0
        }

        Productos.append(producto)

    print("\nRegistro completado correctamente.")


# ---------------------------
#   OPCIÓN 2: Mostrar inventario
# ---------------------------
Productos = ["Burrito de asado", "Burrito de chicharron", "Chilaquiles", "Pan dulce", "Santa clara chocolate"]

def opcion2():
    print("MENÚ DE PRODUCTOS")
    
    contador = 1
    for producto in Productos:
        print(f"{contador}. {producto}")
        contador += 1

    print("-------------------------\n")

# ---------------------------
#   OPCIÓN 3: Registrar ventas
# ---------------------------
def opcion3(Productos):
    if len(Productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n----- Registrar Venta -----")

    for i, p in enumerate(Productos):
        print(f"{i+1}. {p['Nombre']} (Disponible: {p['Cantidad']})")

    while True:
        try:
            opc = int(input("Selecciona un producto: ")) - 1
            if 0 <= opc < len(Productos):
                break
            else:
                print("Producto no válido.")
        except:
            print("Ingresa un número válido.")

    producto = Productos[opc]

    while True:
        try:
            vendido = int(input("¿Cuántas unidades se vendieron? "))
            if 0 <= vendido <= producto["Cantidad"]:
                break
            else:
                print("Cantidad no válida.")
        except:
            print("Ingresa un número entero válido.")

    producto["Cantidad"] -= vendido
    producto["Vendido"] += vendido

    print("Venta registrada con éxito.")


# ---------------------------
#   Cálculo de ingresos
# ---------------------------
def calcular_consumo(Productos):
    Resultados = []

    for p in Productos:
        ingresos = p["Vendido"] * p["Precio"]
        info = {
            "Nombre": p["Nombre"],
            "Vendido": p["Vendido"],
            "Ingresos": ingresos
        }
        Resultados.append(info)

    return Resultados


# ---------------------------
#   OPCIÓN 4: Reporte final
# ---------------------------
def opcion4(Productos):
    if len(Productos) == 0:
        print("No hay datos para guardar.")
        return 

    resultados = calcular_consumo(Productos)

    try:
        with open("reporte_cafeteria.txt", "w") as archivo:
            archivo.write("---- Reporte de Cafetería ----\n\n")

            for r in resultados:
                archivo.write(
                    f"{r['Nombre']} - Vendido: {r['Vendido']} unidades - Ingresos: ${r['Ingresos']}\n"
                )

        print("Reporte generado exitosamente en 'reporte_cafeteria.txt'")
    except:
        print("Error al guardar el archivo.")


# ---------------------------
#   BUCLE PRINCIPAL
# ---------------------------
while True:
    menu()
    Opcion = input("Selecciona una opción: ")

    if Opcion == "1":
        opcion1(Productos)
    elif Opcion == "2":
        opcion2()
    elif Opcion == "3":
        opcion3(Productos)
    elif Opcion == "4":
        opcion4(Productos)
    elif Opcion == "5":
        print("Saliendo del sistema... ¡Gracias!")
        break
    else:
        print("Opción no válida.")
