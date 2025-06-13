import json
import os
import random

"""
Funções que lidam com o tabuleiro
"""
def tabuleiro() -> list[list]:
    with open("config.json", 'r') as js:
        config = json.load(js)
        tamanho = config["Tabuleiro"]
        return [["~"] * tamanho] * tamanho
    
def imprime_tabuleiro(tab : list[list]) -> None:
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
Funções de configuração:
"""
def configura():
    pass

def game():
    tab = tabuleiro()
    imprime_tabuleiro(tab)

def main():
    game()

if __name__ == "__main__":
    main()