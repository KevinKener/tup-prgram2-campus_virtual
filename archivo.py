from datetime import datetime

class Archivo:
    def __init__(self, archivo: str, formato: str) -> None:
        self.__archivo = archivo
        self.__formato = formato
        self.__fecha = datetime.now()

    @property
    def archivo(self) -> str:
        return self.__archivo
    
    @property
    def formato(self) -> str:
        return self.__formato
    
    @property
    def fecha(self) -> str:
        return self.__fecha.strftime("%Y-%m-%d")

    def __str__(self) -> str:
        return f"Archivo: {self.archivo}, Formato: {self.formato}, Fecha: {self.fecha}"