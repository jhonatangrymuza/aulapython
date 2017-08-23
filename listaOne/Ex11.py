'''
Created on 23 de ago de 2017

@author: Jhonatan
'''

w = []
u = []
l = []
n = []
m = []
o = []
b = 1

print("Para votar digite apenas um numero")
print("1-Windows Server") 
print("2-Unix")
print("3-Linux ")
print("4-Netware" )
print("5-Mac OS") 
print("6-Outro")

while(b != '0'):   
  b =input("digite o numero\n")
  if(b in '0123456'):
    if (b == '1'):
      w.append(b)
    elif(b == '2'):
      u.append(b)
    elif(b == '3'):
      l.append(b)
    elif(b == '4'):
      n.append(b)
    elif(b == '5'):
      m.append(b)
    elif(b == '6'):
      o.append(b)
  else:
    print("digite so os numeros 1,2,3,4,5\n\n")

total= len(w) +len(u) + len(l) + len(n) + len(m) +len(o)
porw = (len(w) / total) * 100
porw -= porw % 1;

poru = (len(u) / total) * 100
poru -= poru % 1;

porl = (len(l) / total) * 100
porl -= porl % 1;

porn = (len(n) / total) * 100
porn -= porn % 1;

porm = (len(m) / total) * 100
porm -= porm % 1;

poro = (len(o) / total) * 100
poro -= poro % 1;
print("\n\nSistemas operacionais    votos          %%%%% ")
print("---------------------    -----        ---------")

print("1-Windows Server         ",len(w),'          ', porw,'%') 
print("2-Unix                   ",len(u),'          ', poru,'%')
print("3-Linux                  ",len(l),'          ', porl,'%')
print("4-Netware                ",len(n),'          ', porn,'%')
print("5-Mac OS                 ",len(m),'          ', porm,'%')
print("6-Outro                  ",len(o),'          ', poro,'%')
print("---------------------    --------")
print("Total                    ",total)

      
      