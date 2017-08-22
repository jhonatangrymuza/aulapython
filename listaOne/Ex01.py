'''
Created on 17 de ago de 2017

@author: Jhonatan
'''
letra = []
vogal= "aeiou1234567890!@#$%¨&*()¨`´[]{}\'¬ºª;.?:,<>.+-*/\"\\~^§=ñ╗î³┌c[►◘_─○↓╚♥♦♣♠"
print("digite 10 letras")
for i in range(10):
  b = input(i+1)
  if len(b) > 1 :
    print("digite so uma letra")
  elif(b not in vogal):
    letra.append(b)

  
print(letra)
print(len(letra))
