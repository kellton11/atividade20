# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
soma = 0

for n in range (1,101):
    if n % 2==0:
        soma += n

print(soma)