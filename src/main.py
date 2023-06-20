import pygame
from config import *
from level import Level
from state import State
from game import Game
from gameover import Gameover
from mainmenu import MainMenu
from controls import Controls
from gamewon import Gamewon

State.current_page = "MAINMENU"
quit = False

while not quit:
    if State.current_page == "MAINMENU":
        MainMenu()

    elif State.current_page == "PLAY":
        Game()

    elif State.current_page == "QUIT":
        quit = True

    elif State.current_page == "GAMEOVER":
        Gameover()

    elif State.current_page == "CONTROLS":
        Controls()

    elif State.current_page == "GAMEWON":
        Gamewon()
