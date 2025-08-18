
def calcular_promedio(*args):
    if len(args) == 0:  
        return "No se ingresaron notas"
    promedio = sum(args) / len(args)
    return promedio
print("Promedio:", calcular_promedio(85, 90, 78, 92))
