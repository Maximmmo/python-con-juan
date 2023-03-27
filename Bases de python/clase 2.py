#temas
"""
---Listas y diccionario: similar a tupla salvo que acá podemos agregar y quitar elementos y en la tupla no. Se usa [] y tambien tiene indices
---condicionales
---bucles repetitivos
"""
#Ej de lista:

listaDeCompras=["arroz", "milanesas", "fideos"]
#existen muchos metodos de lista como:
"""
append() agrega un elemento a la lista
clear() elimina todos los elementos
copy() devuelve una copia de la lista
count() cuenta los elementos repetidos de la lista
extend() agega elementos de una lista al final de la lista actual
index() devuelve el indice del primer elemento
insert() agrega un alemento en la posicion especificada
pop() remueve el elemento en la posicion especificada
remove() remueve el elemento con el valor especificado
reverse()invierte el orden de la lista
sort() ordena la lista
"""

"""
#los que mayormente se usan son agregar, encontrar, actualizar y borrar
#agregar:
listaDeCompras.append("sal")
print(listaDeCompras)

listaDeCompras.insert(2, "Pure instantaneo")
print(listaDeCompras)

#eliminar elementos:
listaDeCompras.remove("fideos")
print(listaDeCompras)

listaDeCompras.pop(0)
print(listaDeCompras)

listaDeCompras.clear()
print(listaDeCompras)
"""

"""
#diccionario:, estos se usan por ej en los formularios de google
auto={"marca":"fiat","modelo":600, "anio":1990}
print(auto.get("marca")) #devuelve el valor de la llave
print(auto.keys()) #devuelve todas las llaves existentes
print(auto.values()) #devuelve todos los valores existentes
print(auto.items()) #devuelve las llaves con sus valores separados

#agregar o actualizar datos en el diccionario
auto.setdefault("color" , "rojo") #agregas una llave sola o con un valor, no actualiza
print(auto)

auto.update({"color":"verde"}) #cambias el valor de la llave, lo pde actualizar
print(auto)

#eliminar en un diccionario
auto.pop("modelo") #elimina una llave
auto.popitem() #elimina la ultima llave
auto.clear() #elimina todas las llaves y sus valores
print(auto)
"""


#BUCLEEEEES
#bucle while: se utiliza hasta q una opcion sea verdadera, como por ejemplo una adivinanza

"""
respuesta=90
while respuesta != 53:
    respuesta=int(input("¿Cuantas lunas tiene saturno?: "))
    if respuesta == 53:
        print("muy bien")
    else:
        print("no lo es, intenta otra vez")
"""
#bucle for
"""
for indice in listaDeCompras:
    print(indice)
"""
#rango numerico
"""
final=10 #posicion de finalizacion de bucle
inicio=2 
for i in range(inicio,final):
    print(i)
"""
#cargar una lista de articulos
"""
lista=[]
cantidad=int(input("ingrese la cant de art q queres llevar al super: "))
for i in range(cantidad):
    articulo=input("ingrese cuales son esos articulos:")
    cantidad=int(input("cuantos de estos art vas a llevar: "))
    datos=(articulo, cantidad)
    lista.append(datos)
print(lista)
"""



print("sexo")