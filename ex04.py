# Autor: Michel 
# Data: 2025-04-15

# 4 – ler uma lista de 5 números e imprimir o menor e maior valor.

lista = [] # cria uma lista vazia 
for i in range(5): # loop para ler 5 números
    num = float(input("Digite um número: ")) # lê um número
    lista.append(num) # adiciona o número à lista
    # lista.append(int(num)) # adiciona o número à lista como inteiro
    
print("Lista: ", lista) # imprime a lista
print("Menor valor: ", min(lista)) # imprime o menor valor da lista
print("Maior valor: ", max(lista)) # imprime o maior valor da lista 