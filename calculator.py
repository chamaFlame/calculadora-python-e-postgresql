import re
class CalculatorClass:
    numbersArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operatorsArray = ["+", "-", "*", "/", "%", "^"]
    calcString = None
    #initialize calcString variable
    def __init__(self):
        self.calcString="0"
    #add new character to calc
    def addCharacter(self, newCharacter):
        if(newCharacter in self.numbersArray):
            if(self.calcString == "0"):
                self.calcString = newCharacter
            else:
                self.calcString = self.calcString + newCharacter
        elif((newCharacter in self.operatorsArray) or newCharacter == "."):
            if(self.calcString[-1] in self.numbersArray):
                self.calcString = self.calcString + newCharacter
            elif(self.calcString[-1] in self.operatorsArray or self.calcString[-1] == "."):
                self.calcString = self.calcString[:-1] + newCharacter
    #erase last character from string
    def eraseCharacter(self):
        self.calcString = self.calcString[:-1]
        if self.calcString == "":
            self.calcString ="0"
    def eraseAll(self):
        self.calcString = "0"
    #erase dot if string already has a dot before current index
    def checkDoubleDot(self):
        index = 0
        remover = False
        savedStringPartOne = ""
        savedStringPartTwo = ""
        while (index < len(self.calcString)):
            if(remover == False and self.calcString[index] == "."):
                remover = True
            elif(remover == True and self.calcString[index] in self.operatorsArray):
                remover = False
            elif(remover == True and self.calcString[index] == "."):
                savedStringPartOne = self.calcString[:index]
                savedStringPartTwo = self.calcString[index + 1:]
                self.calcString = savedStringPartOne + savedStringPartTwo
            index = index + 1
    #return the calc's result
    def doCalc(self):
        self.checkDoubleDot()
        if(self.calcString[-1] not in self.numbersArray):
            self.calcString = self.calcString[:-1]
        self.calcString = str(eval(self.calcString))
    