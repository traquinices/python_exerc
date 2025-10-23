##FUNCOES, CICLOS E CENAS DESSAS
#exer29
"""
def cinco(num):
    return num == 5

print(cinco(4))    
"""

#exer30
"""
def horas_dias(num):
    return num / 24

print(horas_dias(48))
"""

#exer31
"""
def area_circ(raio):
    return 3.14 * (raio * raio)

print(area_circ(3))

"""

#exer32
"""
def area_circ(raio):
    return 3.14 * (raio * raio)

def area_croa(r1, r2):
    if r1 > r2:
        raise ValueError("Ta mal")
    return area_circ(r2) - area_circ(r1)

print(area_circ(3))
print(area_croa(10,30))
"""


#exer33
"""
def bissexto(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print(bissexto(2000))

"""

#exer34
"""
def bissexto(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def dia_mes(month, year):
    if month == "jan" or month == "mar" or month == "mai" or month == "jul" or month == "aug" or month == "out" or month == "dez":
        return 31
    if month == "feb":
        if bissexto(year):
            return 29
        return 28
    if month == "abr" or month == "jun" or month == "set" or month == "nov":
        return 30
    raise ValueError("Invalid month")

print(dia_mes('mar', 2017))
"""

#exer35
"""
## q = Quantia depositada; j = juros(0 a 1); n = n de anos
#a
def valor(q, j, n):
    if (j < 0 or j > 1):
        raise ValueError("ta mal")
    juros = q * ((1 + j) ** n)
    return juros

print(valor(100, 0.03, 4))
#b
## o n é quantos anos até duplicar o guito
def dublicar(q, j):
    n = 0
    while True:
        n +=1
        if valor(q, j, n) >= q * 2:
            return n
print(dublicar(100, 0.03))

"""

#exer36
"""
from math import sqrt

def primo(num):
    if (num <= 1):
        return False
    i = 2
    raizNum = sqrt(num)
    
    while i <= raizNum:
        if num % i == 0:
            return False
        i += 1

    return True    

print(primo(5))
print(primo(6))
"""

#exec37
