entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou no sistema')
else:
    print('Você não entrou')
