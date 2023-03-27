#Funciones, "dry" dont repeat yourself. ej:
"""
def ouShet():
    nombre=input("decime tu nombre pa: ")
    print(f"bienvenid@", nombre, "a las clases de tu vieja")
    print("mi nombre no te lo voy a decir porq soy anonimous")
    print("cerra el orto")
#para usarla, hay q invocarla, las veces q vos quieras
ouShet()
#podemos ponerles variables dentro
"""
#en las funciones, en este caso num1 y num2 no son variables, son
#son argumentos, por lo cual al final en vez de poner num1 y num2 pordemos poner x e y 
"""
def cuentasMatematicas(num1, num2):
    suma=num1+num2
    resta=num1-num2
    multiplic=num1*num2
    division=num1/num2
    print(f"resultados: \nSuma: ", suma,"\nresta:", resta, "\nmultiplicacion:", multiplic, "\ndivision:", division)
num1=int(input("ingresa un num entero puto: "))
num2=int(input("ingresa otro num entero: "))
cuentasMatematicas(num1,num2)
"""
#listas en funciones
"""
def escribir(lista):
    for i in lista:
        print(i)
listaLoca=["milanes","fideo","estrés"]
escribir(listaLoca)
"""
#return en funciones
"""
def *nombre de la funcion*(*variables*):
    *codigo que ejecuta*
    return *valor a devolver*
"""
"""
def promedios (nota1,nota2,nota3):
    resultpromedio=(nota1+nota2+nota3)/3
    return resultpromedio

def aprobado(promedios):
    if promedios >=6:
        print("el alumno aprobó")
    else:
        print("el alumno reprobó")

num1=int(input("ingrese primera nota del alumno: "))
num2=int(input("ingrese otra nota del alumno: "))
num3=int(input("ingrese otra nota del alumno: "))
resultpromedios=promedios(num1,num2,num3)

aprobado(resultpromedios)
"""
#crear una lista/bucle con return
"""
def misCompras(numero):
    lista_decompras=[]
    for i in range(numero):
        articulo=input("ingrese un articulo: ")
        lista_decompras.append(articulo)
    return lista_decompras

numero=int(input("diga la cantidad de articulos que desea cargar: "))
lista=misCompras(numero)
print(lista)
"""
#funciones con varios returns
"""
def promedios(nota1,nota2,nota3):
    resultado=(nota1+nota2+nota3)/3
    if resultado >=6:
        return "aprobado"
    else:
        return "debe recuperar"

notaslocas=promedios(7,3,10)
print(notaslocas)
"""
#concepto de scope:
"""
def suma(num1,num2):
    resultado=num1+num2
    print(resultado)
n1=4
n2=10
suma(n1,n2)
"""
"""
1) una variable LOCAL (una variable dentro de una funcion), si no estpa declarada
dentro de una funcion al momento q la creamos o si no esta declarada como argumento
en la funcion, puede ser utilizada por una variable global
SIEMPRE Y CUANDO TENGA EL MISMO NOMBRE Y SE DECLAREN ANTES DE INVOCAR LA FUNCION

2) Una variable LOCAS no pde ser ejecutada o invocada fuera de la funcion
"""
#POO (programacion orientada a objetos)
"""
clase: molde de donde creamos los objetos, osea, la base para crear un objeto
-objeto: creacion a partir de una clase
-atributo: caracteristicas que tendra este objeto creado
-métodos: es la instruccion q se le da a un objeto, para determinar su comportamiento

class Plastilina():

def __init__(self):
    self.color=
    self.tamanio=

gallina=Plastilina("blanco",40)
"""
