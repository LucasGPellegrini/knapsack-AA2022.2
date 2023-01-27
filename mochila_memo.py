PESO = 1
VALOR = 0


class MochilaMemo:
    def __init__(self):
        self.dic = {}

    def resolve(self, k, coisas, n, chave_atual=None):
        if chave_atual is None:
            chave_atual = []

        if n == 0:
            if coisas[n][PESO] <= k:
                if chave_atual != []:
                    if str(chave_atual) not in self.dic:
                        self.dic[str(chave_atual)] = n
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
