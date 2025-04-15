# Autor: Michel 
# Data: 2025-04-15

# 2 – ler uma lista de 5 número reais e imprimir a lista na ordem inversa.

lista = [] # cria uma lista vazia

print("Ler uma lista de 5 números reais e imprimir a lista na ordem inversa") # imprime a mensagem
print("Digite 5 números reais") # imprime a mensagem
for i in range(5): # loop para ler 5 números reais
    num = float(input("Digite um número real: ")) # lê um número real
    lista.append(num) # adiciona o número à lista
    
# revisando o uso de range:
# range(valor_inicial, valor_final, passo)
# valor_inicial: valor inicial do range (inclusivo)
# valor_final: valor final do range (exclusivo)
# passo: valor do incremento (padrão é 1)
# range(0, 10, 2) # gera os números: 0, 2, 4, 6, 8
# range(10, 0, -2) # gera os números: 10, 8, 6, 4, 2
# range(0, 10, -2) # gera os números: 0, -2, -4, -6, -8 
# range(10, 0, 2) # gera os números: 10, 12, 14, 16, 18 
# range(0, 10) # gera os números: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(10) # gera os números: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# usando a lista atual
# range(len(lista)-1, -1, -1) # gera os números: 4, 3, 2, 1, 0
# range(len(lista), -1, -1) # gera os números: 5, 4, 3, 2, 1, 0
# loop para imprimir os números na ordem inversa
print("Lista na ordem inversa:") # imprime a mensagem
for i in range(len(lista)-1, -1, -1): # loop para imprimir os números na ordem inversa
    print(f"Posição {i}: {lista[i]}") # imprime a posição e o número correspondente 
    
# ou
L_inversa = list(reversed(lista)) # cria uma lista reversa com os valores de lista
print("Lista reversa: ", L_inversa) # print a lista reversa
