'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
def inter(i,ii, iii):
    interda = []
    for a,b,c in zip(i, ii,iii):
        interda.append(a)
        interda.append(b)
        interda.append(c)
    return interda

lista1 = [0,1,2,3,4,5,6,7,8,9]
lista2 = [10,11,12,13,14,15,16,17,18,19]
lista3 = [20,21,22,23,24,25,26,27,28,29]

listainterda = inter(lista1, lista2, lista3)

for i in listainterda:
    print(i, end=", ")