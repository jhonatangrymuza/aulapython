'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
resp= []
print("pressione enter 2X para NÃO (s) para SIM")

for i in range(1):
      resp = input("Telefonou para a vítima?")
      resp = input("Esteve no local do crime?")
      resp = input("Mora perto da vítima?")
      resp = input("Devia para a vítima?")
      resp = input("Já trabalhou com a vítima?")
for i in range(1): 
  cont = 0 
  for i in range(1): 
    if (resp=='s' or resp=='S'): 
      cont = cont + 1 
      if(cont==2): 
          print("A pessoa" , i + 1 , "é suspeita")
      if(cont == 5): 
          print("A pessoa",i + 1,"é a assassina") 
      if(cont == 3 or cont ==4): 
          print("A pessoa",i + 1,"é cumplice") 
      if(cont <= 1) : 
          print("A pessoa",i + 1,"é inocente") 