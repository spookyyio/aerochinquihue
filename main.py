class Vuelo:
    def __init__(self, id_vuelo, tipo_avion, destino, hora_salida, hora_llegada, precio, precioencomienda, cap_pasajeros, carga_maxima):
        self.id_vuelo = id_vuelo
        self.tipo_avion = tipo_avion
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.precio = precio
        self.precioencomienda = precioencomienda
        self.cap_pasajeros = cap_pasajeros
        self.carga_maxima = carga_maxima

    def obtener_informacion_vuelo(self):
        return (f"Vuelo {self.id_vuelo} en {self.tipo_avion} con destino a {self.destino}.\n"
                f"Salida: {self.hora_salida} - Llegada: {self.hora_llegada}\n"
                f"Precio: ${self.precio}"
                f"Precio encomienda: ${self.precioencomienda}"
                f"Capacidad de pasajeros: {self.cap_pasajeros} - Carga máxima: {self.carga_maxima}")

class Encomienda:
    def __init__(self, dimensiones, tipo_encomienda, precio):
        self.dimensiones = dimensiones
        self.tipo_encomienda = tipo_encomienda
        self.precio = precio

    def obtener_informacion_encomienda(self):
        return (f"Encomienda: {self.tipo_encomienda}, Dimensiones: {self.dimensiones}, Precio: ${self.precio}")

class Pasajero:
    def __init__(self, nombre, apellido, id_pasajero, nacionalidad, telefono, edad, encomienda=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id_pasajero = id_pasajero
        self.encomienda = encomienda
        self.nacionalidad = nacionalidad
        self.telefono = telefono
        self.edad = edad

    def obtener_informacion_pasajero(self):
        info = (f"Pasajero: {self.nombre} {self.apellido}, ID: {self.id_pasajero}, "
                f"Nacionalidad: {self.nacionalidad}, Telefono: {self.telefono}, Edad: {self.edad} "
                f"{self.encomienda.obtener_informacion_encomienda() if self.encomienda else 'Sin encomienda'}")
        return info
    
    def calc_descuento(self):
        return ("Place holder")
    def solicitar_reserva(self):
        return ("Place holder")
    def enviar_encomienda(self):
        return ("Place holder")

def crear_pasajero(nombre, apellido, id_pasajero, nacionalidad, telefono, edad, desea_encomienda, dimensiones=None, tipo_encomienda=None, precio_encomienda=0):
    if desea_encomienda:
        encomienda = Encomienda(dimensiones, tipo_encomienda, precio_encomienda)
    else:
        encomienda = None
    return Pasajero(nombre, apellido, id_pasajero, nacionalidad, telefono, edad, encomienda)

class Reserva:
    def __init__(self, id_reserva, fecha, estado, asiento, precio_total):
        self.id_reserva = id_reserva
        self.fecha = fecha
        self.estado = estado
        self.asiento = asiento
        self.precio_total = precio_total

    def calcular_preciofinal(self):
        return ("Place holder")

class Gerente:
    def __init__(self, id_gerente, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.id_gerente = id_gerente

    def revisar_resumenventas(self):
        return ("Place holder")

    def realizar_vueloExtraordinario(self):
        return ("Place holder")
    
    def aplicar_descuento(self):
        return ("Place holder")
    
class Aerodromo:
    def __init__(self, id_aerodromo, modelo, cap_pasajero, cap_carga):
        return ("Place holder")
    
class Asistente:
    def __init__(self, id_asistente, nombre, apellido):
        self.id_asistente = id_asistente
        self.nombre = nombre
        self.apellido = apellido

    def gestionar_reservas(self):
        return ("Place holder")
    def gestionar_encomienda(self):
        return ("Place holder")

# poblacion de datos de prueba
vuelo1 = Vuelo("CC123", "C. Caravan 208", "Cochamo", "08:00", "12:00", 20000, 5000, 6, 1315)
vuelo2 = Vuelo("CC124", "C. Caravan 208", "Puelo Bajo", "08:00", "12:00", 20000, 5000, 6, 1315)
vuelo3 = Vuelo("CC125", "C. Caravan 310", "Contao", "08:00", "12:00", 20000, 5000, 9, 910)
vuelo4 = Vuelo("CC126", "C. Caravan 310", "Rio Negro", "08:00", "12:00", 25000, 6000, 9, 910)
vuelo5 = Vuelo("CC127", "C. Caravan 208", "Pupelde", "08:00", "12:00", 25000, 6000, 6, 1315)
vuelo6 = Vuelo("CC128", "C. Caravan 310", "Chepu", "08:00", "12:00", 30000, 8000, 9, 910)
vuelo7 = Vuelo("CC129", "C. Caravan 208", "Ayacara", "08:00", "12:00", 30000, 8000, 6, 1315)
vuelo8 = Vuelo("CC130", "C. Caravan 208", "Pillan", "08:00", "12:00", 40000, 12000, 6, 1315)
vuelo9 = Vuelo("CC131", "C. Caravan 310", "Renihue", "08:00", "12:00", 40000, 12000, 9, 910)
vuelo10 = Vuelo("CC132", "C. Caravan 208", "Isla Quenac", "08:00", "12:00", 40000, 12000, 6, 1315)
vuelo11= Vuelo("CC133", "C. Caravan 208", "Palqui", "08:00", "12:00", 40000, 12000, 6, 1315)
vuelo12 = Vuelo("CC134", "C. Caravan 310", "Chaiten", "08:00", "12:00", 50000, 15000, 9, 910)
vuelo13 = Vuelo("CC135", "C. Caravan 310", "Santa Barbara", "08:00", "12:00", 50000, 15000, 9, 910)

vuelos = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7, vuelo8, vuelo9, vuelo10, vuelo11, vuelo12, vuelo13]

pasajero1 = crear_pasajero("Juan", "Perez", "123456", "Chilena", "12345678", 30, True, "1x1x1", "Caja", 5000)
pasajero2 = crear_pasajero("Maria", "Gonzalez", "654321", "Argentina", "87654321", 25, False)

while True:
    print("\n--- Menú Principal ---")
    print("1. Ver información de vuelos.")
    print("2. Ver información del pasajero 1")
    print("3. Ver información del pasajero 2")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        contador=0
        for vuelo in vuelos:
            contador+=1
            print(f"\n{contador}" + vuelo.obtener_informacion_vuelo())
            continue
    elif opcion == "2":
        print("\n" + pasajero1.obtener_informacion_pasajero())
    elif opcion == "3":
        print("\n" + pasajero2.obtener_informacion_pasajero())
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida, intenta nuevamente.")