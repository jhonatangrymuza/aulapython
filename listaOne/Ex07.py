'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
resp = 0
print("responda as questoes a baixo com 0,1,2,3,4 e 5 lembre-se so coloque as que forem verdadeiras pois isso é um julgamento\n")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print("Telefonou para a vítima?\n")
print("Esteve no local do crime?\n")
print("Mora perto da vítima?\n")
print("Devia para a vítima?\n")
print("Já trabalhou com a vítima?\n")
for i in range(1):
  resp = int(input()) 
  if(resp <= 1): 
    print("A pessoa é inocente") 
  if(resp==2): 
    print("A pessoa é suspeita")
  if(resp == 3 or resp == 4): 
    print("A pessoa é cumplice") 
  if(resp == 5): 
    print("A pessoa é a assassina MEIRINHO PRENDA ELA") 
      
