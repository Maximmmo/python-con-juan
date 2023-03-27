#año bisiesto
"""
print("digite el año:")
anio = 2024
if anio % 4 == 0 and anio % 400 != 0 or anio %400 == 0:    
    print("año bisiesto")
else:
    print("año NO bisiesto")
"""
#bucle alumnos
"""
lista_alumnos=[]
cantidad=int(input("digame la cantidad de alumnos que hay: "))
for i in range(cantidad):
    apellido=input("ingrese el apellido: ")
    promedio=float(input("ingrese el promedio: "))
    datos=[apellido, promedio]
    lista_alumnos.append(datos)

for i in lista_alumnos:
    if i[1] >=4:
        print(f"el alumno {i[0]} esta aprobado")
    else:
        print(f"el alumno {i[0]} está reprobado")

diccionario={"materia": None, "turno": None, "profesor": None}
diccionario.setdefault("cursar")

for i in diccionario.items():
    nuevo=input("ingrese el valor de {i[0]}: ")
    diccionario.update({i[0]:nuevo})
print(diccionario)
"""
#consecionaria
"""
consecionaria con menu
menu:
carga de vehiculos
mostrar vehiculos
editar
eliminar 
salir
"""

class Vehiculo():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo 
        self.color = color
    
    def __str__(self):
        return f"El vehiculo es un {self.marca} {self.modelo}, de color {self.color} "
    
    def get_marca(self):
        return self. marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_color(self):
        return self.color
    
    def set_marca(self, marca):
        marca_editada = self.marca
        self.marca = marca
        return f"Se edito de: {marca_editada} a: {self.marca}"
    
    def set_modelo(self, modelo):
        modelo_editada = self.modelo
        self.modelo = modelo
        return f"Se edito de: {modelo_editada} a: {self.modelo}"
    
    def set_color(self, color):
        color_editada = self.color
        self.color = color
        return f"Se edito de: {color_editada} a: {self.color}"
   
class Terrestre(Vehiculo):
    def __init__(self, marca, modelo, color, motor, ruedas, combustible):
        super().__init__(marca, modelo, color)
        self.motor = motor
        self.ruedas = ruedas
        self.combustible = combustible
    
    def get_motor(self):
        return self.motor
    
    def get_ruedas(self):
        return self.ruedas
    
    def get_combustible(self):
        return self.combustible
    
    def set_motor(self, motor):
        motor_editada = self.motor
        self.motor = motor
        return f"Se edito de: {motor_editada} a: {self.motor}"
    
    def set_ruedas(self, ruedas):
        ruedas_editada = self.ruedas
        self.ruedas = ruedas
        return f"Se edito de: {ruedas_editada} a: {self.ruedas}"
    
    def set_combustible(self, combustible):
        combustible_editada = self.combustible
        self.combustible = combustible
        return f"Se edito de: {combustible_editada} a: {self.combustible}"
   
class Aereos(Vehiculo):
    def __init__(self, marca, modelo, color, propulsion, cantidad_tripulantes):
        super().__init__(marca, modelo, color)
        self.propulsion = propulsion
        self.cantidad_tripulantes = cantidad_tripulantes

    def get_propulcion(self):
        return self.propulsion
    
    def get_cantidad_tripulantes(self):
        return self.cantidad_tripulantes
    
    def set_propulcion(self, propulsion):
        propulsion_editada = self.propulsion
        self.propulsion = propulsion
        return f"Se edito de: {propulsion_editada} a: {self.propulsion}"
    
    def set_cantidad_tripulantes(self, cantidad_tripulantes):
        cantidad_tripulantes_editada = self.cantidad_tripulantes
        self.cantidad_tripulantes = cantidad_tripulantes
        return f"Se edito de: {cantidad_tripulantes_editada} a: {self.cantidad_tripulantes}"

class Maritimo(Vehiculo):
    def __init__(self, marca, modelo, color, nudos, turistico):
        super().__init__(marca, modelo, color)
        self.nudos = nudos
        self.turistico = turistico
    
    def get_nudos(self):
        return self.nudos
    
    def get_turistico(self):
        return self.turistico
    
    def set_nudos(self, nudos):
        edicion = self.nudos
        self.nudos = nudos
        return f"Se edito de: {edicion} a: {self.nudos} "
    
    def set_turistico(self, turistico):
        edicion = self.turistico
        self.turistico = turistico
        return f"Se edito de: {edicion} a: {self.turistico} "

def cargar_vehiculos():
    pass

def mostrar_vehiculos():
    pass

def editar_vehiculo():
    pass

def eliminar_vehiculo():
    pass

def salir():
    pass

def menu():
    print("Menu Principal")
    print("1) Cargar Vehiculos")
    print("2) Mostrar Vehiculos")
    print("3) Editar Vehiculo")
    print("4) Eliminar Vehiculo")
    print("5) Salir ")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        cargar_vehiculos()
    elif opcion == 2:
        mostrar_vehiculos()
    elif opcion == 3:
        editar_vehiculo()
    elif opcion == 4:
        eliminar_vehiculo()
    elif opcion == 5:
        salir()
