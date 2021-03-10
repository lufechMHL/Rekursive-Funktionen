#Luisa Fechner
#15. 05. 2020
#Rekursive Funktionen; NEU-Informatik-9a-003
#Aufgabe 6Z, Kombinatorik

#Fakultät
def faku(z):
    if z == 0:
        return 1
    else:
        return z*faku(z-1)

#Permutation ohne zurücklegen
def permO(n):
    return faku(n)

#Permutation mit zurücklegen
#def permM(n, r):
    #return faku(n) / faku(r) *

#Variation ohne zurücklegen
def variO(n, k):
    return faku(n) / faku(n-k)

#Variation mit zurücklegen
def variM(n, k):
    return n**k

#Kombination ohne zurücklegen
def binO(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return faku(n) / faku(k) * faku(n - k)

#Kombination mit zurücklegen
def binM(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return faku(n+k-1) / faku(k) * faku(n - k)


print("1 = Permutation ohne zurücklegen, 2 = Permutation mit zurücklegen,")
print("3 = Variation ohne zurücklegen, 4 = Variation mit zurücklegen,")
print("5 = Kombination ohne zurücklegen, 6 = Kombination mit zurücklegen")
w = float(input("Welche rechnung? "))
if w == 1:
    n = float(input("n= "))
    print(permO(n))
elif w == 2:
    n = float(input("n= "))
    r = float(input("r= "))
    print(permM(n))
elif w == 3:
    n = float(input("n= "))
    k = float(input("k= "))
    ergebnis = variO(n, k)
    print(ergebnis)

    
