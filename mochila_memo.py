import numpy as np

PESO = 1
VALOR = 0


def main():
    lista_coisas = [(10, 5), (40, 4), (30, 6), (50, 3)]
    mochila = MochilaMemo()

    print(f'Resposta mochila_memoizada : {mochila.resolve(10, lista_coisas, len(lista_coisas)-1)}')


class MochilaMemo:
    def __init__(self):
        self.dic = {}

    def resolve(self, k, coisas, n, chave_atual=None):
        if chave_atual is None:
            chave_atual = []

        if n == 0:
            if coisas[n][PESO] <= k:
                if chave_atual == []:
                    valor = 0
                else:
                    if str(chave_atual) in self.dic:
                        valor = self.dic[str(chave_atual)]
                    else:
                        self.dic[str(chave_atual)] = n
                        valor = n
                chave_atual.append(n)
                chave_atual.sort()
                self.dic[str(chave_atual)] = valor + coisas[n][VALOR]
                return coisas[n][VALOR]
            return 0

        valorCom = -1
        # Calcula o possível valor com
        if k >= coisas[n][PESO]:
            chave = chave_atual.copy()
            chave.append(n)
            chave.sort()
            if str(chave) in self.dic:
                valorCom = self.dic[str(chave)]
            else:
                self.dic[str(chave)] = self.resolve(k - coisas[n][PESO], coisas, n - 1, chave) + coisas[n][VALOR]
                valorCom = self.dic[str(chave)]

        # Calcula o valor sem
        if str(chave_atual) in self.dic:
            valorSem = self.dic[str(chave_atual)]
        else:
            self.dic[str(chave_atual)] = self.resolve(k, coisas, n - 1, chave_atual)
            valorSem = self.dic[str(chave_atual)]

        return max(valorCom, valorSem)


if __name__ == "__main__":
    main()