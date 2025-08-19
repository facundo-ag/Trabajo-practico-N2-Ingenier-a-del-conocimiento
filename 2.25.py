def analizar_finanzas(**kwargs):
    balance = 0
    print("Resumen financiero:")
    for categoria, monto in kwargs.items():
        print(f"{categoria}: {monto}")
        balance += monto
    print(f"\nBalance final: {balance}")

analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
