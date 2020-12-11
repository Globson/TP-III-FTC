class Automato:
    def __init__(self,Q,I,F):
        self.Estados=Q.split()
        del(self.Estados[0])
        self.EstadoI=I.split()
        del(self.EstadoI[0])
        self.EstadosF=F.split()
        del(self.EstadosF[0])
        self.Origem=[]
        self.Destino = []
        self.SimbolosEntrada = []
        self.Entradas = []

    def AdicionaTransicao(self,Linha):
        Linha = Linha.split() #Posicao 1 e 3 devem ser desconsideradas
        del(Linha[1])
        del(Linha[2])
        self.Origem.append(Linha[0])
        del(Linha[0])
        self.Destino.append(Linha[0])
        del(Linha[0])
        self.SimbolosEntrada.append(Linha)

    def AdicionaEntrada(self,Entrada):
        self.Entradas.append(Entrada)
    
    def RealizaComputacao(self):
        for i in self.Entradas: 
            print("\t->Entrada:",i)
            self.EstadoAtual = self.EstadoI[0]
            print("EstadoAtual= ", self.EstadoAtual)
            Tam=len(i)
            index=0
            for z in range(len(i)):
                Posicoes=[]
                for j in range(len(self.Origem)):
                    if(self.Origem[j] == self.EstadoAtual):
                        Posicoes.append(j)
                # print("Posições do estado: ",self.EstadoAtual," :",Posicoes)
                for k in Posicoes:
                    if i[index] in self.SimbolosEntrada[k]:
                        # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                        # print("EstadoDestino= ", self.Destino)
                        self.EstadoAtual = self.Destino[k]
                        print("Simbolo Lido->", i[index])
                        print("\nEstadoAtual= ", self.EstadoAtual,"")
                        if(index<Tam-1):
                            index+=1
                        break
                    
            if(self.EstadoAtual in self.EstadosF):
                print("OK")
            else:
                print("X")

