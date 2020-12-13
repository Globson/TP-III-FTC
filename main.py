from Sources.AFN import *
from Sources.Classes import *
from Sources.AP import *
from Sources.APN import *

def main():
    if __name__ == "__main__":
        Nome_Arq = str(input("Entre com o nome do arquivo a ser aberto:"))
        Arq = open("Arq_Entrada/" + Nome_Arq, 'r')
        # Arq=open("Arq_Entrada/Entrada1.txt",'r')
        Aux = 0
        Aux2 = 0
        print("Menu:")
        print("\t1 - Alfabeto {0, 1}")
        print("\t2 - Alfabeto Arbitrario")
        while (Aux != 1 and Aux != 2):
            Aux = int(input("Entre com uma opcao:"))
            if (Aux != 1 and Aux != 2):
                print("\nERRO!Opcao invalida!\n")
        print("\t1 - AFD")
        print("\t2 - AFN")
        print("\t3 - APD")
        print("\t4 - APN")
        while (Aux2 != 1 and Aux2 != 2 and Aux2 != 3 and Aux2 != 4):
            Aux2 = int(input("Entre com uma opcao:"))
            if (Aux2 != 1 and Aux2 != 2 and Aux2 != 3 and Aux2 != 4):
                print("\nERRO!Opcao invalida!\n")
        if (Aux == 1):
            Q = Arq.readline()
            if Aux2 == 3 or Aux2 == 4:
                G = Arq.readline()
            I = Arq.readline()
            F = Arq.readline()
            if Aux2 == 1:
                Automato1 = Automato(Q, I, F)  # Instanciando objeto com respectivos estados
            elif Aux2 == 2:
                Automato1 = AutomatoAFN(Q, I, F)  # Instanciando objeto com respectivos estados
            elif Aux2 == 3:
                Automato1 = AutomatoAPD(Q, I, F)
            elif Aux2 == 4:
                Automato1 = AutomatoAPN(Q, I, F)
            for linha in Arq:
                if (linha == "---\n"):
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

        elif (Aux == 2):
            Q = Arq.readline()
            S = Arq.readline()
            if Aux == 3 or Aux == 4:
                G = Arq.readline()
            I = Arq.readline()
            F = Arq.readline()
            if '\\' in S:
                print('Não pode haver \\ no alfabeto')
                print('Reiniciando o Programa...\n')
                Arq.close()
                main()
                return
            if Aux2 == 1:
                # Instanciando objeto com respectivos estados
                Automato1 = Automato(Q, I, F)
            elif Aux2 == 2:
                # Instanciando objeto com respectivos estados
                Automato1 = AutomatoAFN(Q, I, F)

            for linha in Arq:
                if (linha == "---\n"):
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

main()