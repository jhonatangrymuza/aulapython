'''
Created on 18 de ago de 2017

@author: Jhonatan
'''
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura= []
media = 0
acima = {}
for i in range(12):
  temperatura.append(float(input("qual a temperatura \n" + meses[i])))
  media +=temperatura[i]
media = media/len(meses)
for i in range(len(meses)):
  if(temperatura[i] > media):
    acima.update({meses[i] : temperatura[i]})
print("temperatura anual "+ str(media))
print("meses acima da media " + str(acima))