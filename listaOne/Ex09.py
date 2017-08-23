'''
Created on 23 de ago de 2017

@author: Jhonatan
'''
num = 0
b = 0

for i in range(1):
  num = int(input("digite quanto o vendedor vendeu\n "))
  if num >= 3000:
    num =  ((num*9)/100) +num+ 200
  elif(num < 3000):
    num =  ((num*9)/100) + num
print("o vendedor vendedor vendeu :R$",num)
  
