n = [2, 1, 3]  # array de entrada


# Função responável por cácular o valor mínimo de um dado array n
def min(n):
    minimum = 223372036854775807  # Maior inteiro possível
    for i in n:
        if minimum > i:
            minimum = i

    return minimum

# Função responsável por calcular a soma dos elementos de um dado array n


def sum(n):
    count = 0
    for i in n:
        count = count + i

    return count


def algorithm(n):
    summation = 0  # Responsável por armazenar o valor do somatório
    auxArr = []  # array auxiliar que será construído com base em n a partir na iteração atual
    for c in range(len(n)):  # [x, n]
        for i in range(c, len(n)):  # [c, x]
            for j in range(c, i+1):  # Gera o array que será trabalhado no min e sum da iteração atual
                auxArr.append(n[j])
            summation += min(auxArr) * sum(auxArr)
            auxArr.clear()  # zera o array auxiliar para a próxima iteração

    print(summation)


algorithm(n)
