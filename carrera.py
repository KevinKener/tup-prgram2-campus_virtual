class Carrera:
    def __init__(self, nombre: str, cant_anios: int, materias: list = []) -> None:
        self.nombre = nombre
        self.cant_anios = cant_anios
        self.materias = materias  # Guardará las materias de la carrera

    def __str__(self) -> str:
        return f"Carrera: {self.nombre}, Duración: {self.cant_anios} años"

    def get_cantidad_materias(self) -> int:
        return len(self.materias)  # Retorna la cantidad de materias

    def agregar_materia(self, materia: str) -> None:
        self.materias.append(materia)  # Agrega una materia a la lista de materias

    def obtener_materias(self) -> list:
        return self.materias  # Retorna la lista de materias

    def eliminar_materia(self, materia: str) -> None:
        if materia in self.materias:
            self.materias.remove(materia)  # Elimina una materia de la lista de materias
        else:
            print(f"{materia} no se encuentra en la lista de materias de la carrera.")