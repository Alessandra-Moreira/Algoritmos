# 1
nota = float(input("Digite uma nota: "))

while nota > 10 or nota < 0:
    print("Valor inválido")
    nota = float(input("Digite uma nota entre zero e dez: "))

# 2
usuario = input("usuário: ")
senha = input("senha: ")

while usuario == senha:
    print("Erro. Usuário e senha não podem ser iguais")
    usuario = input("usuário: ")
    senha = input("senha: ")

# 3

a = 80000
b = 200000
anos = 0

while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print(anos)

# 4
n = int(input('Digite o número: '))

a, b = 1, 1
k = 1

while k <= n-2:
    a, b = b, a + b
    k = k + 1

print(b)

# 5

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print(f"mdc = {n2}")
