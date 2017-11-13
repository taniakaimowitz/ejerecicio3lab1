from random import randint
from datetime import datetime

stock = {'banana':5, 'apple':3, 'pear':2, 'cereal':8, 'milk':5, 'eggs':15}

price = {'banana':1.25, 'apple':0.95, 'pear':1.5, 'cereal':7.3, 'milk':5, 'eggs':2}


def compute_bill(lista):
    total = 0
    for x in lista:
        precio = price[x]
        if stock[x] > 0:
            total = total + precio
            stock[x] = stock[x] - 1
    print (total)

#Ejercicio 2 - c)
def compute_bill_2(lista):
    total = 0
    for x in lista:
        precio = price[x[0]]
        if stock[x[0]] >= x[1]:
            total = total + (precio * x[1])
            stock[x[0]] = stock[x[0]] - x[1]
    print (total)


def compute_bill_3(lista):
    total = 0
    numero_factura = randint(1, 1000)
    print ("Supermercado ABC")
    print ("Fecha: %s" % datetime.now())
    print ("Factura #: %s" % numero_factura)
    print ("Item \t Cantidad \t Precio \t Monto Total")
    for x in lista:
        precio = price[x[0]]
        producto = x[0]
        cant = x[1]
        if stock[producto] >= cant:
            total = total + (precio * cant)
            stock[producto] = stock[producto] - cant
            print (producto + " \t\t" + str(cant) + " \t\t" + str(precio) + " \t\t" + str(cant * precio)) 
    print ("Total %s" % total)
    print ("Impuestos %s" % str(total * 0.13))
