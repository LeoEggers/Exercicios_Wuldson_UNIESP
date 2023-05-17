# 1. Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu
# primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como
# primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu
# dicionário.
def q_1():
    info = {'Nome': 'Carlos', 'Sobrenome': 'Peixoto', 'Cidade': 'Guarabira', 'Idade': 15}
    for k, v in info.items():
        print(f'{k}: {v}')


# 2. Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
# pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número
# favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.
def q_2():
    nums = {'Colega1': int(input('Número favorito: ')), 'Colega2': int(input('Número favorito: ')),
            'Colega3': int(input('Número favorito: ')), 'Colega4': int(input('Número favorito: ')),
            'Colega5': int(input('Número favorito: '))}
    for k, v in nums.items():
        print(f'{k}: {v}')


# 3. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
def q_3():
    import random
    boletim_turma = {}
    lista_notas = []
    for aluno in range(10):
        for nota in range(4):
            notas = random.random() * 10
            lista_notas.append(notas)
        media = sum(lista_notas) / 4
        lista_notas.clear()
        boletim_turma[f'aluno{aluno + 1}'] = media

    cont = 0
    for k, v in boletim_turma.items():
        if v >= 7:
            cont += 1
            print(f'{k}: {v:.2}')
    print(f'Nº de alunos acima da média: {cont}')


# 4. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.
def q_4():
    import random
    alunos = {}
    for aluno in range(30):
        alt = round(random.random() + 1, 2)
        idd = random.randint(10, 17)
        subchave = {'Altura': alt, 'Idade': idd}
        alunos[f'aluno{aluno + 1}'] = subchave

    alturas = []
    for v in alunos.values():
        alturas.append(v['Altura'])
    media = sum(alturas) / 30
    print(f'Média = {media:.2f}cm')

    cont = 0
    for k, v in alunos.items():
        if v['Idade'] > 13:
            if v['Altura'] < media:
                cont += 1
                print(k, v)
    print(f'Nº de alunos com mais de 13 anos com altura abaixo da média: {cont}')


# 5. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
def q_5():
    lista = [1, 2, 3, 4, 5]
    for i in lista:
        print(i)
