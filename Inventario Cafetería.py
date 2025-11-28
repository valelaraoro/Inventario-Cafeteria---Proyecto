print(" ----------MENÚ CAFETERÍA---------- ")

Productos = [{"nombre": "Chilaquiles", "Precio": 25, "Cantidad": 20},
    {"nombre": "Molletes", "Precio": 65, "Cantidad": 15},
    {"nombre": "Pan dulce", "Precio": 15, "Cantidad": 30},
    {"nombre": "Vaso de fruta", "Precio": 40, "Cantidad": 30},
    {"nombre": "Elote en vaso", "Precio": 35, "Cantidad": 15},
    {"nombre": "Nachos con queso", "Precio": 45, "Cantidad": 20}]


def menu():
    print("       MENÚ PRINCIPAL      ")
    print("1. Registrar productos ")
    print("2. Mostrar inventario ")
    print("3. Realizar ventas")
    print("4. Producto mas vendido ")
    print("5. Reporte Final")
    print("6. Salir")

def registrar_productos():
    print("\n--- Registro de productos ---")
    while True:
        try:
            n = int(input("¿Cuántos productos deseas registrar?"))
            break
        except:
          print("Ingresa un número válido")

for i in range(n)
    print(f"\")
#HOla




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



# Lista de productos
Productos = ["Burrito de asado", "Burrito de chicharron", "Chilaquiles", "Pan dulce", "Santa clara chocolate"]

def opcion2():
    print("MENÚ DE PRODUCTOS")
    
    contador = 1
    for producto in Productos:
        print(f"{contador}. {producto}")
        contador += 1

    print("-------------------------\n")




def calcular_consumo(Productos):
    Resultados = []

    for i in Productos:
        Ingresos = i["Vendido"]*i["Precio"]
        información = {"Nombre":i["Nombre"], "Vendido":i["Vendido"], "Ingresos":i[Ingresos]}
        Resultados.append(información)
        return Resultados


def opcion3(Productos):
    if len(Productos) == 0:
        print("Registre productos")
        return
    
    for i in Productos:
        print(f"\nProducto:{i["Nombre"]}")
        print(f"Cantidad Disponible: {i["Cantidad"]}")

while True:
    try:
        Vendido = int(input("Cuántas unidades se vendieron?"))
        if Vendido <= ["Cantidad"] and Vendido >= 0:
            break
        else:
            print("No hay inventario disponible")
    except:
        print("Ingresa un número válido")


print("Ventas registradas con éxito")

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


def opcion4(Productos):
    if len(Productos) == 0:
        print("No hay datos para guardar")
        return 
    resultados = calcular_consumo(Productos)   
    
    try:
        with open("reporte_cafeteria.txt","w") as archivo:
         archivo.write("----Reporte de Cafetería----\n\n")
               
        
        for r in resultados:
            archivo.write(f"{r['nombre']}- Vendido:{r['vendido']} unidades - Ingresos: ${r['Ingresos']}\n")
    except: 
        print("error")





for i in range():


 while True:
     menu()
     Opcion =(input("Selecciona una opción: "))
     if Opcion == "1":
          opcion1()
     elif Opcion == "2":
          opcion2()
     elif Opcion == "3":
          opcion3()
     elif Opcion == "4":
         opcion4()
     elif Opcion == "5":
          opcion4()
    
    
     else:
          print("Opción no válida")