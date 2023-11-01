from archivo import Archivo
import random
import string

class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion=None):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion if contrasenia_matriculacion is not None else self.__generar_contrasenia()
        self.__archivos = []  # Lista para almacenar archivos del curso
        self.__codigo_curso = random.randint(100, 999)  # Generar un código aleatorio de 3 dígitos

        # Generar archivos de ejemplo al crear un nuevo curso
        self.__generar_ejemplos_archivos()

    def agregar_archivo(self, nombre: str, formato: str):
        nuevo_archivo = Archivo(nombre, formato)
        self.__archivos.append(nuevo_archivo)
        return f"Archivo {nombre}.{formato} agregado al curso {self.__nombre}"

    def mostrar_archivos(self):
        archivos_ordenados = sorted(self.__archivos, key=lambda x: x.fecha)
        return [str(archivo) for archivo in archivos_ordenados]

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self) -> str:
        return self.__contrasenia_matriculacion

    @property
    def codigo_curso(self) -> int:
        return self.__codigo_curso

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}\nCódigo: {self.__codigo_curso}\nContraseña: {self.__contrasenia_matriculacion}\nCantidad de archivos: {len(self.__archivos)}"

    @classmethod
    def __generar_contrasenia(cls) -> str:
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(password) for i in range(7))

    def __generar_ejemplos_archivos(self):
        # Se crean algunos archivos de ejemplo al iniciar un nuevo curso
        ejemplos = [("tpi", "pdf"), ("practica1", "pdf"), ("clase1", "docx")]  # Agrega aquí ejemplos de archivos
        for nombre, formato in ejemplos:
            self.agregar_archivo(nombre, formato)