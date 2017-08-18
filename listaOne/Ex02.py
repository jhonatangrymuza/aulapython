'''
Created on 17 de ago de 2017

@author: Jhonatan
'''
vetu = []
par = []
impar = []

print("digite 20 numeros");
for i in range(20):
  b = input(i+1)
  if int(b) % 2==0:
    par.append(b)
    vetu.append(b)
  else:
    impar.append(b)
    vetu.append(b)
    
  
print("vetor com todos os numeros",vetu)
print("vetor com todos os numeros pares ",par)
print("vetor com todos os numeros impares ",impar)