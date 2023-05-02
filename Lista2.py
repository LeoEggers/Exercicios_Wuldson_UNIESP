# 1. Faça um programa que converta metros para centímetros.
def m_cm(n):
    return n * 100


# 2. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def a_circ(r):
    from math import pi
    return pi * r ** 2


# 3. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def a_quad_dub(lado):
    a = lado * lado
    print(f'área: L * L = {lado} * {lado} = {a}')
    print(f'Dobro da área: {a} * 2 = {a * 2}')


# 4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def salario_mes(s_hora, h_mes):
    return s_hora * h_mes


# 5. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
# a temperatura em graus Celsius.
# 1. C = 5 * ((F-32) / 9).
def q_5():
    temp_f = float(input('Digite a temperatura em Fahrenheit: '))
    temp_c = 5 * (temp_f - 32)/9
    print(f'A temperatura em Celsius é: {temp_c:.2f}')


# 6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
# graus Fahrenheit.
def q_6():
    temp_c = float(input('Digite a temperatura em Celsius: '))
    temp_f = temp_c * 1.8 + 32
    print(f'A temperatura em Fahrenheit é: {temp_f:.2f}')


# 7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1. o produto do dobro do primeiro com metade do segundo .
# 2. a soma do triplo do primeiro com o terceiro.
# 3. o terceiro elevado ao cubo.
def q_7():
    int1 = int(input('Digite um número inteiro: '))
    int2 = int(input('Digite outro número inteiro: '))
    float1 = float(input('Digite um número real: '))
    q1 = (int1 * 2) * (int2 / 2)
    q2 = (int1 * 3) + float1
    q3 = float1 ** 3
    print(f'1. o produto do dobro do primeiro com metade do segundo: {q1}'
          f'\n2. a soma do triplo do primeiro com o terceiro: {q2}'
          f'\n3. o terceiro elevado ao cubo: {q3}')


# 8. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def q_8(h):
    print(f'Sendo {h} sua altura em metros, seu peso ideal é {(72.7 * h) - 58:.2f}Kg.')


# 9. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# 1. Para homens: (72.7*h) - 58
# 2. Para mulheres: (62.1*h) - 44.7
def q_9(h):
    while True:
        lista_gen = ['M', 'F']
        gen = input('Digite o seu sexo [M/F]: ').strip().upper()[0]
        if gen in lista_gen:
            break
        else:
            print('Tente novamente.')

    peso_ideal = (72.7 * h) - 58 if gen == 'M' else (62.1 * h) - 44.7
    print(f'Sendo {h} sua altura em metros, seu peso ideal é {peso_ideal:.2f}Kg.')
