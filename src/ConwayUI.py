import tkinter as tk
import time
class ConwayUI(tk.Frame):
    
    def __init__(self, height, width, parent, gameboard):
        self.parent = parent
        self.gameboard = gameboard
        tk.Frame.__init__(self, self.parent)
        self.rows = height
        self.cols = width
        self.margin_x = 20
        self.margin_y = 20
        self.current_row = -1
        self.current_col = -1
        self.current_job = None
        self.__initUI()
        

    def __initUI(self):
        self.parent.title("Conway's Game of Life")
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self,
                             width=500,
                             height=550)

        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        start_btn = tk.Button(self, text="Start Simulation", borderwidth=5, command=self.__startSimulation, bg="green")
        stop_btn = tk.Button(self, text="Stop Simulation", borderwidth=5, command=self.__stopSimulation, bg="red")
        clear_btn = tk.Button(self, text="Clear Board", borderwidth=5, command=self.__clearBoard, bg="grey")
        clear_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)
        stop_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)
        start_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.canvas.bind("<Button-1>", self.__cellClicked)

        self.__drawGrid()

    def __drawGrid(self):
        #self.canvas.create_line(start, 10, start, 480, fill="blue")
        for i in range(11):
            color = "blue"
            self.canvas.create_line(self.margin_x + i * 46, self.margin_y, self.margin_x + i * 46, 500 - self.margin_y, fill=color)
            self.canvas.create_line(self.margin_x, self.margin_y + i * 46, 500 - self.margin_x, self.margin_y + i * 46 , fill=color)

    def __clearBoard(self):
        self.gameboard.resetBoard()
        self.__drawSelectedCells()

    def __startSimulation(self):
        # self.playing = True
        # while self.playing:
        self.gameboard.checkAllNodes()
        self.__drawSelectedCells()
        self.current_job = self.after(1000, self.__startSimulation)
        
    def __stopSimulation(self):
        if self.current_job is not None:
            self.after_cancel(self.current_job)
            self.current_job = None

    def __cellClicked(self, event):
        
        x,y = event.x, event.y

        if ( self.margin_x < x < 500 - self.margin_x and self.margin_y < y < 500 - self.margin_y):
            self.canvas.focus_set()

            row, col = int((y - self.margin_y) / 46), int((x - self.margin_x) / 46)
            self.current_row, self.current_col = row, col
            self.gameboard.board[row][col] = not self.gameboard.board[row][col] 
            self.gameboard.displayBoard()
            print()
            self.__drawSelectedCells()

    def __drawSelectedCells(self):
        ui_cell_name = ""
        for i in range(self.rows):
            for j in range(self.cols):
                ui_cell_name = "cell"+str(i)+str(j)
                self.canvas.delete(ui_cell_name)
                if self.gameboard.board[i][j]:
                    self.canvas.create_rectangle(
                        self.margin_x + j * 46 + 1, 
                        self.margin_y + i * 46 + 1, 
                        self.margin_x + (j +  1) * 46 - 1,
                        self.margin_y + (i + 1) * 46 - 1, 
                        fill="red", 
                        tags=ui_cell_name)
                    

                