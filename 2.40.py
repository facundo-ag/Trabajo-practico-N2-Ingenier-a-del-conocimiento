def ranking_estudiantes(estudiantes):
    promedios = {}
    
    for id_estudiante, materias in estudiantes.items():
       
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas)
 
        promedio = sum(todas_notas) / len(todas_notas)
        promedios[id_estudiante] = promedio
    
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultado = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes:", resultado)
