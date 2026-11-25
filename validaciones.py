
# Comprueba que el DNI no esté vacío.
def validar_dni(dni: str) -> bool:
    """
    Verifica que el DNI ingresado no esté vacío ni compuesto por
    algun caracter que no sea numérico.

    Args:
        dni (str): DNI ingresado por el usuario.

    Returns:
        bool: True si el DNI no está vacío, False en caso contrario.
    """
    if dni == "":
        return False

    for i in range(len(dni)):
        caracter = dni[i]

        if caracter < "0" or caracter > "9":
            return False

    return True


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
    Verifica que el nombre no esté vacío ni contenga números.

    Args:
        nombre (str): Nombre o apellido ingresado.

    Returns:
        bool: True si el nombre es válido.
    """

    if nombre == "":
        return False

    for i in range(len(nombre)):
        caracter = nombre[i]

        if caracter >= "0" and caracter <= "9":
            return False

    return True



# Comprueba que la edad sea mayor o igual a cero.

def validar_edad(edad: str) -> bool:
    """
    Verifica que la edad sea numérica y no sea negativa.

    Args:
        edad (str): Edad ingresada por el usuario.

    Returns:
        bool: True si la edad es válida.
    """

    if edad == "":
        return False

    for i in range(len(edad)):
        caracter = edad[i]

        if caracter < "0" or caracter > "9":
            return False

    return True



# Comprueba que la nota esté dentro del rango permitido.

def validar_nota(nota: str) -> bool:
    """
    Verifica que la nota sea numérica y esté entre 0 y 10.

    Args:
        nota (str): Nota ingresada por el usuario.

    Returns:
        bool: True si la nota es válida.
    """

    if nota == "":
        return False

    for i in range(len(nota)):
        caracter = nota[i]

        if caracter < "0" or caracter > "9":
            return False

    nota = int(nota)

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
