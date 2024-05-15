import random
import os

'''
Some general comments:
All loops start from 1 and end with + 1, most likely since it was converted from
C to python.
'''

def Main():
    Again = "y"
    Score = 0
    while Again == "y":
        Filename = input("Press Enter to start a standard puzzle or enter name of file to load: ")
        if len(Filename) > 0:
            MyPuzzle = Puzzle(Filename+".txt") 
            #creating a puzzle instance that opens a pre-designed game
        else:
            MyPuzzle = Puzzle(8, int(8*8*0.6))
            #creating a puzzle instance that creates a new general game
        Score = MyPuzzle.AttemptPuzzle() 
        #Since the method AttemptPuzzle() returns the final score of the game,
        #we can set a variable named score to the method AttemptPuzzle()
        print("Puzzle finished. Your score was: " + str(Score))
        #the variable score is an integer, so (even though you don't have to 
        # in python) cast it to an integer and print it
        Again = input("Do another puzzle? ").lower() 
        #validates for capital letter Y rather than y
        
class Puzzle():
    def __init__(self, *args):
    #the puzzle class created can have any number of arguments, but in this
    #code it will only ever have 1 or 2 arguments.
        if len(args) == 1:
        #if there is only one argument - if a pre-made puzzle is to be made
        
        #note that the following variables have all been initialized, but their
        #values are assigned in the __LoadPuzzle method
            self.__Score = 0
            self.__SymbolsLeft = 0
            self.__GridSize = 0
            self.__Grid = []
            #Note how the grid is a one-dimensional list, not two.
            #This later causes issues with validation of whether a symbol is
            #completed or not (see notes for demonstration)
            self.__AllowedPatterns = []
            self.__AllowedSymbols = []
            #The allowed patterns and allowed symbols variables allow the user
            #add different types of symbols to score points. These allowed
            #symbols and patterns are specified in the file
            self.__LoadPuzzle(args[0])
            #the load puzzle function is used specifically for loading pre-made
            #puzzle files, where the argument passed in is the name of the file
            #to be loaded

        else:
        #if there are two arguments - if the standard puzzle is to be made
            self.__Score = 0
            self.__SymbolsLeft = args[0]
            self.__GridSize = args[1]
            #note that this is one side of the grid, not the total grid area.
            self.__Grid = []
            for Count in range(1, self.__GridSize * self.__GridSize + 1):
            #looping through the entire grid (most likely starting at 1 because
            #converted from C)
                if random.randrange(1,101) < 90:
                #remember that the randrange function is inclusive, exclusive
                #for any given cell, there is a 90% change that it is a normal
                #cell, and 10% chance that it is a blocked cell
                    C = Cell()
                else:
                    C = BlockedCell()
                self.__Grid.append(C)
                #After creating a cell, append it to the grid
            self.__AllowedPatterns = []
            self.__AllowedSymbols = []
            #populating the above lists below
            QPattern = Pattern("Q", "QQ**Q**QQ")
            #Creating a new instance of the Pattern class
            self.__AllowedPatterns.append(QPattern)
            #Appending the pattern instance to the allowed patterns class
            self.__AllowedSymbols.append("Q")
            #Appending the symbol as a string to the allowed symbols class
            XPattern = Pattern("X", "X*X*X*X*X")
            self.__AllowedPatterns.append(XPattern)
            self.__AllowedSymbols.append("X")
            TPattern = Pattern("T", "TTT**T**T")
            self.__AllowedPatterns.append(TPattern)
            self.__AllowedSymbols.append("T")
        
    def __LoadPuzzle(self, Filename): 
    #this method is only used when playing a pre-made puzzle
        try:
            with open(Filename) as f:
                NoOfSymbols = int(f.readline().rstrip())
                #the first line contains the number of symbols to be appended 
                #into allowed symbols
                for Count in range(1, NoOfSymbols + 1):
                #looping through each line that has a symbol to be appended
                
                