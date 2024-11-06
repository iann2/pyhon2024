from producto import pedir_producto
from cantidad import pedir_cantidad
from calculo import calcular_total

def main():
    productos = {}

    while True:
        nombre, precio = pedir_producto()
        if nombre == "FIN":
            break
        cantidad = pedir_cantidad(nombre)
        productos[nombre] = {'precio': precio, 'cantidad': cantidad}
    
    calcular_total(productos)

if __name__ == "__main__":
    main()