PESO = 1
VALOR = 0


def main():
    lista_coisas = [(10, 5), (40, 4), (30, 6), (50, 3)]
    print(f'Resposta mochila_exponencial: {mochila_exponencial(10, lista_coisas, len(lista_coisas)-1)}')


def mochila_exponencial(k, coisas, n):
    if n == 0:
        if coisas[n][PESO] <= k:
            return coisas[n][VALOR]
        return 0

    valorCom = -1
    if k >= coisas[n][PESO]:
        valorCom = mochila_exponencial(k - coisas[n][PESO], coisas, n - 1) + coisas[n][VALOR]

    valorSem = mochila_exponencial(k, coisas, n - 1)

    return max(valorCom, valorSem)


if __name__ == "__main__":
    main()