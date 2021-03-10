#Luisa Fechner
#15. 05. 2020
#Rekursive Funktionen; NEU-Informatik-9a-003

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

zahl = int(input("Zahl: "))
ergebnis = fib(zahl)
print(zahl, ergebnis)

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        z = 2
        w1 = 0
        w2 = 1
        while z <= n:
            summe = w1 + w2
            z = z + 1
            w1 = w2
            w2 = summe
        return summe

zahl = int(input("Zahl: "))
ergebnis = fib2(zahl)
print(zahl, ergebnis)
