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

# CLASE ALMACÉN
# Creamos la clase almacén para añadir repuestos a este y buscar entre la lista de repuestos

class Almacen:
    def __init__(self, nombre: str, localizacion: str):
        self.nombre = nombre
        self.localizacion = localizacion
        # lista vacía donde meteremos los objetos Repuesto
        self.catalogo_piezas = [] 

    # Añadir objeto a lista
    def agregar_repuesto(self, repuesto: Repuesto):
        self.catalogo_piezas.append(repuesto)

    # buscar objeto 
    def buscar_repuesto(self, nombre_repuesto: str):
        for pieza in self.catalogo_piezas:
            if pieza.nombre == nombre_repuesto:
                return pieza
        return None  
    # imprimir
    def __str__(self):
        return f"Almacén '{self.nombre}' en {self.localizacion} (Piezas distintas: {len(self.catalogo_piezas)})"

# CLASES DE USUARIOS
# Hay dos tipos de usuarios: los Comandantes, que consultan y adquieren, y los Operarios, que mantienen el stock.

# Clase padre. Atributos que tienen todos los usuarios.
class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario

class Comandante(Usuario):
    def __init__(self, nombre: str, id_usuario: str):
        # Llamamos al padre (Usuario) para adquirir sus atributos
        super().__init__(nombre, id_usuario)

    # Busca en el almacen para ver si exite una pieza
    def consultar_repuesto(self, almacen: Almacen, nombre_repuesto: str):
        pieza = almacen.buscar_repuesto(nombre_repuesto)
        if pieza:
            print(f"El Comandante {self.nombre} ha encontrado: {pieza}")
            return pieza
        else:
            print(f"Repuesto '{nombre_repuesto}' no encontrado en el almacén {almacen.nombre}.")
            return None

    def adquirir_repuesto(self, almacen: Almacen, nombre_repuesto: str, cantidad_a_comprar: int):
        pieza = almacen.buscar_repuesto(nombre_repuesto)
        if pieza:
            stock_actual = pieza.get_cantidad()
            if stock_actual >= cantidad_a_comprar:
                # Restamos la cantidad 
                pieza.set_cantidad(stock_actual - cantidad_a_comprar)
                print(f" El Comandante {self.nombre} ha adquirido {cantidad_a_comprar}x {nombre_repuesto}.")
            else:
                print(f"No hay suficiente stock de {nombre_repuesto}. Stock actual: {stock_actual}")
        else:
            print("La pieza no existe en este almacén.")

class Operario(Usuario):
    def __init__(self, nombre: str, id_usuario: str):
        # Llamamos al padre
        super().__init__(nombre, id_usuario)

    # Meter piezas al almacen
    def añadir_repuesto_catalogo(self, almacen: Almacen, nuevo_repuesto: Repuesto):
        almacen.agregar_repuesto(nuevo_repuesto)
        print(f"Operario {self.nombre} ha añadido {nuevo_repuesto.nombre} al catálogo del almacén {almacen.nombre}.")

    # cambiar el stock
    def actualizar_stock(self, repuesto: Repuesto, nueva_cantidad: int):
        # cambiar el stock privado con set_cantidad
        repuesto.set_cantidad(nueva_cantidad)
        print(f"Operario {self.nombre} ha actualizado el stock de {repuesto.nombre} a {nueva_cantidad}.")
        