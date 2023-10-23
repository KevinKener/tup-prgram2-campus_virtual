#La clase Usuario es creada para dar una estructura base que define atributos como nombre, apellido, email y contraseña para representar a x usuario.
#Creamos sus atributos protegidos para controlar el acceso. 


from abc import ABC, abstractmethod

class Usuario(ABC): 
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email
