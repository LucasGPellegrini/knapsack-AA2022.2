PESO = 1
VALOR = 0


class MochilaA:
    def __init__(self):
        self.matriz = [[]]
        self.resposta = -1

    def resolve(self, k, coisas, epsilon = 0.2):
        coisas = self.pre_processamento_IK(k, coisas, epsilon)

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

    def pre_processamento_IK(self, k, coisas, epsilon):
        # Remove elementos com peso maior que a capacidade
        coisas[:] = [x for x in coisas if x[PESO] <= k]

        # IBARRA-KIM
        sigma = max(coisas)[VALOR]
        #epsilon = np.random.ranf()
        print(f"\u03B5 = {epsilon}")
        lmbd = (epsilon * sigma) / (len(coisas)-1)

        u = []
        for valor, peso in coisas:
            u.append(tuple((int(math.floor(valor/lmbd)), peso)))
            
        return u
