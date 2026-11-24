
# Comprueba que el DNI no esté vacío.
def validar_dni(dni: str) -> bool:
    """
    Verifica que el DNI ingresado no esté vacío.

    Args:
        dni (str): DNI ingresado por el usuario.

    Returns:
        bool: True si el DNI no está vacío, False en caso contrario.
    """
    if dni != "":
        return True
    else:
        return False


# Comprueba que el DNI todavía no esté registrado.
def validar_dni_unico(dni: str, alumnos: dict) -> bool:
    """
    Verifica que el DNI no exista en el diccionario de alumnos.

    Args:
        dni (str): DNI que se desea registrar.
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        bool: True si el DNI es único, False si ya existe.
    """
    if dni in alumnos:
        return False
    else:
        return True


# Comprueba que el DNI pertenezca a un alumno registrado.
def validar_dni_existente(dni: str, alumnos: dict) -> bool:
    """
    Verifica que el DNI exista en el diccionario de alumnos.

    Args:
        dni (str): DNI que se desea buscar.
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        bool: True si el DNI existe, False en caso contrario.
    """
    if dni in alumnos:
        return True
    else:
        return False


# Comprueba que el nombre o apellido no esté vacío.
def validar_nombre(nombre: str) -> bool:
    """
    Verifica que el nombre o apellido no esté vacío.

    Args:
        nombre (str): Nombre o apellido ingresado.

    Returns:
        bool: True si el campo no está vacío, False en caso contrario.
    """
    if nombre != "":
        return True
    else:
        return False


# Comprueba que la edad sea mayor o igual a cero.
def validar_edad(edad: int) -> bool:
    """
    Verifica que la edad no sea negativa.

    Args:
        edad (int): Edad ingresada por el usuario.

    Returns:
        bool: True si la edad es válida, False en caso contrario.
    """
    if edad >= 0:
        return True
    else:
        return False


# Comprueba que la nota esté dentro del rango permitido.
def validar_nota(nota: int) -> bool:
    """
    Verifica que la nota esté entre 0 y 10.

    Args:
        nota (int): Nota final ingresada por el usuario.

    Returns:
        bool: True si la nota es válida, False en caso contrario.
    """
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False


# Comprueba que la opción elegida para modificar sea válida.
def validar_opcion_modificacion(opcion: str) -> bool:
    """
    Verifica que la opción ingresada sea del 1 al 4.

    Args:
        opcion (str): Opción elegida por el usuario.

    Returns:
        bool: True si la opción es válida, False en caso contrario.
    """
    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        return True
    else:
        return False
