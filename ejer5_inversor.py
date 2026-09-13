# INVERSOR DE SECUENCIAS 

#Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) 
# que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior 
# para invertir varias listas y retorne un diccionario
# {lista_original: lista_invertida}.

class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[str(lista)] = invertida

        return resultado



inv = InversorSecuencia()


print(inv.invertir_lista([1, 2, 3]))

print(inv.invertir_multiples([1, 2, 3], [4, 5, 6], [7, 8]))