from random import randint

cpf = str(randint(0o00000001, 999999999))
multiplicador = 2
soma = 0

for x in cpf[::-1]:
    soma += int(x) * multiplicador
    multiplicador += 1

n1 = str(11 - (soma % 11))
soma2 = 0

for y in cpf+n1:
    soma2 += int(y) * multiplicador
    multiplicador -= 1

n2 = str(11 - (soma2 % 11))

print(cpf + n1 + n2)
