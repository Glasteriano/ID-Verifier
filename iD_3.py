def somatorio(x):
    soma, multiplicacao = 0, 2
    for numero in x:
        resultado = int(numero) * multiplicacao
        soma += resultado
        multiplicacao += 1
    return soma


while True:
    cpf, cpf_limpo = input('Digite vosso CPF: '), ''

    for add in cpf:  # retira os sinais do CPF caso tenha
        if add.isalpha():
            print('CPF não tem letra!')
            break
        elif not add.isdecimal():
            continue
        else:
            cpf_limpo += add  # adiciona somente os números à uma variável vazia

    if len(cpf_limpo) == 11:
        afericao = 0 if len(str(11 - (somatorio(cpf_limpo[8::-1]) % 11))) > 1\
                   else 11 - (somatorio(cpf_limpo[8::-1]) % 11)

        if afericao == int(cpf_limpo[9]):  # Compara e multiplica os valores
            afericao2 = 0 if len(str(11 - (somatorio(cpf_limpo[9::-1]) % 11))) > 1\
                        else 11 - (somatorio(cpf_limpo[9::-1]) % 11)

            mensagem = 'CPF confirmado\n' if afericao2 == int(cpf_limpo[10]) else 'CPF Inválido\n'

            print(mensagem)
        else:
            print("CPF inválido\n")
            continue
    else:
        print('Tamanho do CPF inválido!\n')
