import random
import os

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
    #the puzzle class created can have any number of arguments
        if len(args) == 1:
        #if there is only one argument - if a pre-made puzzle is to be made
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
            #the load puzzle function is used specifically for             