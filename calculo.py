def calcular_total(productos):
    total_general = 0
    print("\nResumen de la compra:")
    for nombre, datos in productos.items():
        total_producto = datos['precio'] * datos['cantidad']
        total_general += total_producto
        print(f"{nombre}: {datos['cantidad']} unidades x ${datos['precio']} = ${total_producto}")
    
    print(f"\nTotal general: ${total_general}")
    return total_general