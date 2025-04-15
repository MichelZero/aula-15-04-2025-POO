# Autor: Michel 
# Data: 2025-04-15

# 1 – ler uma lista de 5 número inteiros e imprimir cada número juntamente com a sua posição na lista.

lista = [] # cria uma lista vazia
for i in range(5): # loop para ler 5 números inteiros
    num = int(input("Digite um número inteiro: ")) # lê um número inteiro
    lista.append(num) # adiciona o número à lista
    
for i in range(len(lista)): # loop para imprimir os números e suas posições
    print(f"Posição {i}: {lista[i]}") # imprime a posição e o número correspondente
    
    
