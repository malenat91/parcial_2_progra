
import json


def cargar_alumnos() -> dict:
    """
    Carga los alumnos desde el archivo JSON.

    Returns:
        dict: Diccionario con los alumnos registrados.
    """
    with open("alumnos.json", "r", encoding="utf-8") as archivo:
        alumnos = json.load(archivo)

    return alumnos


def guardar_alumnos(alumnos: dict) -> None:
    """
    Guarda los alumnos en el archivo JSON.

    Args:
        alumnos (dict): Diccionario con los alumnos que se van a guardar.
    """
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4)
