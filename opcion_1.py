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
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        Productos.append(producto)

    print("\n" \
    "Registro completado correctamente.")

    def mostrar_inventario(Productos):
    if len(Productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n--- Inventario actual ---")
    for p in Productos:
        print(f"{p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


