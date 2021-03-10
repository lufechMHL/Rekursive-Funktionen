#Luisa Fechner
#15. 05. 2020
#Rekursive Funktionen; NEU-Informatik-9a-003
#Aufgabe 4, ggT ermitteln

def ggT2(x, y):
    if y == 0:
        return x
    else:
        return ggT2(y, x%y)

a = 12
b = 40
g = ggT2(a, b)
print(g)
