# Autor: Michel 
# Data: 2025-04-15

# 3 – ler uma lista de 4 notas e em seguida mostra as notas e a média. 

lista = [] # cria uma lista vazia
soma = 0 # inicializa a soma das notas  

for i in range(4): # loop para ler 4 notas
    nota = float(input("Digite uma nota: ")) # lê uma nota
    lista.append(nota) # adiciona a nota à lista
    soma += nota # soma as notas      
    
for i in range(len(lista)): # loop para imprimir as notas e suas posições
    print(f"Posição {i}: {lista[i]}") # imprime a posição e a nota correspondente
    
print(f"Média: {soma/len(lista)}") # imprime a média das notas
print(f"Média: {soma/4}") # imprime a média das notas 
print(f"Média: {soma/len(lista)}") # imprime a média das notas