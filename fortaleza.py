def clasificar_fortaleza(puntaje):
    umbral = 8  # alerta: contraseña debil
    return "Fuerte" if puntaje >= umbral else "Debil"