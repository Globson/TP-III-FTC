from Sources.Classes import *

if __name__ == "__main__":
    Nome_Arq = str(input("Entre com o nome do arquivo a ser aberto:"))
    Arq = open("Arq_Entrada/"+Nome_Arq, 'r')
    # Arq=open("Arq_Entrada/Entrada1.txt",'r')
    Aux=0
    print("Menu:")
    print("\t1 - Alfabeto {0, 1}")
    print("\t2 - Alfabeto Arbitrario")
    while(Aux!=1 and Aux!=2):
        Aux=int(input("Entre com uma opcao:"))
        if(Aux != 1 and Aux != 2):
            print("\nERRO!Opcao invalida!\n")
    if(Aux==1):
        Q = Arq.readline()
        I = Arq.readline()
        F = Arq.readline()

        Automato1 = Automato(Q, I, F)  #Instanciando objeto com respectivos estados

        for linha in Arq:
            if(linha=="---\n"):
                break
            Automato1.AdicionaTransicao(linha) #Adicionando transicoes

        for linha in Arq:
            Automato1.AdicionaEntrada(linha) #Adicionando Entradas

        print(Automato1.Estados)  #Prints de debug
        print(Automato1.EstadoI)
        print(Automato1.EstadosF)
        print(Automato1.Origem)
        print(Automato1.Destino)
        print(Automato1.SimbolosEntrada)
        print(Automato1.Entradas)

        Automato1.RealizaComputacao()

    elif(Aux==2):
        Q = Arq.readline()
        S = Arq.readline()
        I = Arq.readline()
        F = Arq.readline()

        # Instanciando objeto com respectivos estados
        Automato1 = Automato(Q, I, F)

        for linha in Arq:
            if(linha == "---\n"):
                break
            Automato1.AdicionaTransicao(linha)  # Adicionando transicoes

        for linha in Arq:
            Automato1.AdicionaEntrada(linha)  # Adicionando Entradas

        print(Automato1.Estados)  # Prints de debug
        print(Automato1.EstadoI)
        print(Automato1.EstadosF)
        print(Automato1.Origem)
        print(Automato1.Destino)
        print(Automato1.SimbolosEntrada)
        print(Automato1.Entradas)

        Automato1.RealizaComputacao()
    Arq.close()
    pass
