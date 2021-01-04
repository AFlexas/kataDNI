from code_del_dni import DNI
def test_resto_DNI():
    assert '43470427J' == DNI.dni_completo(43470427)
    assert '44481538K' == DNI.dni_completo(44481538)
    assert '43719375D' == DNI.dni_completo(43719375)
    assert '65004204V' == DNI.dni_completo(65004204)

# def test_numero_y_letra():
#     assert letra_dni[0:7] == int
    
    