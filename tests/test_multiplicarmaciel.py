from funciones.multiplicamaciel import multiplicar_maciel

def test_multiplicar_maciel():
    assert multiplicar_maciel(3, 4) == 12
    assert multiplicar_maciel(-2, 5) == -10