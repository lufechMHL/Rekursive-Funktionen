#Luisa Fechner
#16. 05. 2020
#Rekursive Funktionen, Arythmetische Operationen
#Aufgabe 8, Neu-Informatik-9a-003

def NA(x):
    return x+1

def ADD(x,0):
    if y > 0:
        return NA(ADD(x,y-1))

def MUL(x,0)
    if y > 0:
        return ADD(x,MUL(x,y-1))

def POT(x,0):
    if y > 0:
        return MUL(x, POT(x, y-1))

x = int(input("x= "))
print (NA(x), ADD(x,0),MUL(x,0), POT(x,0))
