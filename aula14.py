# a = 'AAAAA'
# b = 'BBBBBB'
# c = 1.1
# string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# formato = string.format(
#     nome1=a, nome2=b, nome3=c
# )

# print(formato)


nome1 = 'Johny'
nome2 = 'Ramon'

string = 'nome1={w} nome2={k}'

formato1 = string.format(
    w=nome1, k=nome2
)

print(formato1)