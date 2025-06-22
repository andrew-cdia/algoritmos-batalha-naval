import json
import random
import os

class Tabuleiro:
    
    """
    Classe que implementa um objeto tabuleiro e suas operações.
    """

    def __init__(self) -> None:
        with open("config.json", "r") as js:
            config = json.load(js)
        
        self.tamanho = config["Tabuleiro"]
        self.navios = config["Entidades"]
        self.tab_visual = [["~"] * self.tamanho for n in range(self.tamanho)]
        self.posicoes = [["~"] * self.tamanho for n in range(self.tamanho)]
        self.main_sum = 0

    """
    Métodos para imprimir o tabuleiro
    - print_positions() é usado para debug e testes apenas
    """

    def print_board(self) -> None:
        Tabuleiro.print(self.tab_visual)
    
    def print_positions(self) -> None:
        Tabuleiro.print(self.posicoes)

    @staticmethod
    def print(tab) -> None:
        print("   ", end="")
        for n in range(len(tab)):
            print(f"{n + 1} ", end="")
        print()
        for n in range(len(tab)):
            print(f" {chr(n + 65)} ", end="")
            for m in range(len(tab[n])):
                print(f"{tab[n][m]} ", end="")
            print()
    
    """
    Métodos que lidam com a validação de posições e preenchimento automático de tabuleiros
    """

    def generate_places(self) -> list:
        for name, config in self.navios.items():
            counter = 0
            size = config["Tamanho"]
            quantity = config["Quantidade"]

            while counter < quantity:
                row = random.randint(0, self.tamanho - 1)
                col = random.randint(0, self.tamanho - 1)
                view = random.choice(["horizontal", "vertical"])

                if self.can_place(size, row, col, view):
                    self.place(name, size, row, col, view)
                    counter += 1
                    self.main_sum += quantity
                
    def can_place(self, size : int, row : int, col : int, view : str) -> bool:
        if view == "horizontal" and col + size < self.tamanho:
            for n in range(size):
                if self.posicoes[row][col + n] != "~":
                    return False
        elif view == "vertical" and row + size < self.tamanho:
            for n in range(size):
                if self.posicoes[row + n][col] != "~":
                    return False
        else:
            return False
        
        return True
    
    def place(self, name : str, size : int, row : int, col : int, view : str) -> None:
        if view == "horizontal":
            for n in range(size):
                self.posicoes[row][col + n] = name[0]
        elif view == "vertical":
            for n in range(size):
                self.posicoes[row + n][col] = name[0]
    
    """
    Métodos da lógica do jogo
    """

    def guess(self, row : int, col : int):
        pass
    

class BoardException(Exception):
    def __init__(self, message : str) -> None:
        super().__init__(message)