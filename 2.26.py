def registro_empleado(nombre, edad, salario, *args, **kwargs):

    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
        "extra": args,       
    }
    empleado.update(kwargs)
    return empleado

empleado1 = registro_empleado("Ana", 30, 3000, "Ingeniera", "Tiempo completo",
                              direccion="Calle Falsa 123", telefono="123456789")
print(empleado1)
