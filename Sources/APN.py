class AutomatoAPN:
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
        self.SimbolosEmpilha = []
        self.SimbolosDesempilha = []
        self.pilha = []

    def AdicionaTransicao(self, Linha):
        Linha = Linha.split()  # Posicao 1 e 3 devem ser desconsideradas ( -> e | )
        del (Linha[1])
        del (Linha[2])
        self.Origem.append(Linha[0])  # Pega primeiro termo e depois o remove
        del (Linha[0])
        self.Destino.append(
            Linha[0])  # Com remoção de estado de origem, segundo termo vira primeiro e após pega-lo, o remove tb
        del (Linha[0])
        temp1 = []
        temp2 = []
        temp3 = []
        for i in range(len(Linha)):
            x = Linha[i][0]
            y = Linha[i][2]
            z = Linha[i][4]
            h = 4
            while h < len(Linha[i])-1:
                temp3.append(Linha[i][h+1])
                h += 1
            temp1.append(x)
            temp2.append(y)
            temp3.append(z)
        self.SimbolosEntrada.append(temp1)
        self.SimbolosDesempilha.append(temp2)
        self.SimbolosEmpilha.append(temp3)


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
            if len(self.pilha) > 0:
                if (i[index] in self.SimbolosEntrada[k]):
                    if (self.pilha[0] == self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index(i[index])] or
                            self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index(i[index])] == '\\'):
                        # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                        # print("EstadoDestino= ", self.Destino)
                        if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index(i[index])] != '\\':
                            self.pilha.pop(0)
                        if self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index(i[index])] != '\\':
                            for h in range(
                                    len(self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index(i[index])])):
                                self.pilha.insert(0,
                                                  self.SimbolosEmpilha[k][
                                                      self.SimbolosEntrada[k].index(i[index])][h])
                        self.EstadoAtual = self.Destino[k]  # Atualizando estado atual
                        self.MultiplaComputacao(index+1, Tam, i, self.Destino[k])
            elif (i[index] in self.SimbolosEntrada[k]):
                if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index(i[index])] == '\\':
                    # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                    # print("EstadoDestino= ",. self.Destino)
                    if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index(i[index])] != '\\':
                        self.pilha.pop(0)
                    if self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index(i[index])] != '\\':
                        for h in range(len(self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index(i[index])])):
                            self.pilha.insert(0,
                                              self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index(i[index])][h])
                    self.EstadoAtual = self.Destino[k]  # Atualizando estado atual
                    self.MultiplaComputacao(index+1, Tam, i, self.Destino[k])
        for k in Posicoes:
            if len(self.pilha) > 0:
                if ('\\' in self.SimbolosEntrada[k]):
                    if (self.pilha[0] == self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index('\\')] or
                            self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index('\\')] == '\\'):
                        # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                        # print("EstadoDestino= ", self.Destino)
                        if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index('\\')] != '\\':
                            self.pilha.pop(0)
                        if self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index('\\')] != '\\':
                            for h in range(
                                    len(self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index('\\')])):
                                self.pilha.insert(0,
                                                  self.SimbolosEmpilha[k][
                                                      self.SimbolosEntrada[k].index('\\')][h])
                        self.EstadoAtual = self.Destino[k]  # Atualizando estado atual
                        self.MultiplaComputacao(index, Tam, i, self.Destino[k])
            elif ('\\' in self.SimbolosEntrada[k]):
                if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index('\\')] == '\\':
                    # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                    # print("EstadoDestino= ",. self.Destino)
                    if self.SimbolosDesempilha[k][self.SimbolosEntrada[k].index('\\')] != '\\':
                        self.pilha.pop(0)
                    if self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index('\\')] != '\\':
                        for h in range(len(self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index('\\')])):
                            self.pilha.insert(0,
                                              self.SimbolosEmpilha[k][self.SimbolosEntrada[k].index('\\')][h])
                    self.EstadoAtual = self.Destino[k]  # Atualizando estado atual
                    self.MultiplaComputacao(index, Tam, i, self.Destino[k])
        if index >= Tam - 1:
            if self.EstadoAtual in self.EstadosF and len(self.pilha) == 0:
                self.reconhecido = 1
            self.computacao += 1
            return


    def RealizaComputacao(self):
        for i in self.Entradas:  # Cada entrada é iterada
            print("\t->Entrada:", i)
            self.computacao = 1
            self.reconhecido = 0
            self.pilha = []
            self.EstadoAtual = self.EstadoI[0]  # Estado inicial setado como atual
            Tam = len(i)
            index = 0  # index para indexar entrada termo a termo
            self.MultiplaComputacao(index, Tam, i, self.EstadoAtual)
            if self.reconhecido == 1:
                print("OK")
            else:
                print("X")
