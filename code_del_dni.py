from lista_letras import lista_letras
class DNI:

    
    @staticmethod
    def letra_dni(numero):
        assert isinstance(numero, int)
        x = numero % len(lista_letras)
        complete_dni = str(numero) + (lista_letras[x])
        assert isinstance(complete_dni, str)
        assert len(complete_dni) == 9
        return complete_dni

