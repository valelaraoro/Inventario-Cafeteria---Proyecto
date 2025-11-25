# Lista de productos de la cafetería
Productos = ["Burrito de asado", "Burrito de chicharron", "Chilaquiles", "Pan dulce", "Santa clara chocolate"]

# Función Opción 2: mostrar productos
def opcion2(Productos):
    print("\nMENÚ DE PRODUCTOS")
    for i, producto in enumerate(Productos, start=1):
        print(f"{i}. {producto}")
