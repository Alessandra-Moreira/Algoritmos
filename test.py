import random 
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