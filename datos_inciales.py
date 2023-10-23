# Aca realizamos la creracion de datos_iniciales.py contiene a los estudiantes con sus datos al igual que a los profesores.
# Tambien agregamos cursos, y sus contraseñas.

from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

estudiantes = [
    Estudiante("Kevin", "Kener", "kevinkener@gmail.com", "kevin1234", 54789, 2022), 
    Estudiante("Joaquin", "Benitez Velazquez", "joaco07@hotmail.com", "joaco456", 50234, 2020)
]

profesores = [
    Profesor("Ana", "Martínez", "anamartinez@gmail.com", "ana1234", "Ingeniería En Electrónica", 2005),
    Profesor("Carlos", "Gómez", "carlosgomez@hotmail.com", "carlos456", "Ingeniería En Sistemas", 2012)
]

cursos = [
    Curso("Ingles I", 'kKj10'),
    Curso("Ingles II", 'kKj20'),
    Curso("Laboratorio I", 'kKj30'),
    Curso("Laboratorio II", 'kKj40'),
    Curso("Programacion I", 'kKj50'),
    Curso("Programacion II", 'kKj60')
]