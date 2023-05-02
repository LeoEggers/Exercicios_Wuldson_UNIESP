# 1. Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
# divididos por 11, produzam o resto igual a 5.
def q_1():
    for c in range(1000, 2001):
        if c % 11 == 5:
            print(c)


# 2. Faça um programa que mostre as tabuadas dos números de 1 a 10.
def q_2():
    for c in range(1, 11):
        for d in range(1, 11):
            print(f'{c} * {d} = {c * d}')
        print('')


# 3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
# pessoa acessando cada elemento da lista um de cada vez.
def q_3():
    from time import sleep
    lista = ['Seya', 'Shiryu', 'Hyoga', 'Shun', 'Ikki']
    for amigo in lista:
        print(amigo)
        sleep(0.5)


# 4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número..
def q_4():
    num = int(input('Digite um número: '))
    print(f'Exibindo a tabuada de {num}:')
    for c in range(11):
        print(f'{num} * {c} = {num * c}')


# 5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
# com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.
def q_5():
    from time import sleep
    lista = ['Seya', 'Shiryu', 'Hyoga', 'Shun', 'Ikki']
    for amigo in lista:
        print(f'Olá! Como vai você, {amigo}?')
        if amigo == 'Shiryu':
            print(f'({amigo}!! Amigo!!)')
        sleep(0.5)


# 6. Seja criativo ao desenvolver este programa.
# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
# c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
# convites. Imprima o nome das pessoas que não poderão comparecer.
# d. Modifique sua lista, substitua os desistentes por novos convidados.
# e. Exiba um novo convite para cada pessoa que continua presente em sua lista.
def q_6():
    from random import choice
    from time import sleep
    # a:
    lista_convidados = ['Van Damme', 'Stallone', 'Schwarzenegger', 'Chuck Norris', 'Bruce Lee']
    # b:
    for convidado in lista_convidados:
        print(f'Olá, {convidado}! Venha para o meu jantar! Desafio você para um duelo! Vai encarar??')
    # c:
    nao_vai = choice(lista_convidados)
    sleep(1)
    print(f'Infelizmente {nao_vai} arregou...')
    # d:
    lista_convidados.remove(nao_vai)
    lista_convidados.append('Terry Crews')
    # e:
    sleep(1)
    for convidado in lista_convidados:
        print(f'Olá, {convidado}. Não desista, se não vai ser pior! Venha para o meu jantar! ')


# 7. Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora
def q_7():
    lista_pessoas = []
    while True:
        pessoa = {'nome': input("Digite o nome: "),
                  'idade': input("Digite a idade: "),
                  'email': input("Digite o email: ")}
        lista_pessoas.append(pessoa)

        continuar = input("Deseja adicionar mais pessoas? (s/n): ").strip().lower()[0]
        if continuar == 'n':
            break

    for p in lista_pessoas:
        for k, v in p.items():
            print(f'{k}: {v}')
        print('')
