# Aluna: Bruna Raynara Maia Batista

jogador1 = ""
jogador2 = ""
letrasPermitidas = "ABC"
numerosPermitidos = "123"

# Validando a entrada

def trataEntrada(entrada):
    entrada = entrada.replace(" ", "").replace(",", ""). \
        replace("\t", "").replace("\n", "").replace("\r", "").upper()
    return entrada

# Validando as possíveis formas de ganhar: fechando uma linha, uma coluna ou uma diagonal

def colunaTodaIgual(jogador, velha):
    return (velha["1"]["A"] == jogador and velha["2"]["A"] == jogador and velha["3"]["A"] == jogador) or \
           (velha["1"]["B"] == jogador and velha["2"]["B"] == jogador and velha["3"]["B"] == jogador) or \
           (velha["1"]["C"] == jogador and velha["2"]["C"] == jogador and velha["3"]["C"] == jogador)


def linhaTodaIgual(jogador, velha):
    return (velha["1"]["A"] == jogador and velha["1"]["B"] == jogador and velha["1"]["C"] == jogador) or \
           (velha["2"]["A"] == jogador and velha["2"]["B"] == jogador and velha["2"]["C"] == jogador) or \
           (velha["3"]["A"] == jogador and velha["3"]["B"] == jogador and velha["3"]["C"] == jogador)


def temDiagonalTodaIgual(jogador, velha):
    return (velha["1"]["A"] == jogador and velha["2"]["B"] == jogador and velha["3"]["C"] == jogador) or \
           (velha["3"]["A"] == jogador and velha["2"]["B"] == jogador and velha["1"]["C"] == jogador)

def estaTudoPreenchido(velha):
    return (velha["1"]["A"] != " " and velha["1"]["B"] != " " and velha["1"]["C"] != " ") and \
           (velha["2"]["A"] != " " and velha["2"]["B"] != " " and velha["2"]["C"] != " ") and \
           (velha["3"]["A"] != " " and velha["3"]["B"] != " " and velha["3"]["C"] != " ")

def estaEmpatado(velha):
    return estaTudoPreenchido(velha) and not jogadorVenceu("X", velha) and not jogadorVenceu("O", velha)

def jogadorVenceu(jogador, velha):
    return colunaTodaIgual(jogador, velha) or linhaTodaIgual(jogador, velha) or temDiagonalTodaIgual(jogador, velha)

# Validando todos sem vírgula

def validaEntrada(entrada):
    entrada = trataEntrada(entrada)

    if (len(entrada) < 2):
        return False

    itens = list(entrada)

    if (len(itens) > 2):
        return False

    if (numerosPermitidos.find(itens[0]) < 0):
        return False

    if (letrasPermitidas.find(itens[1]) < 0):
        return False

    return True

def tabuleiro(velha):
    print("  A   B   C")
    print("1 " + velha["1"]["A"] + " | " + velha["1"]["B"] + " | " + velha["1"]["C"] + " 1")
    print(" ---+---+---")
    print("2 " + velha["2"]["A"] + " | " + velha["2"]["B"] + " | " + velha["2"]["C"] + " 2")
    print(" ---+---+---")
    print("3 " + velha["3"]["A"] + " | " + velha["3"]["B"] + " | " + velha["3"]["C"] + " 3")
    print("  A   B   C")


def verificaJaMarcado(coordenadas, velha):
    if (len(velha[coordenadas[0]][coordenadas[1]].strip()) > 0):
        print("A posição selecionada já foi marcada, selecione outra!")
        return True
    else:
        return False

def iminenciaDeGanhar(jogadorAtual, velha):
    outroJogador = "X"
    qtdVitoriasOutroJogador = 0

    if (jogadorAtual == "X"):
        outroJogador = "O"

    for linha in velha:
        for coluna in velha[linha]:
            if (velha[linha][coluna] == " "):
                velha[linha][coluna] = outroJogador
                
                if (jogadorVenceu(outroJogador, velha)):
                    qtdVitoriasOutroJogador = qtdVitoriasOutroJogador + 1

                velha[linha][coluna] = " "
                    
                if (qtdVitoriasOutroJogador == 2):
                    return True
    
    return False


# Início do código principal
# Início do jogo, jogador escolhe seu símbolo

escolher = input("Escolha X ou O para começar a jogar: ")

if escolher == "X":
    jogador1 = "X"
    jogador2 = "O"
    print("O jogador 1 escolheu o símbolo X. O jogador 2 ficará com o símbolo O.")
elif escolher == "O":
    jogador1 = "O"
    jogador2 = "X"
    print("O jogador 1 escolheu o símbolo O. O jogador 2 ficará com o símbolo X.")

# Variavéis

jogarNovamente = "SIM"
empate = 0
jogador1vitorias = 0
jogador2vitorias = 0
mensagemEntradaInvalida = "Entrada inválida, tente novamente."
mensagemConclusao = ""
jogadorAtual = {
    "simbolo": jogador1,
    "numero": "1"
}

# Jogo
# PS: Assim como na matemática, usei a sequência [linha][coluna], ou seja
# na hora do jogador digitar as coordenadas, ele deve respeitar essa ordem,
# usando por exemplo: 1A

while jogarNovamente.upper() == "SIM":
    mensagemConclusao = ""
    tabuleiroVelha = {
        "1": {"A": " ", "B": " ", "C": " "},
        "2": {"A": " ", "B": " ", "C": " "},
        "3": {"A": " ", "B": " ", "C": " "}
    }

    while (mensagemConclusao == ""):
        tabuleiro(tabuleiroVelha)

        if (iminenciaDeGanhar(jogadorAtual["simbolo"], tabuleiroVelha)):
            print("Jogador " + jogadorAtual["numero"] + ", o outro jogador já está na iminência de ganhar")

        entrada = input("Jogador " + jogadorAtual["numero"] + ", digite a coordenada: ")

        if (not validaEntrada(entrada)):
            print(mensagemEntradaInvalida)
        else:
            coordenadas = trataEntrada(entrada)

            if (not verificaJaMarcado(coordenadas, tabuleiroVelha)):
                tabuleiroVelha[coordenadas[0]][coordenadas[1]] = jogadorAtual["simbolo"]

                if (jogadorVenceu(jogadorAtual["simbolo"], tabuleiroVelha)):
                    tabuleiro(tabuleiroVelha)
                    mensagemConclusao = "O jogador " + jogadorAtual["numero"] + " venceu."

                    if (jogadorAtual["numero"] == "1"):
                        jogador1vitorias = jogador1vitorias + 1
                    else:
                        jogador2vitorias = jogador2vitorias + 1

                elif estaEmpatado(tabuleiroVelha):
                    tabuleiro(tabuleiroVelha)
                    mensagemConclusao = "O jogo empatou."
                    empate = empate + 1

                if (jogadorAtual["numero"] == "1"):
                    jogadorAtual["numero"] = "2"
                else:
                    jogadorAtual["numero"] = "1"

                if (jogadorAtual["simbolo"] == "X"):
                    jogadorAtual["simbolo"] = "O"
                else:
                    jogadorAtual["simbolo"] = "X"

    print(mensagemConclusao)
    jogarNovamente = input("Deseja jogar novamente ? Sim ou Não: ")

print("Placar do jogo: ")
print("- vitórias do jogador 1:", jogador1vitorias)
print("- vitórias do jogador 2:", jogador2vitorias)
print("- empates:", empate)
