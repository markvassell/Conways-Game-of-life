class GameBoard(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.board = [[False]*self.width for _ in range(self.height)]
        print(sum(len(row) for row in self.board))

    def getBoard(self):
        return self.board

    def displayBoard(self):
        for row in self.board:
            for col in row:
                print (col, end= " ")
            print('')

    def checkNodeVal(self, x, y):
        if(self.board[x][y]):
            return 1
        return 0

    def checkNode(self, x, y):
        # Ternary operator to make the board contine forever
        left = x - 1 if x != 0  else self.width - 1  
        right = x + 1 if x != self.width - 1 else 0
        up = y - 1 if y != 0 else self.height - 1
        down = y + 1 if y != self.height - 1 else 0
        

        living_neighbors_count = sum([
            self.checkNodeVal(left, y),
            self.checkNodeVal(left, up),
            self.checkNodeVal(left, down),
            self.checkNodeVal(x, up),
            self.checkNodeVal(x, down),
            self.checkNodeVal(right, y),
            self.checkNodeVal(right, up),
            self.checkNodeVal(right, down)
        ])

        if self.board[x][y] and (living_neighbors_count == 2 or living_neighbors_count == 3):
            return True

        if not self.board[x][y] and (living_neighbors_count == 3):
            return True    

        return False 


    def checkAllNodes(self):
        updates = []
        for i in range(self.height):
            for j in range(self.width):
                if (self.board[i][j] != self.checkNode(i,j)):
                    updates.append([i,j])
        self.updateBoard(updates)
           
    def updateBoard(self, updates):
        print(updates)
        for x, y in updates:
            self.board[x][y] = not self.board[x][y]

    def resetBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    self.board[i][j] = False
                




        

