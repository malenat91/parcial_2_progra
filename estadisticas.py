
def calcular_promedio(alumnos: dict) -> float:
    """
    Calcula el promedio general de las notas de todos los alumnos.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        float: Promedio general de las notas.
    """
    suma_notas = 0

    for datos in alumnos.values():
        suma_notas += datos["nota_final"]

    promedio = suma_notas / len(alumnos)

    return promedio


def contar_aprobados(alumnos: dict) -> int:
    """
    Cuenta la cantidad de alumnos aprobados (nota mayor o igual a 6).

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        int: Cantidad de alumnos aprobados.
    """
    aprobados = 0

    for datos in alumnos.values():
        if datos["nota_final"] >= 6:
            aprobados += 1

    return aprobados


def contar_desaprobados(alumnos: dict) -> int:
    """
    Cuenta la cantidad de alumnos desaprobados (nota menor a 6).

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        int: Cantidad de alumnos desaprobados.
    """
    desaprobados = 0

    for datos in alumnos.values():
        if datos["nota_final"] < 6:
            desaprobados += 1

    return desaprobados


def obtener_mejor_alumno(alumnos: dict) -> tuple:
    """
    Busca al alumno que obtuvo la nota más alta.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.

    Returns:
        tuple: DNI y datos del alumno con la nota más alta.
    """
    nota_mayor = -1
    mejor_dni = ""

    for dni, datos in alumnos.items():
        if datos["nota_final"] > nota_mayor:
            nota_mayor = datos["nota_final"]
            mejor_dni = dni

    return mejor_dni, alumnos[mejor_dni]


def mostrar_estadisticas(alumnos: dict) -> None:
    """
    Toma los datos ya calculados y muestra las estadísticas generales de los alumnos.

    Args:
        alumnos (dict): Diccionario con los alumnos registrados.
    """
    if len(alumnos) == 0:
        print("No hay alumnos para calcular estadísticas.")
    else:
        total = len(alumnos)
        promedio = calcular_promedio(alumnos)
        aprobados = contar_aprobados(alumnos)
        desaprobados = contar_desaprobados(alumnos)

        dni, mejor_alumno = obtener_mejor_alumno(alumnos)

        print("\n===== ESTADÍSTICAS =====")
        print("Total de alumnos:", total)
        print("Promedio general:", promedio)
        print("Alumnos aprobados:", aprobados)
        print("Alumnos desaprobados:", desaprobados)

        print("\nAlumno con mayor nota:")
        print("DNI:", dni)
        print("Nombre:", mejor_alumno["nombre"])
        print("Apellido:", mejor_alumno["apellido"])
        print("Nota:", mejor_alumno["nota_final"])
