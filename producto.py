def pedir_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().upper()
    if nombre == "FIN":
        return "FIN", 0  
    precio = float(input(f"Ingrese el precio unitario de {nombre}: "))
    return nombre, precio