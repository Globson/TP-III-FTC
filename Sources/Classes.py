class Automato:
    def __init__(self,Q,I,F):    #Construtor inicialmente seta Estados, Iniciais e Finais, alem de remover letras Q,I e F de vetores
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
        Linha = Linha.split() #Posicao 1 e 3 devem ser desconsideradas ( -> e | )
        del(Linha[1])
        del(Linha[2])
        self.Origem.append(Linha[0])  #Pega primeiro termo e depois o remove
        del(Linha[0])
        self.Destino.append(Linha[0]) #Com remoção de estado de origem, segundo termo vira primeiro e após pega-lo, o remove tb
        del(Linha[0])
        self.SimbolosEntrada.append(Linha) #Restante dos termos correspondem a valores aceitos na entrada

    def AdicionaEntrada(self,Entrada):
        self.Entradas.append(Entrada)
    
    def RealizaComputacao(self): 
        for i in self.Entradas: #Cada entrada é iterada 
            print("\t->Entrada:",i)
            self.EstadoAtual = self.EstadoI[0]  #Estado inicial setado como atual
            print("EstadoAtual= ", self.EstadoAtual)
            Tam=len(i)
            index=0 #index para indexar entrada termo a termo
            for z in range(len(i)-1):  #cada iteracao corresponde a uma tentativa de executar um simbolo da entrada
                verificador=0  #verificador para transicao que leva para estado de erro
                Posicoes=[] 
                for j in range(len(self.Origem)):
                    if(self.Origem[j] == self.EstadoAtual):
                        Posicoes.append(j)     #Posicoes onde EstadoAtual possui transicoes 
                # print("Posições do estado: ",self.EstadoAtual," :",Posicoes)
                for k in Posicoes:
                    if i[index] in self.SimbolosEntrada[k]:   #Caso o simbolo esteja nos simbolos aceitos pela transicao, ela é realizada
                        # print("Simbolo Lido:",i[index], " index: ", index, " tam: ", Tam)
                        # print("EstadoDestino= ", self.Destino)
                        self.EstadoAtual = self.Destino[k]   #Atualizando estado atual
                        print("\nSimbolo Lido->", i[index]) 
                        print("EstadoAtual= ", self.EstadoAtual)
                        verificador = 1
                        if(index<Tam-1):
                            index+=1   #Caso transicao aconteca, o index é incrementado
                        break
                if(verificador==0):  #Caso nenhuma transicao tenha acontecido, simbolo de entrada levou para o estado de erro
                    self.EstadoAtual = "Estado_Erro"
            # print("Estado Atual antes de verificar:",self.EstadoAtual)
            if(self.EstadoAtual in self.EstadosF):  #Caso o estado atual final esteja em um estado final, palavra reconhecida!
                print("OK")
            else:
                print("X")

