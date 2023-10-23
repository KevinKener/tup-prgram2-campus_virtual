import os
from datos_inciales import estudiantes, profesores, cursos
from usuario import Usuario
from estudiante import Estudiante
from profesor import Profesor
from curso import Curso


# Funciones
def mensaje_bienvenida():
    print("Bienvenido/a al campus virtual!")

def menu_principal():
    print("1 - Ingresar como alumno.")
    print("2 - Ingresar como profesor.")
    print("3 - Ver cursos.")
    print("4 - Salir.")

def subMenu_alumno():
    print("1. Matricularse a un curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def subMenu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def mostrar_cursos(cursos):
    for curso in cursos:
        print(f"{curso} Carrera: Tecnicatura Universitaria en Programación")

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
                opt_curso = input("Ingrese el número del curso que quiere visualizar: ")
                if opt_curso.isnumeric():
                    curso_index = int(opt_curso) - 1
                    if 0 <= curso_index < len(estudiante.mis_cursos):
                        curso_seleccionado = estudiante.mis_cursos[curso_index]
                        ver_curso(estudiante, curso_seleccionado)
                    else:
                        print("Curso no válido.")
                else:
                    print("Ingrese un número válido.")
            elif int(opt_alumno) == 3:
                respuesta = "salir"
            else:
                print("Ingrese una opción válida.")
        else:
            print("Ingrese una opción numérica.")

def ingreso_profesor(profesor):
    cursos_disponibles = {}
    respuesta = ''
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\n Ingrese la opción de menú: ")
        os.system("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                curso = Curso(nombre_curso)
                cursos.append(curso)
                profesor.dictar_curso(curso)
                print("El curso ha sido ingresado correctamente!")
                ver_curso(profesor, curso)
            elif int(opt_profesor) == 2:
                for i, curso in enumerate(profesor.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i}. {curso.nombre}")
                opt_curso = input("Ingrese el número del curso que quiere visualizar: ")
                curso_seleccionado = cursos_disponibles.get(opt_curso)
                if not curso_seleccionado:
                    print("Curso no válido.")
                    continue
                ver_curso(profesor, curso_seleccionado)
            elif int(opt_profesor) == 3:
                respuesta = "salir"
            else: 
                print("Ingrese una opción válida.")
        else: 
            print("Ingrese una opción numérica.")

# app y menu principal
mensaje_bienvenida()
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            mensaje, validacion, estudiante = ingreso_credenciales(estudiantes)
            if validacion:
                print(mensaje)
                ingreso_alumno(estudiante)
            else:
                print(mensaje)
        elif int(opt) == 2:
            mensaje, validacion, profesor = ingreso_credenciales(profesores)
            if validacion:
                print(mensaje)
                ingreso_profesor(profesor)
            else:
                print(mensaje)
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