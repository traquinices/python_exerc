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
def bissexto(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print(bissexto(2000))

