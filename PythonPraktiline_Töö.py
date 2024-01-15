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
from math import *
a=float(input("напишите число => *"))
b=float(input("напишите число => *"))
v=float(input("напишите число => *"))
try:
    if(a,b,c)>0:
        print()
    if a,b,c
#3
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
#4
