#ex 59

"""
def apenas_digitos_impares(n):
    # Caso base: se n for 0, retorna 0 
    if n == 0:
        return 0
    
    # Pega o último dígito do número
    digit = n % 10
    
    #Se o digito for par
    if digit % 2 == 0:
        #retira o digito par e anda para a proxima casa
        return apenas_digitos_impares(n // 10)
    
    #se o digit for impar
    else:
        #da return do numero menos o impar
        return apenas_digitos_impares(n // 10) * 10 + digit

"""

#ex 60
"""
def junta_ordenadas(list1, list2):
    # devolve a segunda lista (não há mais elementos para comparar)
    if not list1:
        return list2
    
    # devolve a primeira lista (não há mais elementos para comparar)
    if not list2:
        return list1

    # compara os primeiros elementos de cada lista
    if list1[0] < list2[0]:
        return [list1[0]] + junta_ordenadas(list1[1:], list2)
   
    else:
        return [list2[0]] + junta_ordenadas(list1, list2[1:])              

    
# EXEMPLO 
# junta_ordenadas([2, 5], [3, 4]) -> [2, 3, 4, 5]
# 
# 1ª chamada: [2] + junta_ordenadas([5], [3,4])
# 2ª chamada: [3] + junta_ordenadas([5], [4])  
# 3ª chamada: [4] + junta_ordenadas([5], [])
# 4ª chamada: caso base -> return [5]
# Resultado: [2, 3, 4, 5]
    
print(junta_ordenadas([2, 5, 9], [3, 5, 6, 12]))
"""

#ex61

def sublistas(list):
    if len(list) == 0:
        return 0
    
    
    return