from src.las_listas import Listas
class DNI:

    def __init__(self, numero):
        self.numero = str(numero)

    def dni_correcto(self):
        if len(self.numero) != 8:
            raise ValueError("DNI no correcto")
        else:
            return self.numero

    @staticmethod
    def dni_completo(numero):
        assert isinstance(numero, int)
        assert len(str(numero)) == 8
        x = numero % len(Listas.lista_letras)
        letra_encontrada = Listas.lista_letras[x]
        complete_dni = str(numero) + letra_encontrada
        assert isinstance(complete_dni, str)
        assert len(complete_dni) == 9 
        return complete_dni
    
    @staticmethod
    def mala_letra(letra_encontrada):
        if letra_encontrada in Listas.letras_pochas:
            raise ValueError("letra no permitida")
        else:
            return letra_encontrada
