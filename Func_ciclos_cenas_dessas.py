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

def n_esimo_primo(n):
    i = 0
    num = 1
    while i < n:
        if primo(num):
            i += 1
        num += 1
    return num - 1
print(primo(5))
print(primo(6))
"""
#ex38
"""

from math import floor

#h = dia da semana
#q = dia do mes
#m = mes (1/2/3... /12)
#K = ano do seculo (ano mod 100)
#J é o seculo

def dia_da_semana(day, month, year):

    h = exc_formula(day, month, year % 100, floor(year / 100))
    return weekday_to_string(h)


def exc_formula(q, m, K, J):
    return (q + floor(13 * (m + 1) / 5) + K + floor(K/4) + floor(J / 4) - 2 * J) % 7 

def weekday_to_string(weekday):
    if (weekday == 0):
        return "Sabado"
    if (weekday == 1):
        return "Domingo"
    if (weekday == 2):
        return "Segunda"
    if (weekday == 3):
        return "Terça"
    if (weekday == 4):
        return "Quarta"
    if (weekday == 5):
        return "Quinta"
    if (weekday == 6):
        return "Sexta"
    raise ValueError("Ta mal brother (invalid weekday)")

print(dia_da_semana(28, 10, 2025))
    
"""

#ex39

"""
def misterio(n):
    ni = invertNumber(n)
    ns = abs(n - ni)
    if ns < 100:
        return "Condições não verificadas"
    nsi = invertNumber(ns)
    return ns + nsi

def invertNumber(num):
    newNum = 0
    while num > 0:
        newNum = newNum * 10 + num % 10
        num //= 10
    return newNum

print(misterio(246))    

"""

#ex40
"""
soma = 0

for i in range(20, 0, -2):
    soma += 1

print('Soma =', soma)
"""

#ex49
"""
from math import ceil

def codifica(string):
    str1 = ''
    str2 = ''

    for i in range (0 , len(string)):
            if i % 2 == 0:
                  str1 += string[i]
            else:
                  str2 += string[i]
    return str1 + str2

def decodifica(string):
    result = ''
    middle = ceil(len(string) / 2)

    for i in range (middle):
          result += string[i]
          if i + middle < len(string):
                result += string[i + middle]
    return result
      

print(decodifica('acebfd'))
"""

#ex 57
"""
def seq_racaman(n):
    res = []
    
    for i in range(n): 
        if i == 0:
            res += [0]
            continue
        last_item = res[i - 1]
        if last_item > i and last_item - i not in res:
            res += [last_item - i]
        else:
            res += [last_item + i]    
    return res

# EXEMPLO DE EXECUÇÃO PASSO A PASSO:
# i = 0: res = [0]
# i = 1: last_item = 0, 0 > 1? Não → 0 + 1 = 1 → [0, 1]
# i = 2: last_item = 1, 1 > 2? Não → 1 + 2 = 3 → [0, 1, 3]
# i = 3: last_item = 3, 3 > 3? Não → 3 + 3 = 6 → [0, 1, 3, 6]
# i = 4: last_item = 6, 6 > 4? Sim e 6-4=2 não está em res → 6-4=2 → [0, 1, 3, 6, 2]

print(seq_racaman(15))
"""
#ex 58
from random import random
 

def random_to(n):
    # o round vai arredondar o numero random
    return round(random() * n)

def euromilhoes():
    list1 = []
    while len(list1) < 5:
        r = random_to(50)
        #se o numero anterior nao tiver na lista ele acrescenta
        if r not in list1:
            list1 += [r]
    list2 = []
    while len(list2) < 2:
        r = random_to(12)
        if r not in list2:
            list2 += [r]        
    return [list1, list2]
    
print(euromilhoes())

