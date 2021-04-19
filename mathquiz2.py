#Maths Quiz
#Idreis Abdo

from tkinter import*
import random

class mathquiz: 
    def __init__(self, parent):
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.difficulty_var = IntVar()
        self.difficulty_var.set(0)
        
        #first frame
        self.frame1 = Frame(parent)
        self.frame1.grid(row = 0, column = 0)
        self.frame2 = Frame(parent)
        self.frame3 = Frame(parent)
        
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
                 
        self.selectdifflabel = Label(self.frame1, text = "Select difficulty", fg = "white", font = "Calibri 13", bg = "darkblue", padx = 20)
        self.selectdifflabel.grid(row = 3, column = 1, pady = 30, sticky = W)


        self.difficulty_buttons = []
        for i in range(len(self.difficulty)):
            radiobutton = Radiobutton(self.frame1, variable = self.difficulty_var, bg="white", padx = 20,
                                      value = i, anchor = W, text = self.difficulty[i])
            self.difficulty_buttons.append(radiobutton)
            radiobutton.grid(row = 4, column = i+0)

  
        self.exitbutton = Button(self.frame1, text = "Exit", command = self.quit, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#B22222")
        self.exitbutton.grid(row = 5, column = 0, sticky = W)
        
        self.beginbutton = Button(self.frame1, text = "Start", command = self.questions, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#228B22")
        self.beginbutton.grid(row = 5, column = 2, pady = 30, sticky = E)



        #second frame
    def questions(self):
        self.frame1.grid_remove()
        self.frame2.grid(row = 0, column = 0)

        
        self.problem_label = Label(self.frame2, text = "", width = 18, height = 3) #empty for now
        self.problem_label.grid(row = 0, column=0, sticky = W)

        self.answer_entry = Entry(self.frame2, width = 7)
        self.answer_entry.grid(row = 0, column = 1, sticky = W)

        self.check_btn = Button(self.frame2, text = "Check Answer", relief = RIDGE)
        self.check_btn.grid(row = 1, column = 0)
        
        self.next_btn = Button(self.frame2, text = "Next", width = 5,  relief = RIDGE)
        self.next_btn.grid(row = 1, column = 1)
        
        self.feedback = Label(self.frame2, text = "", height = 3)   
        self.feedback.grid(row = 2, column = 0)
        
    def quit(self):
        root.destroy()

    def selectdifficulty(self):
        """some random shit here"""
        
    def begingame(self):
        """some more random shit here"""

if __name__ == "__main__":
    root = Tk()
    root.title("Math quiz 2017")
    randomvariable = mathquiz(root)
    root.mainloop()
        
