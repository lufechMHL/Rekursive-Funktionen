#Luisa Fechner
#15. 05. 2020
#Rekursive Funktionen; NEU-Informatik-9a-003

def faku(n):
    if n == 0:
        return 1
    else:
        return n*faku(n-1)

#zahl = 5
#ergebnis = faku(zahl)
#print(zahl, ergebnis)

def sum(z):
    if z == 0:
        return 0
    else:
        return z + sum(z-1)

zahl = 6
ergebnis = sum(zahl)
print(zahl, ergebnis)

