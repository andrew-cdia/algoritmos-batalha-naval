import utils.Tabuleiro as tb
import os
import json
import time

class OnePlayerGame:
    
    """
    Classe que lida com a lógica de um jogo de batalha naval com apenas um jogador
    """

    def __init__(self):
        self.board = tb.Tabuleiro()
        self.board.generate_places()
    
    def play(self) -> None:
        max_tries = self.ask_difficulty()
        tries = 0

        while tries < max_tries:
            os.system("cls")
            self.board.print_board()
            print(f"\nTentativas: {tries} / {max_tries}")
            print("\n-> Dê uma posição: (linha, coluna): ", end="")
            posicao = self.get_location(input())

            if not posicao:
                print("Posição inválida")
                time.sleep(1)
                continue

            try:   
                self.board.guess(posicao)
            except tb.BoardException as e:
                print(e.message)
                time.sleep(1)
                continue
            
            tries += 1

    """
    Métodos auxiliares
    """
    def ask_difficulty(self) -> int:
        with open("config.json", "r", encoding="UTF-8") as js:
            dificuldades = json.load(js)["Dificuldades"]

        diff = 0
        while diff < 1 or diff > len(dificuldades):
            os.system("cls")
            print("Qual a dificuldade?")
            index = 1
            for level, tries in dificuldades.items():
                print(f"{index} - {level} - {tries} tentativas")
                index += 1
            print("R: ", end="")
            diff = int(input())

        os.system("cls")
        if diff == 1:
            return 50
        elif diff == 2:
            return 42
        elif diff == 3:
            return 35
    
    @staticmethod
    def get_location(source : str) -> list[int]:
        if len(source) != 2 or not source[0].isalpha() or not source[1].isnumeric():
            return None
        
        return ord(source[0].upper()) - ord("A"), int(source[1]) - 1