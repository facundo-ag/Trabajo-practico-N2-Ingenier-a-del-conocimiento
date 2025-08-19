def publicar(usuario, texto, **kwargs):
  
    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": kwargs.get("etiquetas", []),  
        "visibilidad": kwargs.get("visibilidad", "privada"),
        "likes": kwargs.get("likes", 0)
    }
    return publicacion
post = publicar(
    "Juan",
    "Mi primer post!",
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica",
    likes=100
)
print(post)
