"""
consecionaria con menu
menu:
carga de vehiculos
mostrar vehiculos
editar
eliminar 
salir
"""

vehiculos = []
terrestres = []
aereos = []
maritimos = []

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
   
class Aereo(Vehiculo):
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
    print("Menu de carga de vehiculos")
    print("1) Terrestre")
    print("2) Aereo")
    print("3) Maritimo")
    print("4) Volver al menu principal")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        #marca, modelo, color, motor, ruedas, combustible)
        marca = input("Ingrese la marca del Vehiculo: ")
        modelo = input("Ingrese el modelo del Vehiculo: ")
        color = input("Ingrese el color del Vehiculo: ")
        motor = input("Ingrese el motor del Vehiculo: ")
        ruedas = input("Ingrese la cantidad de ruedas del Vehiculo: ")
        combustible = input("Ingrese el combustible del Vehiculo: ")
        vehiculo = Terrestre(marca, modelo, color, motor, ruedas, combustible)
        vehiculos.append(vehiculo)
        terrestres.append(vehiculo)
        print(f"Se cargo con exito a: {marca}")
        print("Lo derivamos al menu principal")
        return menu()

    elif opcion == 2:
        #marca, modelo, color, propulsion, cantidad_tripulantes
        marca = input("Ingrese la marca del Vehiculo: ")
        modelo = input("Ingrese el modelo del Vehiculo: ")
        color = input("Ingrese el color del Vehiculo: ")
        propulsion = input("Ingrese la propulsion del Vehiculo: ")
        cantidad_tripulantes = input("Ingrese la cantidad de tripulantes del Vehiculo: ")
        vehiculo = Aereo(marca, modelo, color, propulsion, cantidad_tripulantes) 
        vehiculos.append(vehiculo)
        aereos.append(vehiculo)
        print(f"Se cargo con exito a: {marca}")
        print("Lo derivamos al menu principal")
        return menu()
    elif opcion == 3:
        #marca, modelo, color, nudos, turistico
        marca = input("Ingrese la marca del Vehiculo: ")
        modelo = input("Ingrese el modelo del Vehiculo: ")
        color = input("Ingrese el color del Vehiculo: ")
        nudos = input("Ingrese los nudos de velocidad del Vehiculo: ")
        turistico = input("Ingrese si el Vehiculo es turistico (S/N): ")
        if turistico == "si" or turistico == "S":
            turistico = True
        elif turistico == "no" or turistico == "N":
            turistico = False
        else:
            print("No se entendio lo ingresado, por favor ingrese de nuevo")
            return cargar_vehiculos()

        vehiculo = Maritimo(marca, modelo, color, nudos, turistico)
        vehiculos.append(vehiculo)
        maritimos.append(vehiculo)
        print(f"Se cargo con exito a: {marca}")
        print("Lo derivamos al menu principal")
        return menu()
    elif opcion == 4:
        print("Lo derivamos al menu principal")
        return menu()
    else:
        print("Opcion no valida, intentelo de nuevo")
        return cargar_vehiculos()
    
def mostrar_vehiculos():
    if len(vehiculos) == 0:
        print("No hay vehiculos para mostrar")
        print("lo derivamos al menu principal")
        return menu()
    else:
        for valor_lista in vehiculos:
            print(f"{vehiculos.index(valor_lista)})  {valor_lista.get_marca()} {valor_lista.get_modelo()}")
        
        print("Estos son los Vehiculos cargados hasta el momento")
        print("Lo derivamos al menu principal")
        return menu()

