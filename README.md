# Sistema de Gestión de Alumnos

## Datos del proyecto

### Alumna

- Malena Aguirre

### Comisión

- 313

### Lenguaje utilizado

- 🐍 Python

## 📝 Descripción del código

El sistema desarrollado es una aplicación de consola que permite gestionar la información de los alumnos de un curso. A través de un menú interactivo, se pueden registrar nuevos alumnos, consultar sus datos, modificar o eliminar registros y obtener estadísticas generales del curso.

La información se almacena en un archivo JSON, lo que permite conservar los datos registrados incluso después de cerrar el programa.

### 🎯 Objetivos

- Registrar alumnos utilizando su DNI como identificador único.
- Validar los datos ingresados por el usuario.
- Consultar la información de los alumnos registrados.
- Modificar los datos de un alumno.
- Eliminar registros mediante el DNI.
- Calcular el promedio general del curso.
- Contabilizar los alumnos aprobados y desaprobados.
- Identificar al alumno con la nota más alta.
- Almacenar la información de manera permanente mediante archivos JSON.

### ⚙️ Funcionalidades implementadas

1. **📥 Agregar alumno:** solicita el DNI, nombre, apellido, edad y nota final. Valida los datos ingresados y registra al alumno en el diccionario.
2. **📋 Listar alumnos:** muestra la información de todos los alumnos registrados, incluyendo DNI, nombre, apellido, edad y nota final.
3. **🔎 Buscar alumno:** permite ingresar el DNI de un alumno y consultar su información completa. Si no existe, vuelve a solicitar el dato.
4. **✏️ Modificar alumno:** permite seleccionar un alumno mediante su DNI y modificar su nombre, apellido, edad o nota final.
5. **🗑️ Eliminar alumno:** permite eliminar un registro utilizando el DNI del alumno.
6. **📊 Mostrar estadísticas:** calcula el promedio general del curso, contabiliza los alumnos aprobados y desaprobados e identifica al alumno con la nota más alta.
7. **🚪 Salir:** finaliza la ejecución del programa.

### 🗂️ Organización del proyecto

El proyecto se encuentra dividido en cinco módulos:

- `main.py`: contiene el menú principal y coordina las distintas operaciones del programa.
- `alumnos.py`: contiene las funciones para agregar, listar, buscar, mostrar, modificar y eliminar alumnos.
- `validaciones.py`: contiene las funciones encargadas

###☆¡Gracias por leer!☆