
def calcular_consumo(Productos):
    Resultados = []

    for i in Productos:
        Ingresos = i["Vendido"]*i["Precio"]
        información = {"Nombre":i["Nombre"], "Vendido":i["Vendido"], "Ingresos":i[Ingresos]}
        Resultados.append(información)
        return Resultados


def opcion_3(Productos):
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

["Vendido"] = Vendido
["Cantidad"] -= Vendido

print("Ventas registradas con éxito")

