#pilares de la programacion, son 4 hoy damos
#Abstraccion: no poner valores q no necesitas
#Encapsulamiento: es para q el usuario no pda acceder a un metodo
#esto se utiliza haciendo __ adelamte de una palabra por ej: 
"""
class Producto():
    def __get_nombre(self):
"""
#Herencia: Se utiliza para no repetir codigo en class
"""
class Producto():
    def __init__(self, tipo, nombre, precio, tamanio, stock): #es una funcion pero dentro de la clase es un método
            self.tipo = tipo
            self.nombre = nombre
            self.preci0 = precio
            self.tamanio = tamanio
            self.stock = stock

    def __str__(self):
        return f"El producto es una {self.tipo}, {self.nombre}, tiene un valor de {self.preci0}, mide {self.tamanio} y hay en stock {self.stock}"

    def get_nombre(self):
        return self.nombre 

    def get_tipo(self):
        return self.tipo 

    def get_precio(self):
        return self.preci0
    
    def get_tamanio(self):
        return self.tamanio

    def get_stock(self):
        return self.stock

    def set_nombre(self, nombre):
        nombre_editado = self.nombre
        self.nombre = nombre
        return f"Se modifico de: {nombre_editado} a: {self.nombre} "

    def set_tipo(self, tipo):
        tipo_editado = self.tipo
        self.tipo = tipo
        return f"Se modifico de: {tipo_editado} a: {self.tipo} "

    def set_preci0(self, preci0):
        preci0_editado = self.preci0
        self.preci0 = preci0
        return f"Se modifico de: {preci0_editado} a: {self.preci0} "

    def set_tamanio(self, tamanio):
        tamanio_editado = self.tamanio
        self.tamanio = tamanio
        return f"Se modifico de: {tamanio_editado} a: {self.tamanio} "

    def set_stock(self, stock):
        stock_editado = self.stock
        self.stock = stock
        return f"Se modifico de: {stock_editado} a: {self.stock} "

class Bebidas(Producto):
    def __init__(self, tipo, nombre, precio, tamanio, stock, sabor, light):
        super().__init__(tipo, nombre, precio, tamanio, stock) 
        self.sabor = sabor
        self.light = light

    def get_sabor(self):
        return self.sabor

    def get_light(self):
        return self.light

    def set_sabor(self, sabor):
        sabor_editado = self.sabor
        self.sabor = sabor
        return f"se modifico de: {sabor_editado} a: {self.sabor} "

    def set_light(self, light):
        light_editado = self.light
        self.light = light
        return f"Se modifico de: {light_editado} a: {self.light} "
    
producto = Bebidas("Gasificada","cocatrucha","250pe","2L","5 enm el mundo","dulceloco","True")
print(producto)
print(producto.get_nombre())
"""
#Polimorfismo: es para que los metodos se puedan usar a la misma vez
class Pantera():
    def correr(self):
        return "corre a una velocidad de 50 km"
    def comer(self):
        return "Carne"
    
class Tortuga():
    def correr(self):
        return "corre a una velocity de 3 km"
    def comer(self):
        return "Verduras"

class Conejo():
    def correr(self):
        return "corre a una velocidad de 15 km"

    def comer(self):
        return "verduras procesadas"
        
def animal_corre(animal):
    print(animal.correr())

def animal_come(animal):
    print(animal.comer())
animal1 = Pantera()
animal2 = Tortuga()
animal3 = Conejo()

animales = [animal1,animal2,animal3]

for x in animales:
    animal_corre(x)
    print("Y tambien come")
    animal_come(x)

