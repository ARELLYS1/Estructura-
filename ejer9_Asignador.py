# ASIGNADOR DE EQUIPOS 

# Clase Equipos que:
# (1) tenga método crear_equipo(nombre_equipo) 
# que inicie un equipo como una lista vacía en un diccionario;
# (2) tenga método agregar_jugador(equipo, jugador)
# que añada el jugador al equipo;
# (3) tenga método equipo_mayor_integrantes() 
# que retorne el nombre del equipo con más jugadores.

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = ""
        cantidad = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad:
                cantidad = len(jugadores)
                mayor = equipo

        return mayor



e = Equipos()


e.crear_equipo("Barcelona")
e.crear_equipo("Emelec")


e.agregar_jugador("Barcelona", "Juan")
e.agregar_jugador("Barcelona", "Pedro")
e.agregar_jugador("Barcelona", "Carlos")

e.agregar_jugador("Emelec", "Luis")
e.agregar_jugador("Emelec", "Miguel")


print(e.equipo_mayor_integrantes())