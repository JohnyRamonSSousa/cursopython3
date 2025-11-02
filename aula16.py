# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')


entrada = input("Deseja entar no sistema?")


if entrada == "sim":
     print("Você entrou no sistem!")
elif entrada == "não":
     print("tente outra vez")
else:
     print("Não sabe o que fazer?")
