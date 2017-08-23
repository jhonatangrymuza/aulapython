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
num= "12345"
b = 1
print("Para votar digite apenas um numero")
print("1-Windows Server") 
print("2-Unix")
print("3-Linux ")
print("4-Netware" )
print("5-Mac OS") 
print("6-Outro")

while(b != 0):   
  b = int(input("digite o numero\n "))
    
  if (b == 1):
    w.append(b)
  elif(b == 2):
    u.append(b)
  elif(b == 3):
    l.append(b)
  elif(b == 4):
    n.append(b)
  elif(b == 5):
    m.append(b)
  elif(b == 6):
    o.append(b)
    
mediaw =0
for a in w:
  mediaw += a;
  mediaw /= len(w)
print("média dos saltos", mediaw)

mediau =0
for b in u:
  mediau += b;
  mediau /= len(u)
print("média dos saltos", mediau)

medial =0
for c in l:
  medial += c;
  medial /= len(l)
print("média dos saltos", medial)

median =0
for d in n:
  median += d;
  median /= len(n)
print("média dos saltos", median)

mediam =0
for e in m:
  mediam += e;
  mediam /= len(m)
print("média dos saltos", mediam)

mediao =0
for f in o:
  mediao += f;
  mediao /= len(o)
print("média dos saltos", mediao)
    
    
print("Sistemas operacionais    votos      %")
print("---------------------    -----      -----")

print("1-Windows Server         ",len(w)) 
print("2-Unix                   ",len(u))
print("3-Linux                  ",len(l))
print("4-Netware                ",len(n))
print("5-Mac OS                 ",len(m))
print("6-Outro                  ",len(o))

print("total",len(w,u,l,n,m,o))
      
      
      
      