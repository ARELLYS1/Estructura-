# GESTOR DE TAREAS CON PRIORIDAD 

# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad)
# que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() 
# que retorne solo las de prioridad alta;
# (3) tenga método eliminar_completada(descripcion) 
# que borre la tarea de la lista.

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Programar", "alta")

print(t.tareas_prioritarias())