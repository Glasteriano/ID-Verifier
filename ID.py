while True:
    cpf = input('Digite vosso CPF: ')
    cpf_limpo = ''

    for add in cpf:  # retira os sinais do CPF caso tenha
        if not add.isdecimal():
            continue
        else:
            cpf_limpo += add  # adiciona somente os números à uma variável vazia

    soma = 0
    multiplicacao = 2

    for x in cpf_limpo[8::-1]:  # Acessa a variável criada e multiplica os valores de trás pra frente
        resultado = int(x) * multiplicacao
        soma += resultado
        multiplicacao += 1

    afericao = 0 if len(str(11 - (soma % 11))) > 1 else 11 - (soma % 11)
    soma2 = 0

    if afericao == int(cpf_limpo[9]):  # Compara e multiplica os valores
        for y in cpf_limpo[:10]:  # Limito até o 9º valor par'a conta
            resultado2 = int(y) * multiplicacao
            soma2 += resultado2
            multiplicacao -= 1
    else:
        print("CPF inválido\n")
        continue

    afericao2 = 0 if len(str(11 - (soma2 % 11))) > 1 else 11 - (soma2 % 11)

    mensagem = 'CPF confirmado\n' if afericao2 == int(cpf_limpo[10]) else 'CPF Inválido\n'

    print(mensagem)
