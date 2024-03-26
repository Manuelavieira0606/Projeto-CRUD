from database import *

def vtMenuT():
    vtMenuTJ = input("\nPressione ENTER para voltar")
    if len(vtMenuTJ) >= 0:
        menuT()

def criarT(idt, nome, cidade, pontos, jgsJogados):
    novoT = {"id": idt, "nome": nome, "cidade": cidade, "pontos": pontos, "jogos_jogados": jgsJogados}
    times.append(novoT)
    print("Time criado!")

def criarJ(idj, nome, idade, posicao, data, idtime):
    novoJ = {"id": idj, "nome": nome, "idade": idade, "posicao": posicao, "data_nascimento": data, "idTime": idtime}
    jogadores.append(novoJ)
    print("Jogador cadastrado!")

def menu():
    indiceMenu = int(input("""
=======================
Sistema gerenciador
1 - Times
2 - Jogadores
3 - Sair    
=======================
"""))
    if indiceMenu == 1:
        menuT()
    elif indiceMenu == 2:
        menuJ()
    elif indiceMenu == 3:
        print("\nDesligando...")
    else:
        print("Valor não reconhecido.")
        menu()


def menuT():
    indiceMenuT = int(input("""
Times
1 - Visualizar
2 - Cadastrar
3 - Atualizar
4 - Voltar
"""))
    if indiceMenuT == 1:
        print("\n")
        for t in times:
            print(f'{t["id"]} {t["nome"]} - {t["pontos"]} pontos - {t["cidade"]}')
        vtMenuT()
    elif indiceMenuT == 2:
        ultId = len(times) + 1
        print("\nCriação de times")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        pontuacao = input("Pontuação: ")
        jogosJogados = input("Jogos jogados: ")
        criarT(ultId, nome, cidade,pontuacao, jogosJogados)
        menuT()
    elif indiceMenuT == 3:
        print("\nAtualização de time")
        idTA = int(input("Id do time: "))
        nomeA = input("Nome: ")
        cidadeA = input("Cidade: ")
        pontosA = input("Pontos: ")
        jogosA = input("Jogos: ")
        for t in times:
            if t["id"] == idTA:
                t["nome"] = nomeA
                t["cidade"] = cidadeA
                t["pontos"] = pontosA
                t["jogos_jogados"] = jogosA
                print("Time atualizado")
                menuT()
        print("Time não encontrado")
        menuT()
    elif indiceMenuT == 4:
        menu()
    else:
        print("Valor inserido inválio.")
        menuT()


def menuJ():
    indiceMenuJ = int(input("""
Jogadores
1 - Visualizar
2 - Cadastrar
3 - Atualização
4 - Remover
5 - Voltar
"""))
    if indiceMenuJ == 1:
        print("\nLista jogadores")
        for j in jogadores:
            print(f'id: {j["id"]} - {j["nome"]} - {j["idade"]} anos - {j["posicao"]}')
        print("")
        menuJ()
    elif indiceMenuJ == 2:
        ultId = len(jogadores) + 1
        print("\nCadastro de jogador")
        nome = input("Nome: ")
        idade = input("Idade: ")
        posicao = input("Posição: ")
        data = input("Data de nascimento: ")
        idTime = input("Id do time: ")
        criarJ(ultId, nome, idade, posicao, data, idTime)
        menuJ()
    elif indiceMenuJ == 3:
        print("\nAtualização de jogador")
        idJA = int(input("Id do jogador: "))
        nomeA = input("Nome: ")
        idadeA = input("Idade: ")
        posicaoA = input("Posição: ")
        dataA = input("Data: ")
        idTimeA = input("Id do time: ")
        for j in jogadores:
            if j["id"] == idJA:
                j["nome"] = nomeA
                j["idade"] = idadeA
                j["posicao"] = posicaoA
                j["data_nascimento"] = dataA
                j["idTime"] = idTimeA
                print("Jogador atualizado")
                menuJ()
        print("Jogador não encontrado")
        menuJ()
    elif indiceMenuJ == 4:
        print("Remover jogador")
        idRem = input("Id do jogador que deseja remover: ")
        for j in jogadores:
            if j["id"] == idRem:
                jogadores.remove(j)
                print("Jogador removido")
                menuJ()
        print("Jogador não encontrado")
        menuJ()
    elif indiceMenuJ == 5:
        menu()
    else:
        print("\nValor inserido inválio.")
        menuJ()