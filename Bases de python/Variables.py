
"""
No es recomendable declarar una variable usando:
-letras especificas del alfabeto como Ñ
-no intercalar mayusculas como aSAdO
-poner una mayus al principio (me chupa la pija)
"""
#el input sirve para pedir datos al usuario ej:

nombre=input("Diganos su nombre: ")
edad=input("Diganos su edad: ")
residencia=input("Diganos su residencia: ")

#tuplas: son variables con variables adentro, ej:
"""
los tipos de metodos para una tupla son
-len: para ver cuantos elementos hay dentro de una tupla
-index:nos da la ubicacion del indice de nuestro dato
los indices van del 0 hasta el infinito, ej:
persona("hola","si","vamos")
esta tiene los indices 0, 1 y 2
"""

persona=nombre, edad, residencia
#las , (comas) sirven para SEPARAR 
print("Hola",nombre,"como estas?, tu edad es de",edad,"años", "vives en", persona)
print(len(persona))
print=(persona)