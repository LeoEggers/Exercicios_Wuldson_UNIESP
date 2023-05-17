# 1. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que
# é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas.
def soma_imposto(taxa_imposto, custo):
    """
    altera o valor de custo para incluir o imposto
    sobre vendas.
    :param taxa_imposto: a quantia de imposto sobre vendas expressa em porcentagem
    :param custo: o custo de um item antes do imposto
    :return: valor float do novo preço do produto
    """
    return (taxa_imposto / 100 * custo) + custo


taxa = 15
valor = 100
novo_custo = soma_imposto(15, 100)
print(f'Novo Custo = R${novo_custo:.2f}')


# 2. Faça uma função que informe a quantidade de dígitos de uma determinada frase informada pelo
# usuário(a).
def quant_dig(msg):
    lista = []
    for i in msg:
        lista.append(i)
    return len(lista)


frase = 'Olá, meu nome é Goku.'
n_dig = quant_dig(frase)
print(f'Nº de dígitos na frase: {n_dig}')


# 3. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por
# exemplo: 127 -> 721.
def reverso(num):
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num


numero = 12345
numero_reverso = reverso(numero)
print(numero_reverso)
