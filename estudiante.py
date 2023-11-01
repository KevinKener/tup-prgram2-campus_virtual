#Agregamos estudiante.py como una implentacion de una clase llamada Estudiante que hereda de la clase Usuario.
#La clase estudiante contiene ya sus propiedades.
#Ademas tambien el método para matricular al estudiante en cursos.

from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    #Agregamos la funcion para desmatricularse del curso.

    def desmatricularse_curso(self, curso):
        if curso in self.mis_cursos:
            self.mis_cursos.remove(curso)
        else:
            print("No estás matriculado en este curso.")

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo):
        self.__legajo = nuevo_legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos
    
    def __str__(self) -> str:
        return self.nombre

    def matricular_en_curso(self, curso) -> None:
        self.mis_cursos.append(curso)