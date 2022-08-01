from tkinter import *
import random

# Minesweeper Retro
# Author: Zheng Lin Lei

# Version 1.0

# Class creaction
class Cell:
    def __init__(self, row, column):
        self.mine = False
        self.position = [row, column]

    def createBtn(self, location, size):
        self.btn = Button(location, font=("Consola", 1), padx=size-1, pady=size-2, cursor="hand2")
        self.btn.bind('<Button-1>', self.leftClickEvent)
        self.btn.bind('<Button-3>', self.rightClickEvent)

    # Actions
    def leftClickEvent(self, event):
        print(self.position)

    def rightClickEvent(self, event):
        print("right")


class Game:
    def __init__(self, row, column, mines):
        self.game = [row, column]
        self.gameSize = (row*column)
        self.mines = mines
        # Mine data
        self.mineArr = []
        self.mineArrPos = []
        # Game data
        self.gameArr = [0] * self.gameSize
        self.btnArr = []

    def addBtn(self, btn):
        self.btnArr.append(btn) # Add the button to the list

    def loadMines(self):
        self.mineArr = random.sample(range(self.gameSize), self.mines)

        # Import data to the game
        for i in self.mineArr:
            self.gameArr[i] = 9 # 9 because in a square of 3x3 the maxim of mines are 9
            self.btnArr[i].mine = True # Activate the mine value

            # Get each mine position in the game arena in (x, y)
            self.mineArrPos.append(self.btnArr[i].position)

            self.btnArr[i].btn.config(bg='red') #! Remove it


        # Prepare the tips numbers
        self.prepareTips()

    # Not accessible 
    def prepareTips(self):
        # Foreach arr position
        for i in self.mineArrPos:
            # Reload
            x = i[0]
            y = i[1]
            # 0 1 2
            # 3   4
            # 5 6 7

            for j in range(8):
                if j == 0:
                    x -= 1
                    y -= 1
                elif j in [1, 2, 6, 7]:
                    y += 1
                elif j == 3 or j == 5:
                    x += 1
                    y -= 2
                elif j == 4:
                    y += 2

                # Checking
                print((x, y), self.posToNum(x, y), len(self.gameArr))
                if x >= 0 and y >= 0 and x <= self.game[0]-1 and y <= self.game[1]-1:
                    if(self.gameArr[self.posToNum(x, y)] < 9):
                        self.gameArr[self.posToNum(x, y)] += 1

        print(self.gameArr)

    def posToNum(self, x, y):
        return (x*self.game[0]) + y # x as row and y as column
            

        


def App(row=15, column=15, mines=10, size=10):

    _W_BANNER = 20
    _W_WIDTH = (size*column)*2
    _W_HEIGHT = (size*row)*2 + _W_BANNER


    root = Tk()

    # Root Configurations
    root.configure(bg="#ffffff")
    root.title('Minesweeper')
    root.geometry(f"{_W_WIDTH}x{_W_HEIGHT}")
    root.resizable(False, False)

    # =================
    # Frames

    # Top frame
    topFrame = Frame(
        root,
        width=_W_WIDTH,
        height=_W_BANNER,
    )
    topFrame.pack(anchor=W)
    # Option
    Button(topFrame, text="New", font=("Consola", 8), borderwidth=0, bg="#ffffff", padx=10, cursor="hand2").grid(row=0, column=0)
    gameBtn = Button(topFrame, text="Config", font=("Consola", 8), borderwidth=0, bg="#ffffff", padx=10, cursor="hand2")
    gameBtn.grid(row=0, column=1)
    Button(topFrame, text="Help", font=("Consola", 8), borderwidth=0, bg="#ffffff", padx=10, cursor="hand2").grid(row=0, column=2)

    # Bottom frame
    bottomFrame = Frame(
        root,
        padx=5,
        pady=5,
        width=_W_WIDTH,
        height=_W_HEIGHT - _W_BANNER,
        bg="#efefef",
    )
    bottomFrame.pack()

    # Game Arena ===================
    GAME = Game(row, column, mines)

    gameArena = Frame(bottomFrame, borderwidth = 3, relief=RAISED, padx=5,pady=5)
    gameArena.place(relx=.5, rely=.5, anchor=CENTER)

    # Create buttons
    for i in range(row):
        for j in range(column):
            c = Cell(i, j)
            GAME.addBtn(c)

            c.createBtn(gameArena, size)
            c.btn.grid(row=i, column=j, sticky="NWSE")

    # Label(gameArena, text="0", font=("Consola", 5)).grid(row=3, column=0, sticky="NWSE") #! Use it later
    
    # Load the mines
    GAME.loadMines()

    for i in range(len(GAME.gameArr)):
        Label(gameArena, text=GAME.gameArr[i], font=("Consola", 5), borderwidth=1, relief=RAISED, bg="red" if GAME.gameArr[i] == 1 else "green" if GAME.gameArr[i] == 9 else "blue" if GAME.gameArr[i] == 2 else "yellow" if GAME.gameArr[i] == 3 else "white").grid(row=GAME.btnArr[i].position[0], column=GAME.btnArr[i].position[1], sticky="NWSE") #! Use it later
    
    # Loop the execution until the user has clicked the close button
    root.mainloop()


#Check if it is the main py
if __name__ == '__main__':

    # Preexecution
    pass

    # Execute the App
    App(
        15, # Num of rows
        15, # Num of columns
        10, # Num of mines
        size=10 # Each button square size
    )