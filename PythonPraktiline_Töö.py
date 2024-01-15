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


