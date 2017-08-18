'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
def inter(i,ii):
    interda = []
    for a,b in zip(i, ii):
        interda.append(a)
        interda.append(b)
    return interda

lista1 = [0,1,2,3,4,5,6,7,8,9]
lista2 = [10,11,12,13,14,15,16,17,18,19]


listainterda = inter(lista1, lista2)

for i in listainterda:
    print(i, end=", ")