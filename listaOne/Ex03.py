'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
i = 0
quad = 0
for elem in lista:
  soma = soma + elem

while i < len(lista):
  quad = quad + lista[i]+lista[i]
  i = i+1    
  
print("soma de todos os numeros",soma)
print("soma + elementos ao quadrado",quad)