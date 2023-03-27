""" 
Ejemplos:
Clases: Personas
    -Objeto: Persona1, persona2, etc.
    -Atributo: Orejon, edad, altura, etc.
    -Métodos: Como caminan, como hablan, etc. (acciones)  
"""
#Ej de clase para un producto
#Primera letra siempre en mayúscula y en singular
#inix
#abstraccion: debo evitar atributos q no sean necesarios para mi producto
#hay metodos q los podes crear vos y tb hay reservados de python
#self primero entre los parentecis del metodo es un representante del objeto 

class Producto():
    def __init__(self, tipo, nombre, precio, tamanio, stock): #es una funcion pero dentro de la clase es un método
            self.tipo = tipo
            self.nombre = nombre
            self.preci0 = precio
            self.tamanio = tamanio
            self.stock = stock

    def __str__(self):
        return f"El producto es una {self.tipo},{self.nombre}, tiene un valor de {self.preci0}, mide {self.tamanio} y hay en stock {self.stock}"
 #el sig metodo es creado por nosotros
    def get_caracteristica(self):
        return self.nombre 
 #esto es para q el usuario lo edite por algun caso especifico
    def set_nombre(self, nombre):
        nombre_editado = self.nombre
        self.nombre = nombre
        return f"Se modifico de: {nombre_editado} a: {self.nombre} "

producto1 = Producto("bebida", "prusw", "310", "2L", "8" )
producto2 = Producto("jueguete sexual", "vibraneitor 3000", "25000", "30cm", "1")
print(producto1)
nombre = input("Ingrese el nuevo nombre: ")
print(producto1.set_nombre(nombre))
print(producto1.get_caracteristica())
print(producto2)
print(producto1)