# Función que recibe configuraciones opcionales con **kwargs
def configurar_app(**kwargs):
    # Diccionario por defecto
    configuraciones = {
        "modo_oscuro": False,
        "idioma": "en",
        "notificaciones": True
    }
    
    # Actualizar con las opciones recibidas
    configuraciones.update(kwargs)
    
    return configuraciones


# Ejemplo de uso
app_config = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print(app_config)
