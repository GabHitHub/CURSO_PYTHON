# Definir los logones disponibles y sus roles asociados
logones_roles = {
    "B959263": "SUPERIOR",
    "C569853": "ADJUNTO",
    "T698952": "TEMPORARIO",
    "Z698563": "TERCERIZADO",
}

# Definir las contraseñas
# Definir los logones disponibles y sus contraseñas correspondientes
logones_contrasenas = {
    "B959263": "CHIPI1971",
    "C569853": "EURASIA",
    "T698952": "JAJAJANT",
    "Z698563": "ECHENME",
}

# Función para realizar el proceso de logueo
def login(logon, password):
    if logon in logones_roles:
        # Verificar la contraseña
        if logones_contrasenas.get(logon) == password:
            return logones_roles[logon]
        else:
            return "Contraseña incorrecta"
    else:
        return "Logon no encontrado"


# Función para verificar los tipos de actos disponibles según el rol
def actos_disponibles(rol):
    permisos_rol = {
        "SUPERIOR": [1, 3, 4],
        "ADJUNTO": [1],
        "TEMPORARIO": [3, 1],
        "TERCERIZADO": [1, 5],
    }

    if rol in permisos_rol:
        return permisos_rol[rol]
    else:
        return []

# Ejemplo de uso
logon = input("Ingrese su logon: ")
password = input("Ingrese su contraseña: ")

rol = login(logon, password)
if rol:
    print(f"Bienvenido, usuario con rol {rol}")
    tipos_actos = actos_disponibles(rol)
    if tipos_actos:
        print(f"Tipos de actos disponibles para su rol: {tipos_actos}")
    else:
        print("No tiene acceso a ningún tipo de acto.")
else:
    print("Logon o contraseña incorrectos")