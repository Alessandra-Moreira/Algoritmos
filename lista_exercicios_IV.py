# 1 Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random

# sorteia uma quantidade de números entre quantos forem definidos
lista = random.sample(range(1, 100), 10)
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

n = random.sample(range(1, 100), 20)
x = 0
par = []
impar = []
while x < 20:
    if n[x] % 2 == 0:
        par.append(n[x])
    if n[x] % 3 == 0:
        impar.append(n[x])
    x += 1

print(f"Lista: {n}")
print(f"Pares: {par}")
print(f"Impares: {impar}")

# 3 Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.

vetor1 = random.sample(range(100), 10)
vetor2 = random.sample(range(100), 10)
vetor3 = []
x = 0
y = 0
while x < 10 and y < 10:
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[y])
    x += 1
    y += 1

print(vetor1)
print(vetor2)
print(vetor3)

# 4 com o texto a seguir,  Gere uma lista de palavras deste texto com
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
# e cuidado com maiúsculas e minúsculas.
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

text = text.replace(":", "").replace(",", "").replace(".", "")
text = text.lower()
new_text = text.split()

lista = []
for p in new_text:
    if p[0] in "python" or p[-1] in "python":
        lista.append(p)

print(lista)

# 5 Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
# minúsculas e de remover antes os caracteres especiais
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

text = text.replace(":", "").replace(",", "").replace(".", "")
text = text.lower()
new_text = text.split()


def search(palavra):
    for letra in palavra:
        if letra in "python":
            return True
    return False


lista = []
for p in new_text:
    if search(p) and len(p) > 4:
        lista.append(p)

print(lista)
print(len(lista))