def editar_vehiculo():
    if len(vehiculos) == 0:
        print("No hay vehiculos para mostrar")
        print("lo derivamos al menu principal")
        return menu()
    else:
        print("Menu de Edicion de vehiculos")
        print("1) Terrestre")
        print("2) Aereo")
        print("3) Maritimo")
        print("4) Volver al menu principal")
        tipo_vehiculo = int(input("Ingrese la opcion deseada: "))
        if tipo_vehiculo == 1:
            for valor_terrestre in terrestres:
                print(f"{terrestres.index(valor_terrestre)})  {valor_terrestre.get_marca()} {valor_terrestre.get_modelo()}")
            
            stop = len(terrestres) - 1
            opcion = int(input(f"Ingrese el indice del vehiculo para editar entre 0 y {stop} "))
            if opcion >= len(terrestres) and opcion < 0:
                print("La opcion ingresada no corresponde, intentelo de nuevo")
                return editar_vehiculo()
            else: 
                vehiculo_elegido = terrestres[opcion]
                #marca, modelo, color, motor, ruedas, combustible)
                print("1) Marca")
                print("2) Modelo")
                print("3) Color")
                print("4) Motor")
                print("5) Ruedas")
                print("6) Combustible")
                print("7) Volver al menu principal")
                opcion_atributo = int(input("Ingrese la opcion deseada: "))
                if opcion_atributo == 1:
                    marca = input("Ingrese la nueva marca: ")
                    print(vehiculo_elegido.set_marca(marca))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 2:
                    modelo = input("Ingrese el nuevo modelo: ")
                    print(vehiculo_elegido.set_modelo(modelo))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 3:
                    color = input("Ingrese el nuevo color: ")
                    print(vehiculo_elegido.set_color(color))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 4:
                    motor = input("Ingrese el nuevo motor: ")
                    print(vehiculo_elegido.set_motor(motor))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 5:
                    ruedas = input("Ingrese la nueva cantidad de ruedas: ")
                    print(vehiculo_elegido.set_ruedas(ruedas))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 6: 
                    combustible = input("Ingrese el nuevo combustible: ")
                    print(vehiculo_elegido.set_combustible(combustible))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 7:
                    print("Lo derivamos al menu principal")
                    return menu()
        elif tipo_vehiculo == 2:
            for valor_aereo in aereos:
                print(f"{aereos.index(valor_aereo)})  {valor_aereo.get_marca()} {valor_aereo.get_modelo()}")
            
            stop = len(aereos) - 1
            opcion = int(input(f"Ingrese el indice del vehiculo para editar entre 0 y {stop} "))
            if opcion >= len(aereos) and opcion < 0:
                print("La opcion ingresada no corresponde, intentelo de nuevo")
                return editar_vehiculo()
            else: 
                vehiculo_elegido = aereos[opcion]
                #marca, modelo, color, propulsion, cantidad_tripulantes
                print("1) Marca")
                print("2) Modelo")
                print("3) Color")
                print("4) Propulsion")
                print("5) Cantidad de Tripulantes")
                print("6) Volver al menu principal")
                opcion_atributo = int(input("Ingrese la opcion deseada: "))
                if opcion_atributo == 1:
                    marca = input("Ingrese la nueva marca: ")
                    print(vehiculo_elegido.set_marca(marca))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 2:
                    modelo = input("Ingrese el nuevo modelo: ")
                    print(vehiculo_elegido.set_modelo(modelo))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 3:
                    color = input("Ingrese el nuevo color: ")
                    print(vehiculo_elegido.set_color(color))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 4:
                    propulsion = input("Ingrese la nueva propulsion: ")
                    print(vehiculo_elegido.set_motor(propulsion))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 5:
                    cantidad_tripulantes = input("Ingrese la nueva cantidad de tripulantes: ")
                    print(vehiculo_elegido.set_ruedas(cantidad_tripulantes))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 6:
                    print("Lo derivamos al menu principal")
                    return menu()
        elif tipo_vehiculo == 3:
            for valor_maritimo in maritimos:
                print(f"{maritimos.index(valor_maritimo)})  {valor_maritimo.get_marca()} {valor_maritimo.get_modelo()}")
            
            stop = len(maritimos) - 1
            opcion = int(input(f"Ingrese el indice del vehiculo para editar entre 0 y {stop} "))
            if opcion >= len(maritimos) and opcion < 0:
                print("La opcion ingresada no corresponde, intentelo de nuevo")
                return editar_vehiculo()
            else: 
                vehiculo_elegido = maritimos[opcion]
                #marca, modelo, color, nudos, turistico
                print("1) Marca")
                print("2) Modelo")
                print("3) Color")
                print("4) Nudos")
                print("5) Turistico")
                print("6) Volver al menu principal")
                opcion_atributo = int(input("Ingrese la opcion deseada: "))
                if opcion_atributo == 1:
                    marca = input("Ingrese la nueva marca: ")
                    print(vehiculo_elegido.set_marca(marca))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 2:
                    modelo = input("Ingrese el nuevo modelo: ")
                    print(vehiculo_elegido.set_modelo(modelo))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 3:
                    color = input("Ingrese el nuevo color: ")
                    print(vehiculo_elegido.set_color(color))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 4:
                    nudos = input("Ingrese la nueva cantidad de nudos de velocidad: ")
                    print(vehiculo_elegido.set_motor(nudos))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 5:
                    turistico = input("Ingrese si el Vehiculo es turistico (S/N): ")
                    print(vehiculo_elegido.set_ruedas(turistico))
                    print("Lo derivamos al menu principal")
                    return menu()
                elif opcion_atributo == 6:
                    print("Lo derivamos al menu principal")
                    return menu()
        elif tipo_vehiculo == 4:
            print("Lo derivamos al menu principal")
            return menu()
        else: 
            print("La opcion ingresada es incorrecta, intentelo de nuevo")
            print("Lo derivamos al menu de edicion")
            return editar_vehiculo()

def eliminar_vehiculo():
    if len(vehiculos) == 0:
        print("No hay vehiculos para mostrar")
        print("Lo derivamos al menu principal")
        return menu()
    else:
        for valor_lista in vehiculos:
            print(f"{vehiculos.index(valor_lista)})  {valor_lista.get_marca()} {valor_lista.get_modelo()}")
        
        opcion_vehiculo = int(input("Ingrese el indice del vehiculo que quiere eliminar"))
        vehiculo_elegido = vehiculos[opcion_vehiculo]
        vehiculos.pop(opcion_vehiculo)
        print(f"Se elimino a: {vehiculo_elegido}, con exito")
        print("Lo derivamos al menu principal")
        return menu()

def salir():
    print("Gracias por visitar la consecionaria")

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

print("Bienvenido a nuestra consecionaria")
menu()    