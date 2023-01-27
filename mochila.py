PESO = 1
VALOR = 0


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
