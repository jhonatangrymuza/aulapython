'''
Created on 23 de ago de 2017

@author: Jhonatan
'''
salt = []
a = ""
a = input("Atleta\n")
media= 0

for i in range(5):
  b = float(input("digite a distancia do salto\n "))
  salt.append(b)

print("\n")

u = 1
for j in salt:
  media += j;
  print("salto",u,"=",j)
  u = u + 1
  media /= len(salt)
print("\nAtleta:",a,"\n")  
print("Saltos", salt)
print("média dos saltos", media)