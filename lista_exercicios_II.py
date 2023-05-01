
# 1
a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if a > (b+c) or b > (a+c) or c > (b+a):
    print("Não compõem um triângulo válido")
elif a == b == c:
    print("Triangulo Equilátero")
elif a == b or b == c:
    print("Triangulo Isósceles")
else:
    print("Triangulo Escaleno")

# 2
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

# 3
peso = float(input("Peso dos peixes: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso:.2f} \nA multa é de R$ {multa:.2f}")

# 4
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print(f"O maior número é: {n1}")
elif n2 >= n3:
    print(f"O maior número é: {n2}")
else:
    print(f"O maior número é: {n3}")

# 5
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 >= n2 and n1 >= n3 and n3 >= n2:
    print(f"O maior número é: {n1} e o menor número é: {n2}")
elif n2 >= n3 and n1 >= n3:
    print(f"O maior número é: {n2} e o menor número é: {n3}")
else:
    print(f"O maior número é: {n3} e o menor número é {n1}")

# 6
salario_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas no mês: "))

salario_bruto = salario_hora * horas_trabalhadas
print(f"Salário bruto: R${salario_bruto:.2f}")

IR = salario_bruto * 0.11
print(f"IR: R${IR:.2f}")

INSS = salario_bruto * 0.08
print(f"INSS: R${INSS:.2f}")

sindicato = salario_bruto * 0.05
print(f"SINDICATO: R${sindicato:.2f}")

descontos = IR+INSS+sindicato
salario_liquido = salario_bruto - descontos
print(f"Seu salário líquido é R${salario_liquido:.2f}")

# 7
area = float(input("Qual a área em m²? "))

if area % 54 == 0:
    latas = area / 54
else:
    latas = int(area/54) + 1

valor_total = 80 * latas
print(f"Quantidade de latas: {latas}")
print(f"Valor total: R${valor_total:.2f}")

