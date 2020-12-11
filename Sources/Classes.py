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
            self.EstadosAtual = self.EstadoI[0]
            Tam=len(i)
            index=0
            for j in range (len(self.Origem)):
                if(self.Origem[j]==self.EstadosAtual):
                    #print("AQUI", i[index])
                    if i[index] in self.SimbolosEntrada[j]: # transiçao reconhecida, ela acontece
                        self.EstadoAtual = self.Destino[j]
                    if(index<(Tam-1)):
                        index += 1;    
            if(self.EstadoAtual in self.EstadosF):
                print("OK")
            else:
                print("X")



    

