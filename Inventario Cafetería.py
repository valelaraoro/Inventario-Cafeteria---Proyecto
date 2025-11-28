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

for i in range(n):
    print(f"\nProducto{i+1}:")
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

    def mostrar_inventario():
        if len(Productos) == 0:
            print("\nNo hay productos registrados")
            return
        print("\n--- Inventario ---")
        i = 1 
        for p in Productos:
            print(f"{i}. {p['nombre']}| Precio: {p['precio']} | Cantidad: {p['cantidad']} | Vendido: {p['vendido']})")
            i += 1
    
    def registrar_venta():
        if len(Productos) == 0:
            print("\nNo hay productos registrados.")
            return
        print("\n--- Registrar venta ---")
        i = 1
        for p in Productos:
            print(f"{i}. {p['nombre']} (Stock: {p['cantidad']})")
            i += 1

        while True:
            try:
                opcion = int(input("Selecciona el número del producto: "))
                if 1 <= opcion <= len(Productos):
                    break
                else:
                    print("Oppción Inválida.")
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
                print("Ingresa un número válido")
                 
                producto["cantidad"] -= cantidad
                producto["vendido"] += cantidad
    print(f"\nVenta registrada: {cantidad} unidades de {producto['nombre']}")

    def producto_mas_vendido():
        if len(Productos) == 0:
            print("\nNo hay productos registrados.")
            return
        
        mas_vendido = Productos[0]
        for p in Productos:
            if p["vendido"] > mas_vendido["vendido"]:
                mas_vendido = p
            if mas_vendido["vendido"]== 0:
                print("\nAún no se han registrado ventas.")
            else:
                print("\n--- Producto más vendido ---")
                print(f"Nombre: {mas_vendido['nombre']}")
                print(f"Unidades vendidas: {mas_vendido['vendido']}")
                print(f"Ingresos: {mas_vendido['vendido'] * mas_vendido['precio']}")
        
        def reporte_final():
            if len(Productos)== 0:
                print("\nNo hay productos registrados. No se puede generar reporte final")
                return
            print("\n--- REPORTE FINAL ---")
            total_ventas = 0
            total_ingresos = 0
            mas_vendido = Productos [0]

        i = 1
        for p in Productos:
                ingresos = p['vendido'] * p['precio']
                total_ventas += p['vendido']
                total_ingresos += ingresos
                print(f"{i}. {p['nombre']} | Vendido: {p['vendido']} | inventario restante: {p['cantidad']} | Ingresos: ${ingresos}")
                
                if p['vendido'] > mas_vendido['vendido']:
                    mas_vendido = p
                i += 1
                print("\n--- RESUMEN ---")
                print(f"Total de productos vendidos: {total_ventas}")
                print(f"Ingresos totales: ${total_ingresos}")
                if mas_vendido['vendido']> 0:
                    print(f"Producto más vendido: {mas_vendido['nombre']}({mas_vendido['vendido']} unidades)")
                else:
                    print("Aún no se han registrado ventas.")
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