from math import *
from random import *

#Практическая работа (квадратное уровнение)

otsustama=input("Kas soovite selle taseme lahendada?").lower()
if otsustama=="jah":
    print("Ruutvõrrandi lahendamine")
    try:
        #a,b,c=map(float,input("a,d,c")).splite( ",")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b-sqrt(D))/2*a
            print("2 lahendust 1:{0:.2f},2:{1:.2f}".format(x1,x2))
        elif D==0:
            x1=(-b)/2*a
            print("1 lahendus {0:.2f}".format(x1))
        else:
            print("Lahendused puuduvad")
    except:
        print("Viga andmetüübiga")
else: 
    print("Hüvasti")

#1

n=float(input("введенное число"))
try:
   a=int(input("Sisesta arv"))
   if a>0:
        print(f"Positiivne")
      if a%2==0:
         print(f"{a} on paaritus")
      else:
         print(f"{a} on paaritu")
  else:
       print("Negatiivne")
except:
    print("Vale andmetüüp")
#2
a,b,c=map(float,input("a,b,c").split())
if a>0 and b> and c>0:
    if a+b+c==180:
        print("kolmnurk")
        if a==b==c:
            print("võrdkülgne")
        elif a==b or b==c or a==c
            print("võrdhaarne")
        else:
            print("erikülgne")
    else:
        print("Nurgad")
else:
    print("<0")
#3
v=input("Kas tahad 1-7 numberist saada päeva nimetus?")
if v.lower()=="jah":
    nr=int(input("Päeva number: "))
    if nr==1:
        p="esmaspäev"
    elif nr==2:
        p="teisipäev"
    elif nr==3
        p="kolmapäev"
    elif nr==4
        p="neljapäev"
    elif nr==5
        p="reede"
    elif nr==6
        p="laupäev"
    elif nr==7
        p="pühapäev"
    print(p)
    else: 
    p="on vaja 1-7"
except: 
    print("viga")

#4

