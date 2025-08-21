def analizar_tendencias(hashtags, tendencias, umbral):
    hashtags_tendencia = []
    
    for hashtag, frecuencia in tendencias:
        if frecuencia > umbral:
            hashtags_tendencia.append(hashtag)
    
    return hashtags_tendencia

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

resultado = analizar_tendencias(hashtags, tendencias, umbral=100)
print(resultado)
