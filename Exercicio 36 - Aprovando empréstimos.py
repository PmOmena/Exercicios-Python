#36: Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. Pergunte o (valor da casa), (salário) do comprador e em (quantos anos) ele vai pagar
# A prestação mensal, não pode exceder 30% do seu salário ou então o emprestimo será negado. 

valor = float(input('Qual o valor da casa a ser comprada? R$'))
salario = float(input('Qual o salário que o comprador recebe? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}")

## print(f"Comparando tem que pagar {prestacao:.2f} e o minimo é de {minimo:.2f}")

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')