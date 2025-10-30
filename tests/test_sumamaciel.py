from funciones.sumamaciel import suma_maciel

def test_suma_maciel():
    assert suma_maciel(2, 3) == 5
    assert suma_maciel(-1, 1) == 0
