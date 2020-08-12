"""
Sujet :

Le code doit respecter les bonnes pratiques
Il doit être commenté et explicite
Il doit être réutilisable
Il doit utiliser les fonctions

1) Créer un fonction permettant d'afficher un rectangle de nxn (3x3) caractères (█) sur l'écran
2) Créer une fonction permettant d'afficher une grille (de 8x8) alternée de rectangles pleins et vides
3) Créer une liste de pièces d'échec (uniquement les initiales)
    Roi = (K)ing, Reine = (Q)ueen, Tour = (R)ook, Cavalier = k(N)ight, Fou = (B)ishop, Pion = (P)awn
4) Améliorer la liste pour créer toutes les pièces d'un joueur
5) Faire en sorte de stocker la position (X,Y) de chaque pièce (toujours une liste ? -> Dictionnaire)
6) Dupliquer les pièces (une série pour le joueur bleu, une série pour le joueur rouge)
7) Afficher les pièces sur le plateau

"""
# coding: utf-8

# imports
import os, sys

# Variables
# Blue = "\033[34m"
# Red = "\033[31m"
Reset = "\033[0m"
Position = "\033[{Line};{Column}H"
PartsList = ["R", "N", "B", "K", "Q", "B", "N", "R", "P", "P", "P", "P", "P", "P", "P", "P" ]
ChessParts = {
    "Blue_Player" : {
        "color" : "\033[34m",
        "Pieces" : {
            "R1" : {
                "name" : "Rook",
                "symbol" : "R",
                "posX" : 1,
                "posY" : 1
            },
            "N1" : {
                "name" : "Knight",
                "symbol" : "N",
                "posX" : 2,
                "posY" : 1
                },
            "B1" : {
                "name" : "Bishop",
                "symbol" : "B",
                "posX" : 3,
                "posY" : 1
                },
            "K" : {
                "name" : "King",
                "symbol" : "K",
                "posX" : 4,
                "posY" : 1
                },
            "Q" : {
                "name" : "Queen",
                "symbol" : "Q",
                "posX" : 5,
                "posY" : 1
                },
            "N2" : {
                "name" : "Knight",
                "symbol" : "N",
                "posX" : 6,
                "posY" : 1
            },
            "B2" : {
                "name" : "Bishop",
                "symbol" : "B",
                "posX" : 7,
                "posY" : 1
                },
            "R2" : {
                "name" : "Rook",
                "symbol" : "R",
                "posX" : 8,
                "posY" : 1
            },
            "P1" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 1,
                "posY" : 2
            },
            "P2" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 2,
                "posY" : 2
            },
            "P3" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 3,
                "posY" : 2
            },
            "P4" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 4,
                "posY" : 2
            },
            "P5" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 5,
                "posY" : 2
            },
            "P6" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 6,
                "posY" : 2
            },
            "P7" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 7,
                "posY" : 2
            },
            "P8" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 8,
                "posY" : 2
            }
        }
    },
    "Red_sparow" : {
        "color" : "\033[31m",
        "Pieces" : {
            "R1" : {
                "name" : "Rook",
                "symbol" : "R",
                "posX" : 1,
                "posY" : 8
            },
            "N1" : {
                "name" : "Knight",
                "symbol" : "N",
                "posX" : 2,
                "posY" : 8
                },
            "B1" : {
                "name" : "Bishop",
                "symbol" : "B",
                "posX" : 3,
                "posY" : 8
                },
            "K" : {
                "name" : "King",
                "symbol" : "K",
                "posX" : 4,
                "posY" : 8
                },
            "Q" : {
                "name" : "Queen",
                "symbol" : "Q",
                "posX" : 5,
                "posY" : 8
                },
            "N2" : {
                "name" : "Knight",
                "symbol" : "N",
                "posX" : 6,
                "posY" : 8
            },
            "B2" : {
                "name" : "Bishop",
                "symbol" : "B",
                "posX" : 7,
                "posY" : 8
                },
            "R2" : {
                "name" : "Rook",
                "symbol" : "R",
                "posX" : 8,
                "posY" : 8
            },
            "P1" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 1,
                "posY" : 7
            },
            "P2" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 2,
                "posY" : 7
            },
            "P3" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 3,
                "posY" : 7
            },
            "P4" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 4,
                "posY" : 7
            },
            "P5" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 5,
                "posY" : 7
            },
            "P6" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 6,
                "posY" : 7
            },
            "P7" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 7,
                "posY" : 7
            },
            "P8" : {
                "name" : "Pawn",
                "symbol" : "P",
                "posX" : 8,
                "posY" : 7
            }
        }
    }   
}


# Functions

def ClearConsole():
    """
        Clear the console depending on OS
    """
    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")

def ColorAndPositionSample():
    """
        Sample color and positioning
    """
    ClearConsole()
    print(f"Affiche {Blue}BLEU{Reset} puis {Red}ROUGE{Reset}.")
    print(f"{Position.replace('{Line}', str(5)).replace('{Column}', str(10))}Ce texte est à la ligne 5, colonne 10.")

def Square(Lines, Columns, Char):
    """
        This function should draw a square Lines x Columns of Char
    """
    for Line in range(Lines):
        for Column in range(Columns):
            print(Char, end = "")
        print()


def board(width, height, char, char_2 = " "):
    """
        Will one day create a board.
    """

    for line in range(round(height / 2)):
        print((char + char_2) * round(width / 2))
        print((char_2 + char) * round(width / 2))


def DrawChess():
    # for player in ChessParts.keys ():
    #     for parts in ChessParts
    for Player, PlayerData in ChessParts.items():
        # on defini la couleur du player
        color = PlayerData["color"]
        for PieceID, PieceData in PlayerData["Pieces"].items():
            StringToPrint = (f"{Position.replace('{Line}', str(PieceData['posY'])).replace('{Column}', str(PieceData['posX']))}{color}{PieceData['symbol']}{Reset}")
            print(StringToPrint, end="")
            #print(PieceData['symbol']["posX"]["posY"], end="")

    print()

# Code
if __name__ == "__main__":
    # ColorAndPositionSample()
    ClearConsole()
    # Square(3, 3, "█")
    board(8, 8, "█")
    DrawChess()
    input()