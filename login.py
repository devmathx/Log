global dados

print('Digite 1 para se cadastrar.')
print('Digite 2 para fazer login.')
print('Digite 3 para sair.')

escolha = int(input('O que você deseja fazer? '))

if escolha == 1: # Cadastro
    print('Digite seus dados.')
    nome = input('Nome: ')
    idade = input('Idade: ')
    senha = input('Senha: ')
    with open('log.txt', 'w') as log:
        log.write(str(nome) + '\n')
        log.write(str(idade) + '\n')
        log.write(str(senha) + '\n')
        log.write(str('Conta Ativada'))
    print('\033[32mDados salvos!\033[m')

elif escolha == 2: # Login
    print('Fazer login.')
    login_nome = input('Nome: ')
    login_senha = input('Senha: ')
    with open('log.txt', 'r') as log:
        dados = []
        for valor in log:
            dados.append(valor)
        nome = dados[0].strip()
        senha = dados[2].strip()
    if nome == login_nome and senha == login_senha:
        with open('log.txt', 'r') as log:
            dados = log.read().replace('Offline', 'Ativada')
        with open('log.txt', 'w') as log:
            log.write(dados)
        print('\033[32mLogin comclúido, você está online!\033[m')
    else:
        print('\033[31m[ERRO] Dados incorretos!\033[m')

elif escolha == 3: # Sair
    print('Sair da conta.')
    confirm_senha = input('Digite sua senha para confirmar: ')
    with open('log.txt', 'r') as log:
        dados = []
        for valor in log:
            dados.append(valor)
        senha = dados[2]
    if senha[:len(senha)-1] == confirm_senha:
        with open('log.txt', 'r') as log:
            dados = log.read().replace('Ativada', 'Offline')
        with open('log.txt', 'w') as log:
            log.write(dados)
        print('\033[32mVocê está offline.\033[m')
    else:
        print('\033[31m[ERRO] Senha incorreta!\033[m')
else:
    print('\033[31m[ERRO] Digite um valor valido!\033[m')
