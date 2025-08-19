def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = [f"{clave}={valor}" for clave, valor in kwargs.items()]
    return perfiles

usuarios = ["Ana", "Luis", "María"]
config = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

print(config)
