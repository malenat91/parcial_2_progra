
from archivos import cargar_alumnos, guardar_alumnos

from alumnos import (
    agregar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_alumno,
    eliminar_alumno,
    mostrar_alumno
)

from estadisticas import mostrar_estadisticas


def main() -> None:
    """
    Función principal del programa.
    """

    # Cargamos los alumnos del archivo JSON, funcion en el modulo archivos.
    alumnos = cargar_alumnos()

    # Inicializamos la opción del menú.
    opcion = ""

    # Repetimos el menú hasta que el usuario elija salir.
    while opcion != "7":

        print("\n===== SISTEMA DE GESTIÓN DE ALUMNOS =====")
        print("1. Registrar alumno")
        print("2. Listar alumnos")
        print("3. Buscar alumno")
        print("4. Modificar alumno")
        print("5. Eliminar alumno")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                resultado = agregar_alumno(alumnos)

                if resultado == True:
                    guardar_alumnos(alumnos)
                    print("Los datos se guardaron correctamente.")

            case "2":
                listar_alumnos(alumnos)

            case "3":
                dni, datos = buscar_alumno(alumnos)
                print("Alumno encontrado:")
                mostrar_alumno(dni, datos)

            case "4":
                resultado = modificar_alumno(alumnos)

                if resultado == True:
                    guardar_alumnos(alumnos)
                    print("Los cambios se guardaron correctamente.")

            case "5":
                resultado = eliminar_alumno(alumnos)

                if resultado == True:
                    guardar_alumnos(alumnos)
                    print("Los cambios se guardaron correctamente.")

            case "6":
                mostrar_estadisticas(alumnos)

            case "7":
                print("Saliendo del programa...\nHa salido con éxito.")

            case _:
                print("Opción inválida.")


# Llamamos a la función principal.
main()
