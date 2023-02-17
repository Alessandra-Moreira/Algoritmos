# 1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = n1 + n2
print(f"O resultado da soma é {resultado}")

# 2
metros = float(input("Informe o valor em metros para conversão: "))
milimetros = (metros*1000)
print(f"O valor convertido é {milimetros} mm")

# 3
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_segundos = float(dias*86400 + horas*3600 + minutos*60 + segundos)

print(f"O total em segundos é: {total_segundos}")

# 4
salario = float(input("Digite seu salario atual: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))
aumento = float(salario*porcentagem/100)
novo_salario = float(salario + aumento)
print(f"O aumento é de: R${aumento:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")

# 5
mercadoria = float(input("Digite o preço da mercadoria: R$ "))
percentual = float(input("Digite o percentual de desconto: "))
desconto = float(mercadoria*percentual/100)
mercadoria_desconto = float(mercadoria - desconto)
print(f"O valor do desconto é R$ {desconto:.2f}")
print(f"O valor da mercadoria com desconto é R$ {mercadoria_desconto:.2f}")

# 6
distancia = float(input("Distância em km: "))
velocidade = float(input("Qual é a velocidade média km/h: "))
tempo = distancia/velocidade
print(f"O tempo estimado é de {tempo:.1f} horas")

# 7
C = float(input("Digite a temperatura em celsius: "))
fahrenheit = 9*C/5+32
print(f"A temperatura é {fahrenheit:.1f}F")

# 8
F = float(input("Digite a temperatura em fahrenheit: "))
celsius = float((F - 32)/1.8)
print(f"A temperatura é {celsius:.1f}C")

# 9
km = float(input("Distância percorrida em km: "))
dias = int(input("Quantidade de dias: "))
preco = dias*60+km*0.15
print(f"O preço total é R$ {preco:.2f}")

# 10
cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite há quantos anos você fuma: "))
total_cigarros = anos*365*cigarros
total_minutos = total_cigarros*10
dias = total_minutos/1440
print(f"Você perdeu {dias:.1f} dias de vida.")

# 11
print(len(str(2**1000000)))
