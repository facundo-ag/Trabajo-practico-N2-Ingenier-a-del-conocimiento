
def empleados_con_salario_mayor(empleados, salario_minimo):
    resultado = {}
    for id_empleado, datos in empleados.items():
        nombre, edad, salario = datos  
        if salario > salario_minimo:
            resultado[id_empleado] = datos
    return resultado

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

print(empleados_con_salario_mayor(empleados, 2800))
