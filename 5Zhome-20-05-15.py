#Luisa Fechner
#15. 05. 2020
#Rekursive Funktionen; NEU-Informatik-9a-003
#Aufgabe 5, Binominalkoeffizienten

def faku(z):
    if z == 0:
        return 1
    else:
        return z*faku(z-1)

def bin(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return faku(n) / faku(k) * faku(n - k)

n = float(input("n= "))
k = float(input("k= "))
print (bin(n, k))
