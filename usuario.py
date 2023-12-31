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

#Agregamos la funcionalidad relacionada con la contraseña y validacion.
#Con este metodo validar_credenciales nos va a ser util para verificar si el usuario pone los datos correctos

    @property
    def contrasenia(self):
        return self._contrasenia
    
    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self._contrasenia = nueva_contrasenia

    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str) -> bool:
        return self._email == email_ingresado and self._contrasenia == contrasenia_ingresada

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError