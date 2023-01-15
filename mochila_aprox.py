import numpy as np

PESO = 1
VALOR = 0


def main():
    lista_coisas = [(10, 5), (40, 4), (30, 6), (50, 3)]
    mochila = MochilaA()

    mochila.resolve(10, lista_coisas)
    print(f'Resposta mochila_aproximada: {mochila.resposta}')


class MochilaA:
    def __init__(self):
        self.matriz = [[]]
        self.resposta = -1

    def resolve(self, k, coisas):
        self.pre_processamento_IK(k, coisas)

        self.matriz = np.zeros((len(coisas), k+1))

        for i in range(len(coisas)):
            for c in range(0, k+1):
                if coisas[i - 1][PESO] > c:
                    self.matriz[i][c] = self.matriz[i - 1][c]
                else:
                    menorSem = self.matriz[i - 1][c]
                    menorCom = self.matriz[i - 1][c - coisas[i - 1][PESO]] + coisas[i - 1][VALOR]
                    self.matriz[i][c] = max(menorSem, menorCom)

        self.acha_maior()

    def acha_maior(self):
        for linha in self.matriz:
            for elem in linha:
                if elem > self.resposta:
                    self.resposta = elem

    def pre_processamento_IK(self, k, coisas):
        # Remove elementos com peso maior que a capacidade
        coisas[:] = [x for x in coisas if x[PESO] < k]

        # IBARRA-KIM
        sigma   = max(coisas, key=lambda x: x[VALOR])[VALOR]
        epsilon = np.random.ranf()
        print(f"\u03B5 = {epsilon}")
        # Lambda é DIVIDIDO pelo subconjunto n ?????
        # pelo tamanho de n?
        # ENTÃO ISSO TEM QUE SER FEITO A CADA ITERAÇÃO ?????
        lmbd = (epsilon * sigma) / len(coisas)

        u = []
        for valor, _ in coisas:
            u.append(valor/lmbd)




if __name__ == "__main__":
    main()