# Autor: Michel 
# Data: 2025-04-15
#
#
# Exemplo de lista com sublistas

L = [0, 1, [2, 3, [4, 5]], 6, 7] # valores da lista
#   [0  1  2[0 1  2[0 1]]  3  4] index

print("print o 0") # print o valor 0
print(L[0]) 
print("print o 6") # print o valor 6
print(L[-2])
print("print o 3") # print o valor 3
print(L[2][1])
print("print o 5") # print o valor 5
print(L[2][2][1])

