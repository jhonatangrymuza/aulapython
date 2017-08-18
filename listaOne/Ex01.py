'''
Created on 17 de ago de 2017

@author: Jhonatan
'''
letra = []
vogal= ['a','e','i','o','u']
print("digite 10 letras")
for i in range(10):
  b = input(i+1)
  if len(b) > 1 :
    print("digite so uma letra")
  elif(b not in vogal):
    letra.append(b)

  
print(letra)
