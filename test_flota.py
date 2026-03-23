# TEST UNITARIOS CON PYTEST

import pytest
from imperio import Repuesto, Almacen, Comandante

#  comprobar que se crea bien un repuesto
def test_crear_repuesto():
    pieza = Repuesto("Tornillo", "Acme", 100, 5.0)
    assert pieza.nombre == "Tornillo"
    assert pieza.get_cantidad() == 100

# comprobar que salta la excepción si ponemos stock negativo
def test_stock_negativo():
    pieza = Repuesto("Tornillo", "Acme", 100, 5.0)
    with pytest.raises(ValueError):
        pieza.set_cantidad(-10)

#  comprobar que el almacén guarda las piezas
def test_agregar_almacen():
    almacen = Almacen("Almacén Test", "Tatooine")
    pieza = Repuesto("Tornillo", "Acme", 100, 5.0)
    almacen.agregar_repuesto(pieza)
    
    assert len(almacen.catalogo_piezas) == 1
    assert almacen.buscar_repuesto("Tornillo") == pieza


if __name__ == "__main__":
    pytest.main()