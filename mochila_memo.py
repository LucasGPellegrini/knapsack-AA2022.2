PESO = 1
VALOR = 0


class MochilaMemo:
    def __init__(self):
        self.dic = {}

    def resolve(self, k, coisas, n):
        if n == 0:
            if coisas[n][PESO] <= k:
                return coisas[n][VALOR]
            return 0

        if (n, k) in self.dic:
            return self.dic[(n, k)]

        # Calcula o possível valor sem o elemento
        valorSem = self.resolve(k, coisas, n - 1)

        # Calcula o possível valor com o elemento
        if k >= coisas[n][PESO]:
            valorCom = self.resolve(k - coisas[n][PESO], coisas, n - 1) + coisas[n][VALOR]
            self.dic[(n, k)] = max(valorCom, valorSem)
        # Se não cabe, é sem mesmo
        else:
            self.dic[(n, k)] = valorSem

        return self.dic[(n, k)]
    
