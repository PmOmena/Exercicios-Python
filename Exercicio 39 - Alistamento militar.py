import datetime
atual = datetime.date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")

if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(f"Você ainda não tem que se alistar, ainda restam {saldo} anos para seu alistamento.")
    ano = atual + saldo
    print(f"Seu alistamento será realizado no ano de {ano}.")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Você ja deveria ter se alistado há {saldo} anos, caso ja efetuado ignorar esta mensagem.")
    print(f"Seu alistamento deveria ter sido realizado em {ano}.")