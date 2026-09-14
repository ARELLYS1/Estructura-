# EJERCICIO_1 CLASE BASICA 

# Crear la clase Pasajero con nombre, cédula y edad.
# Crear tres instancias y mostrarlas.

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # los datos de tres pasajeros
  
  #2) Proceso -  Qué hago con eso
  # definir la clase, luego instanciar
  
  # 3) Salida — Qué debo mostrar
  # los tres pasajeros formateados
  
#2) BOSQUEJO A MANO 

  # MOLDE (clase Pasajero):
  # - nombre, cedula, edad
  # - __init__ para crearlos
  # - __str__ para mostrarlos

  # Fábrica:
  # p1 = Pasajero("Ana", ..., 28)
  # p2 = Pasajero("Luis", ..., 35)
  # p3 = Pasajero("Diana", ..., 22)
  
# 3) DESCUBRIR EL PATRON 

  # Los atributos self.nombre, self.cedula, self.edad pertenecen a
  #cada objeto, no a la clase. Por eso cambian entre p1, p2, p3.
  # El __str__ permite que print(p1) muestre algo útil en vez de 
  # <__main__.Pasajero object at 0x7f...>.
  
# 4) ESCRIBIR CODIGO 

class Pasajero:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - {self.edad} años"

# --- Programa principal ---
p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

print(p1)
print(p2)
print(p3)

# Añade un método cumplir_anios() que sume 1 a la edad.

class Pasajero:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1

    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - {self.edad} años"


# --- Programa principal ---
p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

p1.cumplir_anios()
p2.cumplir_anios()
p3.cumplir_anios()

print(p1)
print(p2)
print(p3)



#====================================================
# EJERCICIO_2 CLASE CUENTABANCARIA
#===================================================
# Crear CuentaBancaria con métodos depositar, retirar, 
# saldo y __str__. El saldo empieza en 0.
# No se puede retirar más de lo que hay.

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # movimientos de la cuenta
  
  #2) Proceso -  Qué hago con eso
  # métodos que modifican el estado interno
  
  # 3) Salida — Qué debo mostrar
  # el saldo tras cada operación
  
#2) BOSQUEJO A MANO 

  # cuenta = CuentaBancaria("001")
  # cuenta.depositar(100)   → saldo = 100
  # cuenta.retirar(30)      → saldo = 70
  # cuenta.retirar(200)     → error, no hay suficiente
  # cuenta.saldo()          → 70
  
# 3) DESCUBRIR EL PATRON 

  # Aquí las acciones son las protagonistas.
  # Cada método modifica el estado interno del objeto.
  # Fíjate en el método retirar: valida antes de restar. 
  # Es la ventaja de encapsular en una clase: la lógica de validación vive junto a los datos, no dispersa por el programa.
  
# 4) ESCRIBIR CODIGO 


class CuentaBancaria:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0                # el _ indica "atributo interno"

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido"); return
        self._saldo += monto
        print(f"Depósito de ${monto}. Saldo: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido"); return
        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})"); return
        self._saldo -= monto
        print(f"Retiro de ${monto}. Saldo: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta {self.numero}: ${self._saldo}"

# --- Uso ---
c = CuentaBancaria("001")
c.depositar(100)         # Depósito de $100. Saldo: $100
c.retirar(30)            # Retiro de $30. Saldo: $70
c.retirar(200)           # Saldo insuficiente (tiene $70)
print(c)                 # Cuenta 001: $70
print(c.saldo())         # 70


# Añade historial: una lista donde cada operación añade
# un string tipo '+100', '-30'. Método ver_historial().

class CuentaBancaria:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0
        self.historial = []

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return

        self._saldo += monto
        self.historial.append(f"+{monto}")
        print(f"Depósito de ${monto}. Saldo: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return

        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})")
            return

        self._saldo -= monto
        self.historial.append(f"-{monto}")
        print(f"Retiro de ${monto}. Saldo: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def ver_historial(self):
        print("Historial:")
        for operacion in self.historial:
            print(operacion)

    def __str__(self):
        return f"Cuenta {self.numero}: ${self._saldo}"


# --- Uso ---
c = CuentaBancaria("001")

c.depositar(100)
c.retirar(30)
c.retirar(200)

print(c)
print(c.saldo())

c.ver_historial()





#====================================================
# EJERCICIO_3 CLASE PRODUCTO PARA TIENDA 
#===================================================
# Clase Producto con nombre, precio y stock. Métodos: 
# vender(cantidad) (reduce stock si hay), reabastecer(cantidad), 
# valor_inventario() (precio × stock).

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # productos y sus operaciones
  
  #2) Proceso -  Qué hago con eso
  # encapsular stock y precio
  
  # 3) Salida — Qué debo mostrar
  # valor del inventario y estado del producto
  
#2) BOSQUEJO A MANO 

  # Producto("Leche", 1.20, 10)
  # vender(3)           → stock=7
  # vender(20)          → error, sin stock suficiente
  # reabastecer(5)      → stock=12
  # valor_inventario()  → 12 * 1.20 = 14.40

# 3) DESCUBRIR EL PATRON 

  # Mismo patrón que CuentaBancaria: 
  # validación al vender, actualización interna, método consultor.
  # Nota cómo la clase protege sus propias reglas: nunca se puede 
  # vender lo que no hay.
  
# 4) ESCRIBIR CODIGO 


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"Sin stock suficiente ({self.stock} disponibles)"); return False
        self.stock -= cantidad
        print(f"Vendidas {cantidad} de {self.nombre}. Stock: {self.stock}")
        return True

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def valor_inventario(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - stock: {self.stock}"

# --- Uso ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)

print(leche)                     # Leche - $1.20 - stock: 10
leche.vender(3)                  # Vendidas 3
print(f"Valor: ${leche.valor_inventario():.2f}")  # Valor: $8.40
leche.vender(20)                 # Sin stock suficiente
leche.reabastecer(5)             # Nuevo stock: 12


# Amplíalo con un método de clase total_inventario(productos) 
# que sume los valores de una lista de productos.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"Sin stock suficiente ({self.stock} disponibles)")
            return False

        self.stock -= cantidad
        print(f"Vendidas {cantidad} de {self.nombre}. Stock: {self.stock}")
        return True

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def valor_inventario(self):
        return self.precio * self.stock

    @classmethod
    def total_inventario(cls, productos):
        total = 0

        for producto in productos:
            total += producto.valor_inventario()

        return total

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - stock: {self.stock}"


# --- Uso ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)

print(leche)
leche.vender(3)

print(f"Valor leche: ${leche.valor_inventario():.2f}")

leche.vender(20)

leche.reabastecer(5)

print(pan)

# Lista de productos
productos = [leche, pan]

# Total del inventario
total = Producto.total_inventario(productos)

print(f"Total inventario: ${total:.2f}")