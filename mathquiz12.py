#Maths Quiz
#Idreis Abdo

from tkinter import*
from tkinter.scrolledtext import*
import random
studentList = []

class student: #support class
    def __init__(self, name, age, difficulty, score):
        self.name = name
        self.age = age
        self.difficulty = difficulty
        self.score = score
        studentList.append(self) #this list appends all the values I've added



class mathquiz: 
    def __init__(self, parent): #initilizes the code
        
        self.difficulty = ["Easy", "Medium", "Hard"] #list is so that we can assign the difficulty to a radiobutton
        self.difficulty_var = StringVar()
        self.difficulty_var.set(0) 
        self.counter = 0 #counts the question number
        self.score = 0
        self.challenge = ""
        
        #Creating all my frames for my labels and widgets to go in
        self.frame1 = Frame(parent)
        self.frame2 = Frame(parent)
        self.frame3 = Frame(parent)
        #makes the first frame appear
        self.frame1.grid(row = 0, column = 0)
        self.welcomelabel = Label(self.frame1, text = "Welcome to the worlds greatest math game!", font = ("Melvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.welcomelabel.grid(row = 0, column = 0, columnspan = 4)
        #label allows text of my choice and formatting to appear, in this case the "Please enter your name: ", with white foreground and a font of calibri, size 13 and in italic.
        self.namelabel = Label(self.frame1, text = "Please enter your name: ", fg = "white", font = ("calibri", "13", "italic"), bg = "#5B9BD5", width = 20)
        self.namelabel.grid(row = 1, column = 0, pady = 10)
        self.name_entry = Entry(self.frame1) #adds a textbox field
        self.name_entry.grid(row = 1, column = 1)
        
        self.agelabel = Label(self.frame1, text = "Please enter your age: ", fg = "white", font = ("calibri", "13", "italic"), bg = "#5B9BD5", width = 20)
        self.agelabel.grid(row = 2, column = 0)
        self.age_entry = Entry(self.frame1)
        self.age_entry.grid(row = 2, column = 1)
        
        self.selectdifflabel = Label(self.frame1, text = "Select difficulty", fg = "white", font = ("calibri", "13", "italic"), bg = "darkblue", padx = 20)
        self.selectdifflabel.grid(row = 3, column = 1, pady = 30, sticky = NSEW)

        #forloop to make the buttons appear 
        self.difficulty_buttons = [] 
        for i in range(len(self.difficulty)): #i is +1 to make it add one as the forloop continues
            radiobutton = Radiobutton(self.frame1, variable = self.difficulty_var, bg="white", padx = 20,
                                      value = i, anchor = W, text = self.difficulty[i])
            self.difficulty_buttons.append(radiobutton) #adds it to the radio button list
            radiobutton.grid(row = 4, column = i+0) #grids all the options accordingly, on row 4 and going +1 in the column as each value is added


        #for error message
        self.errorcontrol_label = Label(self.frame1, text = "", font = ("Calibri", "13", "bold"), fg = "blue", justify = "center")

        #goes towards the quit function
        self.exitbutton = Button(self.frame1, text = "Exit", command = self.quit, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#B22222")
        self.exitbutton.grid(row = 6, column = 0, sticky = W)
        #goes towards the namecontrol function
        self.beginbutton = Button(self.frame1, text = "Start", command = self.namecontrol, fg = "white", font = ("Melvetica", "16", "bold"), bg = "#228B22") 
        self.beginbutton.grid(row = 6, column = 3, pady = 30, sticky = E)

    #function makes the next questions appear by making the counter variable go up by one for question count, forgets the last question and moves on
    def Next(self):
        self.counter +=1
        self.instruction.configure(text = "Question:" + str(self.counter))        
        self.feedback.grid_forget()
        self.check_ans.grid(row = 2, column = 3, sticky = E)
        if self.difficulty_var.get() == '0': #if the value is = to 0, which is the value for this makes it choose easy
            self.EasyQuestion()
        elif self.difficulty_var.get() == '1': #same applies to medium or hard
            self.MediumQuestion()
        elif self.difficulty_var.get() == '2':
            self.HardQuestion()
        else:
            pass

    #difficulty functions
    def EasyQuestion(self):
        x = random.randint(1,5) #random number between 1 to 5
        y = random.randint(1,5)
        self.Answer = x+y #the answer is x + y which is the random number generated
        problem = str(x) + " + " + str(y) + " ="
        self.problem_label.configure(text = problem)
        self.answer_entry.delete(0, END)
        self.next_btn.grid_forget()
        self.check_ans.grid(row = 2, column = 3, pady = 5)
        self.answer_entry.focus()
    #this function has a number random from 1-12 for the x value, and the same for the y.
    #then they're to multiply each other, and to be presented by x + y =
    #this will then go into the variable to be stored in answer_entry
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
        #calculations to make the hard equations
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
    #if the answer is right the score will be addded by 1 with a green label appearing as correct
    #if not the score won't be added by 1 and there will be a red label saying wrong
    #when the counter reaches 10, the frame containing the quiz will disappear and take us to the 3rd frame with results
    #if nothing is entered or if a letter is entered, it'll prompt them to enter numbers only
    def Ans_Check(self):
        try:
            ans = int(self.answer_entry.get())

            
              
            if ans == self.Answer:
                self.feedback.grid(row = 3, column = 2, sticky = W)
                self.feedback.configure(text = "Correct", fg = "darkgreen")
                
                self.next_btn.grid(row = 2, column = 3, sticky = E)  
                self.check_ans.grid_forget()
                self.score += 1

            


            else:
                self.feedback.grid(row = 3, column = 2, sticky = W)
                self.feedback.configure(text = "Wrong", fg = "red")
                
                self.next_btn.grid(row = 2, column = 3, sticky = E) 
                self.check_ans.grid_forget()

                
            if self.counter == 10:  #answer
                self.frame2.grid_forget()
                self.results()
            

             
        #Used for error control, makes sure that the values entered are only integers
        except ValueError:
            self.feedback.grid(row = 3, column = 2, sticky = W, pady = 5)
            self.feedback.configure(text = "Numbers only", fg = "red")
            self.answer_entry.delete(0, END)
            self.answer_entry.focus()         

    #Second frame used to make all the questions appear to the user using it.
    def questions(self):
        self.frame1.grid_remove()
        self.frame2.grid(row = 0, column = 0) #the counter underneath this line is used to count how many questions there are
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
        root.destroy() #destroys the program so that it exits appropriately
        
    #function for error control for name, allowing only a valid name to be entered with no numbers or spaces
    def namecontrol(self):
                name_error = str(self.name_entry.get())
                self.errorcontrol_label.grid_remove()

                if name_error.isalpha(): #makes it so only string characters are allowed 
                    self.agecontrol()
                    #if nothing is entered
                elif name_error == "":
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = EW)
                    self.errorcontrol_label.configure(text = "Write a name!")
                    #if string characters were allowed through, means that they've used an integer.
                else:
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = EW)
                    self.errorcontrol_label.configure(text = "Letters only!")
                    
    #function for error control for age
    def agecontrol(self):
        try:
            age_error = int(self.age_entry.get())
            self.errorcontrol_label.grid_remove()
            #if the user entered nothing
            if age_error == "":
                    self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW)
                    self.errorcontrol_label.configure(text = "Enter a Number")
            #If the age entered is below 8 or over 12, tell them that it's for ages 8-12 only
            elif age_error > 12 or age_error < 8:
                self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW)
                self.errorcontrol_label.configure(text = "Ages 8-12 only")
            #continue to the questions function
            else:
                self.questions()
                
        #makes sure that only numbers are allowed
        except ValueError:
            self.errorcontrol_label.grid(row = 5, column = 1, sticky = NSEW )
            self.errorcontrol_label.configure(text = "Invalid Number")
            self.age_entry.delete(0, END) #Clears the answer field

    #frame 3 containing the final results        
    def results(self):
        
        if self.difficulty_var.get() == '0':
            challenge = 'Easy'
        elif self.difficulty_var.get() == '1':
            challenge = 'Medium'
        elif self.difficulty_var.get() == '2':
            challenge = 'Hard'
        stuvar = student(self.name_entry.get(), self.age_entry.get(), str(challenge), str(self.score))
        self.frame3.grid(row = 0, column = 0)
        self.results_title = Label(self.frame3, text = "Results!", font = ("Melvetica", "16", "bold"), fg = "white", bg = "#5B9BD5", padx = 100, pady = 10)
        self.results_title.grid(row = 0, columnspan = 4)
        self.scrolled_display = ScrolledText(self.frame3) #adds a scrolledtext box containing my results
        self.scrolled_display.grid(row = 1, columnspan = 4)
        for i in range(len(studentList)):
            self.scrolled_display.insert(END, "Name: " + studentList[i].name + " Age: " + studentList[i].age + " Difficulty: " + studentList[i].difficulty + " Score: " + studentList[i].score + "\n")

        #try again button that goes to the restart function
        self.retry_btn = Button(self.frame3, text = "Retry", width = 10, command = self.restart, font = ("Melvetica", "12", "bold"))
        self.retry_btn.grid(row = 2, column = 3, sticky = E)

    #makes it so that all my variables go to zero and that the summary frame is removed. By doing this we can now grid frame1 to restart the entire code.
    def restart(self):
        self.frame3.grid_forget()
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.difficulty_var.set(0)
        self.counter = 0
        self.score = 0
        self.feedback.grid_forget()
        self.frame1.grid(row = 0, columnspan = 4)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz 2017")
    randomvariable = mathquiz(root)
    root.mainloop()
        
