
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedio_estudiante(registro, matricula):
    if matricula in registro:  
        notas = registro[matricula]["calificaciones"].values()
        promedio = sum(notas) / len(notas)
        nombre = registro[matricula]["nombre"]
        return f"{nombre} tiene un promedio de {promedio:.2f}"
    else:
        return "Matrícula no encontrada"
print(promedio_estudiante(estudiantes, 101))
print(promedio_estudiante(estudiantes, 102))
