def promedio_notas(notas_estudiantes):
    return {nombre: sum(notas) / len(notas) for nombre, notas in notas_estudiantes}

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
resultado = promedio_notas(notas_estudiantes)
print(resultado)
