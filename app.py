import os
from datos_inciales import estudiantes, profesores, cursos
from usuario import Usuario
from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
#Aca agregamos Archivo y Carrera
from archivo import Archivo
from carrera import Carrera
import random  # Importante añadir la librería random para generar el código del curso


# Funciones
def mensaje_bienvenida():
    print("Bienvenido/a al campus virtual!")

def menu_principal():
    print("1 - Ingresar como alumno.")
    print("2 - Ingresar como profesor.")
    print("3 - Ver cursos.")
    print("4 - Salir.")

#agregamos 2. Desmatricularse a un curso
def subMenu_alumno():
    print("1. Matricularse a un curso.")
    print("2. Desmatricularse a un curso.")
    print("3. Ver curso.")
    print("4. Volver al menú principal")

# Agregamos Función para mostrar los archivos del curso ordenados por fecha
def mostrar_archivos(curso):
    archivos_ordenados = sorted(curso.archivos, key=lambda x: x.fecha)
    for archivo in archivos_ordenados:
        print(archivo)

def subMenu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def mostrar_cursos(cursos):
    for curso in cursos:
        print(f"{curso} Carrera: Tecnicatura Universitaria en Programación")

#Ver cursos
def ver_curso(usuario, curso):
    if isinstance(usuario, Estudiante):
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre del curso: {curso.nombre}")
                print("Archivos:")
                mostrar_archivos(curso)  # Llama a la función para mostrar archivos
                break
    else:
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre del curso: {curso.nombre}")
                print("Archivos:")
                mostrar_archivos(curso)  # Llama a la función para mostrar archivos
                break

# Función para dar de alta al estudiante
def alta_estudiante():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")
    contrasenia = input("Ingrese su contraseña: ")
    legajo = int(input("Ingrese su número de legajo: "))
    anio_inscripcion = int(input("Ingrese el año de inscripción: "))
    nuevo_estudiante = Estudiante(nombre, apellido, email, contrasenia, legajo, anio_inscripcion)
    estudiantes.append(nuevo_estudiante)
    print("¡Registro exitoso! Bienvenido al campus virtual.")

# Función para dar de alta al profesor con código admin
def alta_profesor(codigo_admin):
    if codigo_admin == "admin":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        contrasenia = input("Ingrese su contraseña: ")
        titulo = input("Ingrese su título: ")
        anio_egreso = int(input("Ingrese su año de egreso: "))
        nuevo_profesor = Profesor(nombre, apellido, email, contrasenia, titulo, anio_egreso)
        profesores.append(nuevo_profesor)
        print("¡Registro exitoso! Bienvenido al campus virtual.")
    else:
        print("Código admin incorrecto")

def ingreso_credenciales(usuarios):
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario.email == email:
            if usuario.validar_credenciales(email, password):
                return "Usted ingreso correctamente al sistema", True, usuario
            else:
                return "La contraseña ingresada es incorrecta", False, usuario
    return "El email ingresado no se encuentra registrado, debe registrarse", False, usuario

def ver_curso(usuario, curso):
    if isinstance(usuario, Estudiante):
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                break
    else:
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                print(f"Contraseña: {curso.contrasenia_matriculacion}")
                break

