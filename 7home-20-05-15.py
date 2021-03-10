#Luisa Fechner
#16. 05. 2020
#Rekursive Funktionen, Dualzahlen erzeugen
#Aufgabe 7, Neu-Informatik-9a-003

def dual(zahl):
    ganz = zahl // 2
    rest = zahl % 2
    if rest == 0:
        zeichen = "0"
    else:
        zeichen = "1"
    if ganz == 0:
        return zeichen
    else:
        return dual(ganz) + zeichen

n = int(input("Zahl: "))
print (dual(n))
