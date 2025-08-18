
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analizar_temperaturas(datos):
    media = sum(datos) / len(datos)   
    maxima = max(datos)               
    minima = min(datos)               
    return media, maxima, minima

media, maxima, minima = analizar_temperaturas(temperaturas)

print(f"Temperatura media: {media:.2f}°C")
print(f"Temperatura máxima: {maxima}°C")
print(f"Temperatura mínima: {minima}°C")
