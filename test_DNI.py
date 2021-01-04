from code_del_dni import DNI
def test_resto_DNI():
    assert '43470427J' == DNI.letra_dni(43470427)
    assert '44481538K' == DNI.letra_dni(44481538)
    assert '43719375D' == DNI.letra_dni(43719375)
    assert '65004204V' == DNI.letra_dni(65004204)

# def test_numero_y_letra():
#     assert letra_dni[0:7] == int
    
    