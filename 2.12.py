Productos=[( ("laptop", 1200, 5),
    ("mouse", 25, 50),
    ("teclado", 100, 30))]

def Producto_mas_caro (lista):
    mas_caro= lista[0]
    for n in lista[1:]:
        if n[1]> mas_caro[1]:
            mas_caro=n
    return mas_caro

resultado= Producto_mas_caro(Productos)
print("El pruducto mas caro es:",resultado)