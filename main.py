from Sources.Classes import *

if __name__ == "__main__":
    Arq=open("Arq_Entrada/Entrada1.txt",'r')
    Q = Arq.readline()
    I = Arq.readline()
    F = Arq.readline()

    Automato1 = Automato(Q, I, F)
    for linha in Arq:
        if(linha=="---\n"):
            break
        Automato1.AdicionaTransicao(linha)

    for linha in Arq:
        Automato1.AdicionaEntrada(linha)

    print(Automato1.Estados)
    print(Automato1.EstadoI)
    print(Automato1.EstadosF)
    print(Automato1.Origem)
    print(Automato1.Destino)
    print(Automato1.SimbolosEntrada)
    print(Automato1.Entradas)
    Automato1.RealizaComputacao()
    Arq.close()
    pass
