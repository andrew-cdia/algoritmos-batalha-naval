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

            if self.board.contador == self.board.main_sum:
                return True

            self.board.print_board()
            self.board.print_positions()
            print(f"\nTentativas: {tries} / {max_tries}")
            print("\n-> Dê uma posição: (linha, coluna): ", end="")
            row, col = self.get_location(input())

            if row == None or col == None:
                print(f"\n\033[91mPosição inválida\033[00m")
                time.sleep(1)
                continue

            try:   
                self.board.guess(row, col)
            except tb.BoardException as e:
                print(f"\n\033[91m{e.message}\033[00m")
                time.sleep(1)
                continue
            
            time.sleep(1)
            tries += 1
        
        if self.board.contador == self.board.main_sum:
            return True

        return False

    """
    Métodos auxiliares
    """
    def ask_difficulty(self) -> int:
        with open("config.json", "r", encoding="UTF-8") as js:
            dificuldades = json.load(js)["Dificuldades"]
            quantidades = list(dificuldades.values())

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
            return quantidades[0]
        elif diff == 2:
            return quantidades[1]
        elif diff == 3:
            return quantidades[2]
    
    @staticmethod
    def get_location(source : str) -> list[int]:
        if not len(source) >= 2 or not source[0].isalpha() or not source[1:].isnumeric():
            return None, None
        
        return ord(source[0].upper()) - ord("A"), int(source[1:]) - 1