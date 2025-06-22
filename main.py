from utils import OnePlayer, TwoPlayer
import os

"""
Entry point da aplicação
"""

def main():
    modo_de_jogo = 0

    while modo_de_jogo not in [1, 2]:
        os.system("cls")
        print("//////////////")
        print("Batalha naval")
        print("//////////////")
        print()
        print("Escolha o modo de jogo:\n1 - Um jogador\n2 - Dois jogadores\nR: ", end="")
        try:
            modo_de_jogo = int(input())
        except ValueError:
            continue
    
    if modo_de_jogo == 1:
        jogo = OnePlayer.OnePlayerGame()
    elif modo_de_jogo == 2:
        jogo = TwoPlayer.TwoPlayerGame()

    resultado = jogo.play()

    if resultado:
        pass
    else:
        pass

if __name__ == "__main__":
    main()