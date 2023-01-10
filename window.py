# class for the window
import tkinter
from tokenize import Single
import pygame
from calculator import CalculatorClass
from postgre import postgreClass
import keyboard


class WindowClass:
    calculatorObject = CalculatorClass()
    databaseObject = postgreClass()
    historicValue = 0
    soundsArray = ["button1.mp3", "button2.mp3"]

    def __init__(self):
        self.generateWindow()

    def playSound(self, soundindex):
        pygame.mixer.init()
        if (soundIndex == 0):
            pygame.mixer.music.load(self.soundsArray[0])
        elif (soundIndex == 1):
            pygame.mixer.music.load(self.soundsArray[1])
        pygame.mixer.music.play()
        pygame.QUIT

    def generateWindow(self):
        window = tkinter.Tk()
        window.state('zoomed')
        window.title("Calculator")
        window.iconbitmap("icon.ico")
        window.configure(bg="black")
        # numbers buttons
        zeroButton = tkinter.Button(window, width=3, height=1, text="0", font=("Arial", 20), bg="#666565",
                                    foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("0"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        zeroButton.place(x=490, y=600)
        oneButton = tkinter.Button(window, width=3, height=1, text="1", font=("Arial", 20), bg="#666565",
                                   foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("1"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        oneButton.place(x=490, y=530)
        twoButton = tkinter.Button(window, width=3, height=1, text="2", font=("Arial", 20), bg="#666565",
                                   foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("2"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        twoButton.place(x=560, y=530)
        threeButton = tkinter.Button(window, width=3, height=1, text="3", font=("Arial", 20), bg="#666565",
                                     foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("3"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        threeButton.place(x=630, y=530)
        fourButton = tkinter.Button(window, width=3, height=1, text="4", font=("Arial", 20), bg="#666565",
                                    foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("4"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        fourButton.place(x=490, y=460)
        fiveButton = tkinter.Button(window, width=3, height=1, text="5", font=("Arial", 20), bg="#666565",
                                    foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("5"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        fiveButton.place(x=560, y=460)
        sixButton = tkinter.Button(window, width=3, height=1, text="6", font=("Arial", 20), bg="#666565",
                                   foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("6"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        sixButton.place(x=630, y=460)
        sevenButton = tkinter.Button(window, width=3, height=1, text="7", font=("Arial", 20), bg="#666565",
                                     foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("7"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        sevenButton.place(x=490, y=390)
        eightButton = tkinter.Button(window, width=3, height=1, text="8", font=("Arial", 20), bg="#666565",
                                     foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("8"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        eightButton.place(x=560, y=390)
        nineButton = tkinter.Button(window, width=3, height=1, text="9", font=("Arial", 20), bg="#666565",
                                    foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("9"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        nineButton.place(x=630, y=390)
        # other symbols
        dotButton = tkinter.Button(window, width=3, height=1, text=".", font=("Arial", 20), bg="yellow",
                                   foreground="black", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("."),
            calcLabel.config(text=self.calculatorObject.calcString)))
        dotButton.place(x=560, y=600)
        equalButton = tkinter.Button(window, width=3, height=1, text="=", font=("Arial", 20), bg="blue",
                                     foreground="white", command=lambda: (
            self.playSound(1), self.calculatorObject.doCalc(), calcLabel.config(text=self.calculatorObject.calcString)))
        equalButton.place(x=630, y=600)
        restartButton = tkinter.Button(window, width=3, height=1, text="<-", font=("Georgia", 20), bg="orange",
                                       foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.eraseCharacter(),
            calcLabel.config(text=self.calculatorObject.calcString)))
        restartButton.place(x=770, y=320)
        restartAllButton = tkinter.Button(window, width=3, height=1, text="<<--", font=("Georgia", 20), bg="orange",
                                          foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.eraseAll(),
            calcLabel.config(text=self.calculatorObject.calcString)))
        restartAllButton.place(x=700, y=320)
        # operators
        plusButton = tkinter.Button(window, width=3, height=1, text="+", font=("Arial", 20), bg="red",
                                    foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("+"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        plusButton.place(x=700, y=600)
        minusButton = tkinter.Button(window, width=3, height=1, text="-", font=("Arial", 20), bg="red",
                                     foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("-"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        minusButton.place(x=700, y=530)
        divisionButton = tkinter.Button(window, width=3, height=1, text="/", font=("Arial", 20), bg="red",
                                        foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("/"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        divisionButton.place(x=700, y=460)
        multiplicationButton = tkinter.Button(window, width=3, height=1, text="X", font=("Arial", 20), bg="red",
                                              foreground="white", command=lambda: (
            self.playSound(0), self.calculatorObject.addCharacter("*"),
            calcLabel.config(text=self.calculatorObject.calcString)))
        multiplicationButton.place(x=700, y=390)
        # postgreSQL buttons
        saveButton = tkinter.Button(window, width=14, height=1, text="Save current calc", font=("Georgia", 20),
                                    bg="green", foreground="white", command=lambda: (
            self.playSound(1), self.databaseObject.insertNewValue(self.calculatorObject.calcString),
            showAndHideLabel()))
        saveButton.place(x=770, y=390)
        loadButton = tkinter.Button(window, width=11, height=1, text="Load all saves", font=("Georgia", 20), bg="green",
                                    foreground="white",
                                    command=lambda: (self.playSound(1), removeHistoric(), newHistoricValue()))
        loadButton.place(x=770, y=460)
        deleteOldestButton = tkinter.Button(window, width=14, height=1, text="Delete oldest save", font=("Georgia", 20),
                                            bg="green", foreground="white",
                                            command=lambda: (self.playSound(1), deleteOldestSave()))
        deleteOldestButton.place(x=770, y=530)
        deleteAllButton = tkinter.Button(window, width=12, height=1, text="Delete all saves", font=("Georgia", 20),
                                         bg="green", foreground="white", command=lambda: (
            self.playSound(1), self.databaseObject.deleteAllSaves(), removeHistoric()))
        deleteAllButton.place(x=770, y=600)
        calcLabel = tkinter.Label(window, height=1, font=("Arial", 40), text="0")
        calcLabel.place(x=430, y=230)
        savedLabel = tkinter.Label(window, font=("Arial", 40), text="calc saved!", bg="black", foreground="blue")

        def showAndHideLabel():
            savedLabel.place(x=480, y=120)
            window.after(1500, savedLabel.destroy)

        # historic list and scroll bar
        historicList = tkinter.Listbox(window, width=30, height=20, selectmode=Single)
        historicList.place(x=0, y=0)
        historicScrollBar = tkinter.Scrollbar(historicList)
        historicScrollBar.place(relx=1, rely=0, relheight=1, anchor="ne")
        historicList.configure(yscrollcommand=historicScrollBar.set)
        historicScrollBar.configure(command=historicList.yview)

        def newHistoricValue():
            loadedValues = self.databaseObject.loadSaves()
            for x in loadedValues:
                historicList.insert(self.historicValue, x)
                self.historicValue = self.historicValue + 1

        def removeHistoric():
            while self.historicValue > 0:
                historicList.delete(self.historicValue - 1)
                self.historicValue = self.historicValue - 1

        def deleteOldestSave():
            self.databaseObject.deleteFirstRow()
            historicList.delete(0)
            self.historicValue = self.historicValue - 1

        def selectFromHistoric(event):
            calcLabel.config(text=(event.widget.get(event.widget.curselection())))

        historicList.bind('<<ListboxSelect>>', selectFromHistoric)
        # keyboard actions
        keyboard.on_press_key("0", lambda _: (
        self.calculatorObject.addCharacter('0'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("1", lambda _: (
        self.calculatorObject.addCharacter('1'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("2", lambda _: (
        self.calculatorObject.addCharacter('2'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("3", lambda _: (
        self.calculatorObject.addCharacter('3'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("4", lambda _: (
        self.calculatorObject.addCharacter('4'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("5", lambda _: (
        self.calculatorObject.addCharacter('5'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("6", lambda _: (
        self.calculatorObject.addCharacter('6'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("7", lambda _: (
        self.calculatorObject.addCharacter('7'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("8", lambda _: (
        self.calculatorObject.addCharacter('8'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("9", lambda _: (
        self.calculatorObject.addCharacter('9'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key(".", lambda _: (
        self.calculatorObject.addCharacter('.'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("+", lambda _: (
        self.calculatorObject.addCharacter('+'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("-", lambda _: (
        self.calculatorObject.addCharacter('-'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("/", lambda _: (
        self.calculatorObject.addCharacter('/'), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("=", lambda _: (
        self.calculatorObject.doCalc(), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("backspace", lambda _: (
        self.calculatorObject.eraseCharacter(), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.add_hotkey("shift+backspace", lambda: (
        self.calculatorObject.eraseAll(), calcLabel.config(text=self.calculatorObject.calcString)))
        keyboard.on_press_key("l", lambda _: (removeHistoric(), newHistoricValue()))
        window.mainloop()
