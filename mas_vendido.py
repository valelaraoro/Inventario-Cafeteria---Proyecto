def producto_con_mayor_inventario(Productos):
    if len(Productos) == 0:
        print("No hay productos registrados.")
        return

    mayor = Productos[0]

    for p in Productos:
        if p["cantidad"] > mayor["cantidad"]:
            mayor = p

    print("\n--- Producto con mayor inventario ---")
    print(f"Nombre: {mayor['nombre']}")
    print(f"Cantidad: {mayor['cantidad']}")
    print(f"Precio: {mayor['precio']}")