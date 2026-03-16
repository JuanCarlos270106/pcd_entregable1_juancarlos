# MI IMPERIO

# ENUMERACIONES
# 'Ubicacion' y 'ClaseNave' son una lista cerrada. Por eso importamos Enum.

from enum import Enum

class Ubicacion(Enum):
    ENDOR = "Endor"
    CUMULO_RAIMOS = "Cúmulo Raimos"
    NEBULOSA_KALIIDA = "Nebulosa Kaliida"

class ClaseNave(Enum):
    EJECUTOR = "Ejecutor"
    ECLIPSE = "Eclipse"
    SOBERANO = "Soberano"


# REPUESTO
# Para esta clase tenemos que hacer un atributo privado.

class Repuesto:
    def __init__(self, nombre: str, proveedor: str, cantidad: int, precio: float):
        self.nombre = nombre
        self.proveedor = proveedor
        self.precio = precio
        self.__cantidad = cantidad  # aatributo privado 
        

    #  método para leer atributo privado
    def get_cantidad(self) -> int:
        return self.__cantidad

    # método para modificarlo
    def set_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            raise ValueError("No puede ser negativa.")

    #  método para imprimir
    def __str__(self):
        return f"Repuesto: {self.nombre} | Proveedor: {self.proveedor} | Stock: {self.__cantidad} | Precio: {self.precio} cr"
    
# HERENCIA MÚLTIPLE

# nave con su nombre y lista de repuestos
class Nave:
    
    def __init__(self, nombre: str, catalogo_repuestos: list = None):
        self.nombre = nombre
        self.catalogo_repuestos = catalogo_repuestos if catalogo_repuestos is not None else []

# Todo vehículo militar tiene estos dos datos
class UnidadCombateImperial:
    
    def __init__(self, id_combate: str, clave_transmision: int):
        self.id_combate = id_combate
        self.clave_transmision = clave_transmision

# NAVES ESPECÍFICAS
# Llamamos a los constructores padres en cada nave y después añadimos atributos propios de cada una

class EstacionEspacial(Nave, UnidadCombateImperial):
    def __init__(self, nombre: str, id_combate: str, clave_transmision: int, tripulacion: int, pasaje: int, ubicacion: Ubicacion):
        
        Nave.__init__(self, nombre)
        UnidadCombateImperial.__init__(self, id_combate, clave_transmision)
        
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class NaveEstelar(Nave, UnidadCombateImperial):
    def __init__(self, nombre: str, id_combate: str, clave_transmision: int, tripulacion: int, pasaje: int, clase: ClaseNave):
        
        Nave.__init__(self, nombre)
        UnidadCombateImperial.__init__(self, id_combate, clave_transmision)
        
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

class CazaEstelar(Nave, UnidadCombateImperial):
    def __init__(self, nombre: str, id_combate: str, clave_transmision: int, dotacion: int):
        Nave.__init__(self, nombre)
        UnidadCombateImperial.__init__(self, id_combate, clave_transmision)
        
        self.dotacion = dotacion