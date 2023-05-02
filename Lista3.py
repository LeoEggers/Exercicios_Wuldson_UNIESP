# Lista de exercícios - Estrutura de Decisão:
# 1. Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
# menor que 10. O programa deve escrever a mensagem correspondente (maior ou
# menor) e informar o valor digitado pelo usuário.
def q_1():
    if num := float(input('Digite um valor numérico: ')) > 10:
        print(f'O valor {num} é maior do que 10.')
    else:
        print(f'O valor {num} não é maior do que 10.')


# 2. Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
# negativo (considere o valor zero como positivo).
def q_2():
    if num := float(input('Digite um valor: ')) >= 0:
        print(f'O valor {num} é positivo.')
    else:
        print(f'O valor {num} é negativo.')


# 3. As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
# forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.
def q_3():
    qtde = int(input('Digite quantas maçãs serão compradas: '))
    valor = 1 if qtde >= 12 else 1.3
    print(f'Serão compradas {qtde} maçãs a R${valor} cada.'
          f'\nO valor total da compra é R${valor * qtde}.')


# 4. Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
# nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
def q_4():
    boletim = []
    for c in range(2):
        while True:
            nota = float(input(f'Digite a {c+1}ª nota: '))
            if 0 <= nota <= 10:
                boletim.append(nota)
                break
            else:
                print('Tente novamente.')
    media = sum(boletim) / len(boletim)
    status = 'APROVADO' if media >= 6 else 'REPROVADO'
    print(f'Média: {media} | Situação: {status}')


# 5. Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
# deles.
def q_5():
    print('Por favor digite dois valores inteiros diferentes.')
    valores = []
    for c in range(2):
        num = int(input(f'Digite o {c+1}º valor: '))
        valores.append(num)
    print(f'O maior valor digitado foi {sorted(valores)[-1]}.')


# 6. Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
# ordem crescente.
def q_6():
    print('Por favor digite dois valores inteiros diferentes.')
    valores = []
    for c in range(2):
        num = int(input(f'Digite o {c+1}º valor: '))
        valores.append(num)
    print(f'Aqui estão os valores em ordem crescente: {sorted(valores)}.')


# 7. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
# testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.
def q_7():
    n_conta = input('Digite o número da sua conta: ')
    saldo = float(input('Digite o seu saldo: '))
    debt = float(input('Digite o valor do débito: '))
    credt = float(input('Digite o valor do crédito: '))
    saldo_atual = saldo - debt + credt
    balanco = 'Positivo' if saldo_atual > 0 else 'Negativo'
    print(f'Exibindo informações da conta nº{n_conta}:'
          f'\nSaldo atual: R${saldo_atual:.2f}'
          f'\nSaldo {balanco}.')


# 8. Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
# estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
# quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
# mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
def q_8():
    qtde_atual = int(input('Digite a quantidade atual: '))
    qtde_max = int(input('Digite a quantidade máxima: '))
    qtde_min = int(input('Digite a quantidade mínima: '))
    qtde_media = (qtde_max + qtde_min)/2
    if qtde_atual >= qtde_media:
        print('Não efetuar compra.')
    else:
        print('Efetuar compra.')


# 9. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.
def q_9():
    boletim = []
    for c in range(2):
        while True:
            nota = float(input(f'Digite a {c+1}ª nota: '))
            if 0 <= nota <= 10:
                boletim.append(nota)
                break
            else:
                print('Tente novamente.')
    media = sum(boletim) / len(boletim)

    if media >= 9:
        conceito = 'A'
    elif media >= 7.5:
        conceito = 'B'
    elif media >= 6:
        conceito = 'C'
    elif media >= 4:
        conceito = 'D'
    else:
        conceito = 'E'

    status = 'APROVADO' if conceito in 'ABC' else 'REPROVADO'

    print(f'Média: {media} | Conceito: {conceito} | Status: {status} ')
