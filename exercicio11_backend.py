"""
Faça um programa que fará a leitura de indeterminados números e esses devem ser armazenados em um vetor.
No final devem ser apresentados a soma, a média e o número de elementos desse vetor.
A condição de saída é o usuário digitando o número 0 (zero).   
"""

numeros = []
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print (f"Soma: {soma}")
print (f"Média: {media}")
print (f"Número de elementos: {len(numeros)}")



# Versão do professor

numeros = []
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

# Processamento
soma = 0
for elemento in numeros:
    soma =  soma + elemento

# Saida
print(f"A soma dos todos os elementos é {soma}")
media = soma / len(numeros)
print(f"A média é {media}")

