class AutomatoAFN:
    def __init__(self, Q, I,
                 F):  # Construtor inicialmente seta Estados, Iniciais e Finais, alem de remover letras Q,I e F de vetores
        self.Estados = Q.split()
        del (self.Estados[0])
        self.EstadoI = I.split()
        del (self.EstadoI[0])
        self.EstadosF = F.split()
        del (self.EstadosF[0])
        self.Origem = []
        self.Destino = []
        self.SimbolosEntrada = []
        self.Entradas = []
        self.reconhecido = 0
        self.computacao = 0

    def AdicionaTransicao(self, Linha):
        Linha = Linha.split()  # Posicao 1 e 3 devem ser desconsideradas ( -> e | )
        del (Linha[1])
        del (Linha[2])
        self.Origem.append(Linha[0])  # Pega primeiro termo e depois o remove
        del (Linha[0])
        self.Destino.append(
            Linha[0])  # Com remoção de estado de origem, segundo termo vira primeiro e após pega-lo, o remove tb
        del (Linha[0])
        self.SimbolosEntrada.append(Linha)  # Restante dos termos correspondem a valores aceitos na entrada

    def AdicionaEntrada(self, Entrada):
        self.Entradas.append(Entrada)

    def MultiplaComputacao(self,index,Tam,i,estado):
        self.EstadoAtual = estado
        Posicoes = []
        for j in range(len(self.Origem)):
             if (self.Origem[j] == self.EstadoAtual):
                Posicoes.append(j)  # Posicoes onde EstadoAtual possui transicoes
                # print("Posições do estado: ",self.EstadoAtual," :",Posicoes)
        for k in Posicoes:
            if i[index] in self.SimbolosEntrada[k]:  # Caso o simbolo esteja nos simbolos aceitos pela transicao, ela é realizada
                    # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam
                    # )
                    # print("EstadoDestino= ", self.Destino)
                self.MultiplaComputacao(index+1, Tam, i, self.Destino[k])
        for y in Posicoes:
            if '\\' in self.SimbolosEntrada[y]:
                self.MultiplaComputacao(index, Tam, i, self.Destino[y])
        if index >= Tam-1:
            if self.EstadoAtual in self.EstadosF:
                self.reconhecido = 1
            self.computacao += 1
            return

    def RealizaComputacao(self):
        print(" ")  # quebra de linha
        for i in self.Entradas:  # Cada entrada é iterada
            self.computacao = 1
            self.reconhecido = 0
            self.EstadoAtual = self.EstadoI[0]  # Estado inicial setado como atual
            Tam = len(i)
            index = 0  # index para indexar entrada termo a termo
            self.MultiplaComputacao(index, Tam, i, self.EstadoAtual)
            if self.reconhecido == 1:
                print("OK -> Entrada: ",i)
            else:
                print("X -> Entrada: ",i)
