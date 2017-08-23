'''
Created on 21 de ago de 2017

@author: Jhonatan

num = []
a = '-l'
print("digite um numero\n ")
while(num != a):   
  num.append()
print(len(num))
print('B)'+ num)
'''
num = []
b = 0

while(b != -1):   
    b = int(input("digite um numero\n "))
    if b != -1:
        num.append(b)

  
print("quantidade de numeros informados: \n",len(num))
print("ordem dos numeros informados \n",num)  
print("ordem inversa: \n", sorted(num, reverse=True))
print("Soma dos valores: \n", sum(num))
media = 0
menor = 0

for i in num:
  media += i;
  if(i < 7):
    menor+=1;

media /= len(num)
maior = 0
for i in num:
  if(i > media):
    maior+=1
  
  
print("media dos numeros informados:\n ", media)
print("numeros acima da media :\n ", maior)
print("numeros informados abaixo de 7:\n ", menor)
print("acabou kkk")