# DETECTOR DE NUMEROS PARES E IMPARES 

# Clase AnalizadorNumeros que: (1) tenga método es_par(numero)
# que retorne True/False; (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 
# 'impares': [...]} reutilizando es_par; 
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).

class AnalizadorNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []

        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {
            "pares": self.pares,
            "impares": self.impares
        }

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))



an = AnalizadorNumeros()


print(an.separar(1, 2, 3, 4, 5))


print(an.cantidad_pares_impares())