def ingreso_alumno(estudiante):
    respuesta = ''
    while respuesta != "salir":
        subMenu_alumno()
        opt_alumno = input("\n Ingrese la opción de menú: ")
        os.system("cls")
        if opt_alumno.isnumeric():
            if int(opt_alumno) == 1:
                print("Cursos disponibles:")
                for i, curso in enumerate(cursos, 1):
                    print(f"{i}. {curso.nombre}")
                opt_curso = input("Ingrese el número del curso al que quiere matricularse: ")
                if opt_curso.isnumeric():
                    curso_index = int(opt_curso) - 1
                    if 0 <= curso_index < len(cursos):
                        curso_seleccionado = cursos[curso_index]

                        # Verificamos si el estudiante ya está matriculado en este curso
                        if curso_seleccionado in estudiante.mis_cursos:
                            print("Usted ya se encuentra matriculado en este curso.")
                        else:
                            contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")
                            if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
                                estudiante.matricular_en_curso(curso_seleccionado)
                                print(f"Usted se ha matriculado en el curso: {curso_seleccionado.nombre}")
                            else:
                                print("La contraseña de matriculación ingresada es incorrecta.")
                    else:
                        print("Curso no válido.")
                else:
                    print("Ingrese un número válido.")
            elif int(opt_alumno) == 2:
                print("Cursos a los que te has matriculado:")
                for i, curso in enumerate(estudiante.mis_cursos, 1):
                    print(f"{i}. {curso.nombre}")
                opt_curso = input("Ingrese el número del curso al que desea desmatricularse: ")
                if opt_curso.isnumeric():
                    curso_index = int(opt_curso) - 1
                    if 0 <= curso_index < len(estudiante.mis_cursos):
                        curso_seleccionado = estudiante.mis_cursos[curso_index]
                        # Eliminar el curso de la lista de cursos matriculados
                        estudiante.desmatricularse_curso(curso_seleccionado)
                        print(f"Se ha desmatriculado del curso: {curso_seleccionado.nombre}")
                    else:
                        print("Curso no válido.")
                else:
                    print("Ingrese un número válido.")
        #Aca completamos la opcion numero 3.
            elif int(opt_alumno) == 3:
                print("Cursos en los que estás matriculado:")
                for i, curso in enumerate(estudiante.mis_cursos, 1):
                    print(f"{i}. {curso.nombre}")
                opt_curso = input("Ingrese el número del curso que quiere visualizar: ")
                if opt_curso.isnumeric():
                    curso_index = int(opt_curso) - 1
                    if 0 <= curso_index < len(estudiante.mis_cursos):
                        curso_seleccionado = estudiante.mis_cursos[curso_index]
                        print(f"Nombre del curso: {curso_seleccionado.nombre}")
                        print("Archivos del curso:")
                        archivos_del_curso = curso_seleccionado.mostrar_archivos()
                        if archivos_del_curso:
                            for archivo in archivos_del_curso:
                                print(archivo)
                        else:
                            print("No hay archivos en este curso.")
                    else:
                        print("Curso no válido.")
                else:
                    print("Ingrese un número válido.")
            elif int(opt_alumno) == 4:
                respuesta = "salir"
            else:
                print("Ingrese una opción válida.")
        else:
            print("Ingrese una opción numérica.")
    print("Hasta luego!")

