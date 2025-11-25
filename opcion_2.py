print(" ----------MENÚ CAFETERÍA---------- ")

# Aquí estará la lista de productos
Productos = ["Burrito de asado", "Burrito de chicharron", "Chilaquiles", "Pan dulce", "Santa clara chocolate"]

def menu():
    print("\n       MENÚ PRINCIPAL      ")
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Realizar ventas")
    print("4. Reporte Final")
    print("5. Salir")

# -------------------------
#        OPCIÓN 2
# -------------------------
def opcion2():
    print("\n--- MENÚ DE PRODUCTOS ---")
    
    contador = 1
    for producto in Productos:
        print(f"{contador}. {producto}")
        contador += 1

    print("-------------------------\n")


# Bucle principal
while True:
    menu()
    Opcion = input("Selecciona una opción: ")

    if Opcion == "1":
        print("Opción 1 aún no programada")
    elif Opcion == "2":
        opcion2()
    elif Opcion == "3":
        print("Opción 3 aún no programada")
    elif Opcion == "4":
        print("Opción 4 aún no programada")
    elif Opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida")
