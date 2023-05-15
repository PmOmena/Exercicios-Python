import math
num = int(input('Digite um numero inteiro: '))
print('''scolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
   print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}") 

elif opcao == 2:
   print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")

elif opcao == 3:
   print(f"{num} convertido para Hexadecimal é igual a {hex(num)[2:]}")
else: 
   print('Opção inválida, tente novamente')
