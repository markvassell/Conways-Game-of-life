from GameBoard import GameBoard
import tkinter as tk
from ConwayUI import ConwayUI
import time
HEIGHT = 10
WIDTH = 10


if __name__ == '__main__':
    gameboard = GameBoard(HEIGHT, WIDTH)
    root = tk.Tk()
    ui = ConwayUI(HEIGHT, WIDTH, root, gameboard)

    root.mainloop()