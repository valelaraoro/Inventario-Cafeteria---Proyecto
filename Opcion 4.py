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

