print(" ----------MENÚ CAFETERÍA---------- ")
Productos = []


while True:
     try:
          Num_productos = int(input("Cuantós productos se registrarán?"))
          break
     except:
          print("Ingresa un número válido")


def menu():
    print("       MENÚ PRINCIPAL      ")
    print("1. Registrar productos ")
    print("2. Mostrar inventario ")
    print("3. Realizar ventas")
    print("4. Reporte Final")
    print("5. Salir")



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




def opcion3(Productos):


def opcion4():



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
     else:
          print("Opción no válida")