from tkinter import*
import random

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class mathquiz: 
    def __init__(self, parent):
        self.difficulty = IntVar()
        self.difficulty.set(0)

        self.frame1 = Frame(parent)
        self.frame1.pack()
        
        self.welcomelabel = Label(self.frame1, text = "Welcome to the worlds greatest math game!", font = ("Melvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.welcomelabel.grid(row = 0, column = 0, columnspan = 4)
        
        self.namelabel = Label(self.frame1, text = "Please enter your name: ", fg = "white", font = "Calibri 13", bg = "#5B9BD5", width = 20)
        self.namelabel.grid(row = 1, column = 0, pady = 10)
        self.nameentry = Entry(self.frame1)
        self.nameentry.grid(row = 1, column = 1)
        
        self.agelabel = Label(self.frame1, text = "Please enter your age: ", fg = "white", font = "Calibri 13", bg = "#5B9BD5", width = 20)
        self.agelabel.grid(row = 2, column = 0)
        self.ageentry = Entry(self.frame1)
        self.ageentry.grid(row = 2, column = 1)
                 
        self.selectdifflabel = Label(self.frame1, text = "Select difficulty", fg = "white", font = "Calibri 13", bg = "blue")
        self.selectdifflabel.grid(row = 3, column = 1, pady = 30, sticky = W)
        
        self.difficulty1 = Radiobutton(self.frame1, text = "1", variable = self.difficulty, value = 1, command = self.difficultychooser, fg = "white", font = "Calibri 13", bg = "blue")
        self.difficulty1.grid(row = 4, column = 0)
        
        self.difficulty2 = Radiobutton(self.frame1, text = "2", variable = self.difficulty, value = 2, command = self.difficultychooser, fg = "white", font = "Calibri 13", bg = "blue")
        self.difficulty2.grid(row = 4, column = 1, padx = 30, sticky = W)
        
        self.difficulty3 = Radiobutton(self.frame1, text = "3", variable = self.difficulty, value = 3, command = self.difficultychooser, fg = "white", font = "Calibri 13", bg = "blue")
        self.difficulty3.grid(row = 4, column = 2, sticky = W, padx = 5)        
        
        self.exitbutton = Button(self.frame1, text = "Exit", command = self.quit, fg = "black", font = ("Melvetica", "16", "bold"), bg = "yellow")
        self.exitbutton.grid(row = 5, column = 0, sticky = W)
        
        self.beginbutton = Button(self.frame1, text = "Begin", command = self.begingame, fg = "black", font = ("Melvetica", "16", "bold"), bg = "green")
        self.beginbutton.grid(row = 5, column = 2, pady = 30, sticky = E)
        
    def quit(self):
        root.destroy()

    def difficultychooser(self):
        "test"
    def begingame(self):
        "test"
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("580x400")
    root.title("Math quiz 2017")
    randomvariable = mathquiz(root)
    root.mainloop()
        
