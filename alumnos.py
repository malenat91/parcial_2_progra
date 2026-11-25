
from validaciones import (
    validar_dni,
    validar_dni_unico,
    validar_dni_existente,
    validar_nombre,
    validar_edad,
    validar_nota,
    validar_opcion_modificacion
)


# Solicita un DNI y comprueba que no esté vacío ni registrado.
def pedir_dni_nuevo(alumnos: dict) -> str:
    """
    Solicita un DNI y verifica que no esté registrado.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        str: DNI ingresado por el usuario.
    """
    dni = input("Ingrese el DNI del alumno: ")

    while validar_dni(dni) == False or validar_dni_unico(dni, alumnos) == False:
        print("DNI inválido o ya registrado.")
        dni = input("Ingrese el DNI del alumno: ")

    return dni


# Solicita un DNI y comprueba que corresponda a un alumno registrado.
def pedir_dni_existente(alumnos: dict) -> str:
    """
    Solicita un DNI y verifica que pertenezca a un alumno registrado.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        str: DNI ingresado por el usuario.
    """
    dni = input("Ingrese el DNI del alumno: ")

    while validar_dni(dni) == False or validar_dni_existente(dni, alumnos) == False:
        print("DNI inválido o alumno inexistente.")
        dni = input("Ingrese el DNI del alumno: ")

    return dni


# Solicita un nombre o apellido y comprueba que no esté vacío.
def pedir_nombre(mensaje: str) -> str:
    """
    Solicita un nombre o apellido y verifica que no esté vacío.

    Args:
        mensaje (str): Mensaje que se muestra al solicitar el dato.

    Returns:
        str: Nombre o apellido ingresado.
    """
    nombre = input(mensaje)

    while validar_nombre(nombre) == False:
        print("El campo no puede estar vacío.")
        nombre = input(mensaje)

    return nombre


# Solicita una edad y comprueba que no sea negativa.
def pedir_edad() -> int:
    """
    Solicita la edad y verifica que no sea negativa.

    Returns:
        int: Edad ingresada por el usuario.
    """
    edad = int(input("Ingrese la edad: "))

    while validar_edad(edad) == False:
        print("La edad no puede ser negativa.")
        edad = int(input("Ingrese la edad: "))

    return edad


# Solicita una nota y comprueba que esté entre 0 y 10.
def pedir_nota() -> int:
    """
    Solicita la nota final y verifica que esté entre 0 y 10.

    Returns:
        int: Nota ingresada por el usuario.
    """
    nota = int(input("Ingrese la nota final: "))

    while validar_nota(nota) == False:
        print("La nota debe estar entre 0 y 10.")
        nota = int(input("Ingrese la nota final: "))

    return nota


# Registra un alumno nuevo en el diccionario.
def agregar_alumno(alumnos: dict) -> bool:
    """
    Solicita los datos y registra un alumno nuevo.

    Args:
        alumnos (dict): Diccionario donde se guardan los alumnos.

    Returns:
        bool: True si el alumno fue agregado correctamente.
    """
    # Solicitamos todos los datos del alumno.
    dni = pedir_dni_nuevo(alumnos)
    nombre = pedir_nombre("Ingrese el nombre: ")
    apellido = pedir_nombre("Ingrese el apellido: ")
    edad = pedir_edad()
    nota_final = pedir_nota()

    # Creamos un diccionario con los datos del alumno.
    # El DNI se utiliza como clave del diccionario principal.
    alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota_final": nota_final
    }

    print("Alumno agregado correctamente.")

    return True


# Muestra todos los alumnos registrados.
def listar_alumnos(alumnos: dict) -> None:
    """
    Muestra los datos de todos los alumnos registrados.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
    """

    if len(alumnos) <= 0:
        print("No hay alumnos registrados.")
        return

    for dni in alumnos:

        datos = alumnos[dni]

        print("-------------------------")
        print("DNI:", dni)
        print("Nombre:", datos["nombre"])
        print("Apellido:", datos["apellido"])
        print("Edad:", datos["edad"])
        print("Nota final:", datos["nota_final"])


