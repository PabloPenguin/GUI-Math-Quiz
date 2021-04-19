#Maths Quiz
#Idreis Abdo

from tkinter import*
from tkinter.scrolledtext import*
import random

class mathquiz: 
    def __init__(self, parent):
        
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.difficulty_var = IntVar()
        self.difficulty_var.set(0)
        self.counter = 0 #counts the question number
        self.score = 0
        self.diff = ""
        
        #Creating all my frames
        self.frame1 = Frame(parent)
        self.frame1.grid(row = 0, column = 0)
        self.frame2 = Frame(parent)
        self.frame2.grid(row = 0, column = 0)
        self.frame3 = Frame(parent)
        self.frame3.grid(row = 0, column = 0)
        
        self.welcomelabel = Label(self.frame1, text = "Welcome to the worlds greatest math game!", font = ("Melvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.welcomelabel.grid(row = 0, column = 0, columnspan = 4)
        
        self.namelabel = Label(self.frame1, text = "Please enter your name: ", fg = "white", font = "Calibri 13", bg = "#5B9BD5", width = 20)
        self.namelabel.grid(row = 1, column = 0, pady = 10)
        self.name_entry = Entry(self.frame1)
        self.name_entry.grid(row = 1, column = 1)
        
        self.agelabel = Label(self.frame1, text = "Please enter your age: ", fg = "white", font = "Calibri 13", bg = "#5B9BD5", width = 20)
        self.agelabel.grid(row = 2, column = 0)
        self.age_entry = Entry(self.frame1)
        self.age_entry.grid(row = 2, column = 1)
        
        self.selectdifflabel = Label(self.frame1, text = "Select difficulty", fg = "white", font = "Calibri 13", bg = "darkblue", padx = 20)
        self.selectdifflabel.grid(row = 3, column = 1, pady = 30, sticky = NSEW)


        self.difficulty_buttons = []
        for i in range(len(self.difficulty)):
            radiobutton = Radiobutton(self.frame1, variable = self.difficulty_var, bg="white", padx = 20,
                                      value = i, anchor = W, text = self.difficulty[i])
            self.difficulty_buttons.append(radiobutton)
            radiobutton.grid(row = 4, column = i+0)


        #for error message
        self.errorcontrol_label = Label(self.frame1, text = "", font = ("Calibri", "13", "bold"), fg = "blue", justify = "center")

          
        self.exitbutton = Button(self.frame1, text = "Exit", command = self.quit, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#B22222")
        self.exitbutton.grid(row = 6, column = 0, sticky = W)
        
        self.beginbutton = Button(self.frame1, text = "Start", command = self.namecontrol, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#228B22")
        self.beginbutton.grid(row = 6, column = 3, pady = 30, sticky = E)

    #function to make the next questions
    def MathQuiz(self):
        self.frame1.grid_forget()

        if str(self.difficulty_var.get()) == str(0):
            self.difficulty = "Easy"
            self.EasyQuestion()
        elif str(self.difficulty_var.get()) == str(1):
            self.difficulty = "Medium"
            self.MediumQuestion()
        elif str(self.difficulty_var.get()) == str(2):
            self.difficulty = "Hard"
            self.HardQuestion()
        else:
            pass
        
    def Next(self):
        self.counter +=1
        self.instruction.configure(text = "Question:" + str(self.counter))        
        self.feedback.grid_forget()
        self.check_ans.grid(row = 2, column = 3, sticky = E)
        if str(self.difficulty_var.get()) == str(0):
            self.EasyQuestion()
        elif str(self.difficulty_var.get()) == str(1):
            self.MediumQuestion()
        elif str(self.difficulty_var.get()) == str(2):
            self.HardQuestion()
        else:
            pass

    #difficulty functions
    def EasyQuestion(self):
        x = random.randint(1,25)
        y = random.randint(1,25)
        self.Answer = x+y
        problem = str(x) + " + " + str(y) + " ="
        self.problem_label.configure(text = problem)
        self.answer_entry.delete(0, END)
        self.next_btn.grid_forget()
        self.check_ans.grid(row = 2, column = 3, pady = 5)
        self.answer_entry.focus()

    def MediumQuestion(self):
        x = random.randint(1,12)
        y = random.randint(1,12)
        self.Answer = x*y
        problem = str(x) + " x " + str(y) + " ="
        self.problem_label.configure(text = problem)
        self.answer_entry.delete(0, END)
        self.next_btn.grid_forget()
        self.check_ans.grid(row = 2, column = 3, pady = 5)
        self.answer_entry.focus()
        
    def HardQuestion(self):
        x = random.randint(1,13)
        y = random.randint(1,13)
        z = random.randint(1,10)
        self.Answer = z*x+y
        problem = str(z) + " x " + str(x) + " + " + str(y) + " ="
        self.problem_label.configure(text = problem)
        self.answer_entry.delete(0, END)
        self.next_btn.grid_forget()
        self.check_ans.grid(row = 2, column = 3, pady = 5)
        self.answer_entry.focus()

    #function that checks if the answer is right
    def Ans_Check(self):
        try:
            ans = int(self.answer_entry.get())

            if self.counter == 3:  #change this to 9 for answer
                self.frame2.grid_forget()
                self.results()
              
            if ans == self.Answer:
                self.feedback.grid(row = 3, column = 2, sticky = W)
                self.feedback.configure(text = "Correct", fg = "green")
                
                self.next_btn.grid(row = 2, column = 3, sticky = E)  
                self.check_ans.grid_forget()
                self.score += 1


            else:
                self.feedback.grid(row = 3, column = 2, sticky = W)
                self.feedback.configure(text = "Wrong", fg = "red")
                
                self.next_btn.grid(row = 2, column = 3, sticky = E) 
                self.check_ans.grid_forget()

             
  
        except ValueError:
            self.feedback.grid(row = 3, column = 2, sticky = W, pady = 5)
            self.feedback.configure(text = "Numbers only", fg = "red")
            self.answer_entry.delete(0, END)
            self.answer_entry.focus()         

        #Second frame
    def questions(self):
        self.frame1.grid_remove()

        self.instruction = Label(self.frame2, text = "Question:" + str(self.counter), font = ("Helvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.instruction.grid(row = 0, column = 0, columnspan = 4)
        
        self.problem_label = Label(self.frame2, text = "", height = 3, font = ("Helvetica", "10", "bold"))
        self.problem_label.grid(row = 2, column=1)

        self.answer_entry = Entry(self.frame2, width = 20)
        self.answer_entry.grid(row = 2, column = 2, sticky = W)

        self.check_ans = Button(self.frame2, width = 20, text = "Check", relief = RIDGE, command = self.Ans_Check )
        self.check_ans.grid(row = 2, column = 3, sticky = E)
        
        self.next_btn = Button(self.frame2, text = "Next", width = 20,  relief = RIDGE, command = self.Next)
        self.next_btn.grid(sticky = W)
        
        self.feedback = Label(self.frame2, text = "", height = 3)   
        self.feedback.grid(row = 2, column = 0)
        
        self.Next()
        
    def quit(self):
        root.destroy()
        
    #function for error control for name
    def namecontrol(self):
                name_error = str(self.name_entry.get())
                self.errorcontrol_label.grid_remove()

                if name_error.isalpha(): #makes it so only string characters are allowed 
                    self.agecontrol()
                    
                elif name_error == "":
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = EW)
                    self.errorcontrol_label.configure(text = "Write a name!")

                else:
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = EW)
                    self.errorcontrol_label.configure(text = "Letters only!")
                    
    #function for error control for age
    def agecontrol(self):
        try:
            age_error = int(self.age_entry.get())
            self.errorcontrol_label.grid_remove()

            if age_error == "":
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW)
                    self.errorcontrol_label.configure(text = "Enter a Number")
            
            elif age_error > 12 or age_error < 8:
                self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW)
                self.errorcontrol_label.configure(text = "Ages 8-12 only")

            else:
                self.questions()
                

        except ValueError:
            self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW )
            self.errorcontrol_label.configure(text = "Invalid Number")
            self.age_entry.delete(0, END) #Clears the answer field

    #frame 3        
    def results(self):
        self.results_title = Label(self.frame3, text = "Results!", font = ("Melvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.results_title.grid(row = 0, columnspan = 4)
        self.scrolled_display = ScrolledText(self.frame3)
        self.scrolled_display.grid(row = 1, columnspan = 4)
        self.scrolled_display.insert(END, "Name: " + self.name_entry.get() + " Age: " + self.age_entry.get() + " Difficulty: " + str(self.diff) + " Score: " + str(self.score))

        #try again button
        self.retry_btn = Button(self.frame3, text = "Retry", width = 10, command = self.restart, font = ("Melvetica", "12", "bold"))
        self.retry_btn.grid(row = 2, column = 3, sticky = E)

    #retry module
    def restart(self):
        self.frame3.grid_forget()
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.difficulty_var.set(0)
        self.counter = 1
        self.score = 0
        self.frame1.grid(row = 0, columnspan = 4)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math quiz 2017")
    randomvariable = mathquiz(root)
    root.mainloop()
        
