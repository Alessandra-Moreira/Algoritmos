# 1 Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random

lista = random.sample(range(1, 100), 10) # sorteia uma quantidade de números entre quantos forem definidos
maior = menor = lista[0]
x = 1
while x < 10:
    if lista[x] > maior:
        maior = lista[x]
    if lista[x] < menor:
        menor = lista[x] 
    x += 1
print(lista)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. 
# Imprima as três listas.

n = random.sample(range(100),20)
x = 0
par = []
impar = []
while x < 20:
    if n[x] % 2 == 0:
        par.append(n[x])
    if n[x] % 3 == 0:
        impar.append(n[x])
    x += 1

print (f"Lista: {n}")
print(f"Pares: {par}")
print(f"Impares: {impar}")

# 3