# Muestra en pantalla los datos de un alumno.
def mostrar_alumno(dni: str, datos: dict) -> None:
    """
    Muestra los datos de un alumno en pantalla.

    Args:
        dni (str): DNI del alumno.
        datos (dict): Diccionario con los datos del alumno.
    """
    print("-------------------------")
    print("DNI:", dni)
    print("Nombre:", datos["nombre"])
    print("Apellido:", datos["apellido"])
    print("Edad:", datos["edad"])
    print("Nota final:", datos["nota_final"])


# Busca un alumno y muestra sus datos.
def buscar_alumno(alumnos: dict) -> tuple:
    """
    Busca un alumno por su DNI y muestra su información.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
    """
    # Solicitamos un DNI que esté registrado.
    dni = pedir_dni_existente(alumnos)

    # Obtenemos los datos correspondientes a ese DNI.
    datos = alumnos[dni]

    return dni, datos


# Muestra las opciones disponibles para modificar un alumno.
def mostrar_menu_modificacion() -> None:
    """
    Muestra las opciones para modificar los datos de un alumno.
    """
    print("1. Modificar nombre")
    print("2. Modificar apellido")
    print("3. Modificar edad")
    print("4. Modificar nota")


# Solicita una opción y comprueba que sea válida.
def pedir_opcion_modificacion() -> str:
    """
    Solicita una opción y verifica que sea válida.

    Returns:
        str: Opción elegida por el usuario.
    """
    opcion = input("Seleccione una opción: ")

    # Repite el pedido mientras la opción no sea válida.
    while validar_opcion_modificacion(opcion) == False:
        print("Opción inválida.")
        opcion = input("Seleccione una opción: ")

    return opcion


# Modifica el nombre de un alumno.
def modificar_nombre(alumnos: dict, dni: str) -> None:
    """
    Solicita y modifica el nombre de un alumno.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
        dni (str): DNI del alumno que se desea modificar.
    """
    alumnos[dni]["nombre"] = pedir_nombre("Ingrese el nuevo nombre: ")


# Modifica el apellido de un alumno.
def modificar_apellido(alumnos: dict, dni: str) -> None:
    """
    Solicita y modifica el apellido de un alumno.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
        dni (str): DNI del alumno que se desea modificar.
    """
    alumnos[dni]["apellido"] = pedir_nombre("Ingrese el nuevo apellido: ")


# Modifica la edad de un alumno.
def modificar_edad(alumnos: dict, dni: str) -> None:
    """
    Solicita y modifica la edad de un alumno.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
        dni (str): DNI del alumno que se desea modificar.
    """
    alumnos[dni]["edad"] = pedir_edad()


# Modifica la nota final de un alumno.
def modificar_nota(alumnos: dict, dni: str) -> None:
    """
    Solicita y modifica la nota final de un alumno.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
        dni (str): DNI del alumno que se desea modificar.
    """
    alumnos[dni]["nota_final"] = pedir_nota()


# Coordina el proceso de modificación de un alumno.
def modificar_alumno(alumnos: dict) -> bool:
    """
    Coordina la modificación de un dato de un alumno.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        bool: True si la modificación se realizó correctamente.
    """
    # Solicitamos el DNI del alumno que queremos modificar.
    dni = pedir_dni_existente(alumnos)

    # Mostramos las opciones y solicitamos una elección válida.
    mostrar_menu_modificacion()
    opcion = pedir_opcion_modificacion()

    # Según la opción elegida, modificamos el campo correspondiente.
    match opcion:
        case "1":
            modificar_nombre(alumnos, dni)

        case "2":
            modificar_apellido(alumnos, dni)

        case "3":
            modificar_edad(alumnos, dni)

        case "4":
            modificar_nota(alumnos, dni)

    print("Alumno modificado correctamente.")

    return True


# Elimina un alumno del diccionario mediante su DNI.
def eliminar_alumno(alumnos: dict) -> bool:
    """
    Elimina un alumno del diccionario mediante su DNI.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        bool: True si el alumno fue eliminado correctamente.
    """
    # Solicitamos el DNI de un alumno existente.
    dni = pedir_dni_existente(alumnos)

    # Eliminamos el registro correspondiente a ese DNI.
    del alumnos[dni]

    print("Alumno eliminado correctamente.")

    return True