# Actualización de la función ingreso_profesor para integrar los nuevos requerimientos
def ingreso_profesor(profesor):
    respuesta = ''
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\n Ingrese la opción de menú: ")
        os.system("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                codigo_curso = random.randint(100, 999)  # Generar un código aleatorio de 3 dígitos
                nueva_contrasenia = Curso._Curso__generar_contrasenia()  # Generar contraseña automáticamente
                curso_nuevo = Curso(nombre_curso, nueva_contrasenia)
                cursos.append(curso_nuevo)
                profesor.dictar_curso(curso_nuevo)
                print("El curso ha sido ingresado correctamente!")
                print(f"Nombre: {curso_nuevo.nombre}")
                print(f"Código: {codigo_curso}")
                print(f"Contraseña: {nueva_contrasenia}")
            elif int(opt_profesor) == 2:
                cursos_disponibles = {}
                for i, curso in enumerate(profesor.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i}. {curso.nombre}")
                opt_curso = input("Ingrese el número del curso que quiere visualizar: ")
                curso_seleccionado = cursos_disponibles.get(opt_curso)
                if not curso_seleccionado:
                    print("Curso no válido.")
                    continue
                print(f"Nombre: {curso_seleccionado.nombre}")
                print(f"Código: {curso_seleccionado.codigo_curso}")
                print(f"Contraseña: {curso_seleccionado.contrasenia_matriculacion}")
                print(f"Cantidad de archivos: {len(curso_seleccionado.mostrar_archivos())}")

                respuesta_adjunto = input("¿Desea agregar un archivo adjunto? (s/n): ")
                if respuesta_adjunto.lower() == 's':
                    nombre_archivo = input("Ingrese el nombre del archivo: ")
                    formato_archivo = input("Ingrese el formato del archivo: ")
                    curso_seleccionado.agregar_archivo(nombre_archivo, formato_archivo)
                    print("Archivo adjunto agregado con éxito.")

            elif int(opt_profesor) == 3:
                respuesta = "salir"
            else:
                print("Ingrese una opción válida.")
        else:
            print("Ingrese una opción numérica.")

#Matriculacion y Desmatriculacion

def matricularse_curso(alumno, cursos):
    print("Cursos disponibles:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso.nombre}")

    opt_curso = input("Ingrese el número del curso al que quiere matricularse: ")

    if opt_curso.isnumeric():
        curso_index = int(opt_curso) - 1

        if 0 <= curso_index < len(cursos):
            curso_seleccionado = cursos[curso_index]

            # Verificar si el curso está en la lista de cursos del alumno
            if curso_seleccionado in alumno.mis_cursos:
                print("Ya está matriculado en este curso.")
            else:
                # Verificar si el alumno pertenece a la carrera del curso
                if alumno.carrera == curso_seleccionado.carrera:
                    contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")

                    # Verificar si la contraseña ingresada es correcta
                    if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
                        # Matricular al alumno en el curso
                        alumno.matricular_en_curso(curso_seleccionado)
                        print(f"Usted se ha matriculado en el curso: {curso_seleccionado.nombre}")
                    else:
                        print("La contraseña de matriculación es incorrecta.")
                else:
                    print("El curso no pertenece a su carrera.")
        else:
            print("Curso no válido.")
    else:
        print("Ingrese un número válido.")


def desmatricularse_curso(alumno):
    print("Cursos a los que te has matriculado:")
    for i, curso in enumerate(alumno.mis_cursos, 1):
        print(f"{i}. {curso.nombre}")

    opt_curso = input("Ingrese el número del curso que quiere desmatricular: ")

    if opt_curso.isnumeric():
        curso_index = int(opt_curso) - 1

        if 0 <= curso_index < len(alumno.mis_cursos):
            curso_seleccionado = alumno.mis_cursos[curso_index]
            alumno.mis_cursos.remove(curso_seleccionado)
            print(f"Usted se ha desmatriculado del curso: {curso_seleccionado.nombre}")
        else:
            print("Curso no válido.")
    else:
        print("Ingrese un número válido.")

# app y menu principal
mensaje_bienvenida()
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:  # Opción 1 - Ingresar como alumno
            mensaje, validacion, estudiante = ingreso_credenciales(estudiantes)
            if validacion:
                print(mensaje)
                ingreso_alumno(estudiante)
            else:
                print(mensaje)
                alta = input("¿Desea darse de alta como estudiante? (s/n): ")
                if alta.lower() == 's':
                    alta_estudiante()
        elif int(opt) == 2:  # Opción 2 - Ingresar como profesor
            mensaje, validacion, profesor = ingreso_credenciales(profesores)
            if validacion:
                print(mensaje)
                ingreso_profesor(profesor)
            else:
                print(mensaje)
                alta = input("¿Desea darse de alta como profesor? (s/n): ")
                if alta.lower() == 's':
                    codigo_admin = input("Darse de alta ingresando el código admin : ")
                    alta_profesor(codigo_admin)  # Se corrige aquí
        elif int(opt) == 3:
            mostrar_cursos(cursos)
        elif int(opt) == 4:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida.")
    else: 
        print("Ingrese una opción numérica.")
    
    input("Presione cualquier tecla para continuar....")

print("Hasta luego!")