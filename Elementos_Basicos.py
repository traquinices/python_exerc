#exer 9
"""
print('Insere 2 valores: ')
x = eval(input('Escreve o valor de x: , x = '))
y = eval(input('Escreve o valor de y: , y = '))
k = (x + 3 * y) * (x - y)
print(k)
"""

#exer10
"""
print('Da me a distancia e o tempo')
distance = eval(input('Distancia(em Km) = '))
time = eval(input('time(em minutos) = '))
timeHour = time / 60
timeSec = time * 60

distanceMetros = distance * 1000

velA = distance / timeHour
velB = distanceMetros / timeSec
print(f'{velA} km/h')
print(f'{velB}  m/s')
"""

#exer11
"""
print('Escreve ai segundos primo: ')
sec = eval(input('segundos = '))

1 hora tem 3600 segundos
1 dia tem 24 horas

secInDays = (sec / 3600 ) / 24

print(secInDays)
"""

#exer12
"""
print('Escreve ai segundos primo: ')
sec = eval(input('segundos = '))
dias = sec // (3600 * 24)

sec = sec - dias * 3600 * 24

horas = sec // 3600
sec = sec - horas * 3600

min = sec // 60
sec = sec - min * 60

print("dias:", dias,  "horas:", horas, "minutos:", min, "segundos:", sec)
"""

#exer13
"""
from math import sqrt
from statistics import mean
sum = 0
for i in range(5):
    num = eval(input("digite um numero:  "))
    sum += num

media = sum / 5
print(media)
"""

"""
print('Escreve ai 5 numeros : ')
a1 = eval(input('a1 = '))
a2 = eval(input('a2 = '))
a3 = eval(input('a3 = '))
a4 = eval(input('a4 = '))
a5 = eval(input('a5 = '))

media = (a1 +a2 +a3 +a4 + a5) / 5
"""

#exer14
"""
numHigher = 0
for i in range(3):
    num = eval(input("Introduza o {0}º número: ".format(i + 1)))
    if num > numHigher:
        numHigher = num
print(num)        
"""


#exer 15
"""
hours = eval(input("Quantas horas trabalhou na semana?: "))
salary = eval(input("Quanto recebe em € por semana?(à hora): "))

if hours<= 40:
    salaryPerWeek = salary * hours
    print("O salario por hora é ", salaryPerWeek)
else:
    salaryPerWeekOver40 = 40 * salary + (hours - 40) * (salary * 2)
    print("O salario por hora é ", salaryPerWeekOver40)
"""
#exer16

"""
while True:
    print('Escreva um numero de segundos \n(um numero negativo para terminar)')
    seconds = eval(input(''))
    if seconds < 0:
        break
    
    days = seconds / (3600 * 24)
    print('O numero de dias são: ', days)

"""

#exer17
### O -1 tem que ser '-1' por que é uma string
"""
num = ''

while True:
   print('Escreva um numero \n(-1 para terminar)')
   x = input("? ")
   if x == '-1':
     print("O numero é: ", num)
     break
   num += x
"""   

#exer18
"""

print('Escreva um inteiro')
number = eval(input("? "))

result = 0
i = 0
while number != 0:
    digit = number % 10
    number //= 10
    if digit % 2 == 1:
        result += digit * (10 ** i)
        i += 1

print('Resultado:', result)

"""

#exec19
"""
print('Escreva um inteiro positivo')
number = input("? ")

result = ''

#range(início, fim, passo) / for(int i; i <= number.length() ; i-- )
for i in range(len(number), 0, -1):
    result += number[i - 1]

print('Result: ', result)
"""
#exec20
"""
print('Qual o valor de x')
x = eval(input("? "))

print('Qual o valor de n')
n = eval(input("? "))

result = 1
last_item = 1

for i in range(1, n + 1):
    item = last_item * (x / i)
    last_item = item
    result += item

print('O valor da soma é', result)

"""

#exec21
"""
print("Escreva um numero para eu escrever a tabuada da multiplicação")
num = eval(input("Num -> "))

result = 0
for i in range(1, 11, +1 ):
   result = num * i 
   print(num,  " x ", i, " = " , result)

"""

#exec22

"""
print("Introduza um número")
num = int(input("? "))

sum = 0
for i in str(num):
    sum += int(i)

print(sum)

"""

#exec23
"""
result = 0

while True:
    print("Introduza um dígito")
    num = eval(input("? "))
    if num == -1:
        break
        #o 10 faz com que ele ande uma casa
    result = result * 10 + num

print("O numero é:", result)    

"""

#exer24

"""
print('Escreva um inteiro positivo')
number = input("? ")

result2 = ''
#range(início, fim, passo)
for i in range(len(number), 0, -1):
    result2 += number[i - 1]
result = str(number) + str(result2)

print(result)
"""

#exer25
"""
print("Introduza uma lista de notas, separada por vírgulas (,)")
notas = eval(input("? "))

countPositive = 0
countTotal = 0

for nota in notas:
    countTotal += 1
    if nota >= 10:
        countPositive += 1

print("Notas positivas:", countPositive)
print((countPositive / countTotal) * 100 ,"% de notas positivas" )

"""

#exer26
"""
print("Escreva um inteiro?")
num = input("? ")

count = 0
for i in range(len(num) -1):
    if num[i] == '0' and num[i + 1] == '0':
        count += 1

print ("O numero de 0's seguidos é:", count)

"""

#exer27
"""
print("Introduza uma quantia em euros")
num = eval(input("? ")) * 100 // 1 # passar a inteiro

for amount in [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]:

    print("Há", num // amount, "nota(s) de ", amount / 100, "€")
    num %= amount
"""

#exer28
"""
print("Padrão matematico todo XPTO\n")

num = ""

for i in range(1, 10):
    num += str(i)
    result = int(num) * 8 + i

    print(num, "x 8 +" ,i ,"=" ,result)
"""



#func how to do it
"""
def test():
    a = 2
    return a 

print(test())
"""