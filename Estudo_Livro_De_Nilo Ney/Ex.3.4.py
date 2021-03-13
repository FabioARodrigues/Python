# Exercício 3.4 - Calcular se paga imposto ou não, referência R$1200.00

sal = float(input('Informe seu salário'))

imposto = not sal<1200
if imposto == True:
    print('Você irá pagar imposto de renda =/')
if imposto == False:
    print('Você não irá pagar imposto de renda =)')


# Exercício 3.6

m1 = int(input('Informe ume nota até 10: '))
m2= int(input('Informe ume nota até 10: '))
m3 = int(input('Informe ume nota até 10: '))
md = 7

aprovado = m1>=md and m2>=md and m3>=md
if aprovado == True:
    print('APROVADO')
if aprovado == False:
    print('REPROVADO')