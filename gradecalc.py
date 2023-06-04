import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

#Creates the main window
window = Tk()
window.title("Swift Grade Calculator")
window.geometry('700x400')

#Frames to layout the widgets in the window
head = Frame(window, width = 100, height = 100)
head.pack()

buttons = Frame(window, width = 100, height = 100)
buttons.pack(pady = 30)

#Lists to store user-inputted data
names = []
#Num means numerator
gradesNum = []
#Den means denominator
gradesDen = []
weights = []
#ex: with user inputted data weights = [20,80]
categoriesLabel = []

#The widgets in the home screen
title = Label(head, text="Swift Grade Calculator", font = ("Arial", 18, "bold"))
title.pack()
info = Label(head, text = "Welcome to Swift Grade Calculator.\nWith this calculator, you will be able to add categories and add assignments in the categories.\nThis will help be able to calculate your grades easier.", font = ("Arial", 14))
info.pack()
#When the add category button is pressed, the function will be called and it will create a window and prompt users to input their category’s grade numerator and denominator, weights, and category name
def addCategory():
    #Create the category window
    categoryWindow = Toplevel(window)
    categoryWindow.title("Add Category")
    categoryWindow.geometry('800x200')
    #Labels, buttons, and entries in the category window
    title = Label(categoryWindow, text="Swift Grade Calculator\nThe place to swiftly calculate your grades")
    title.grid(column = 2, row = 0)

    gradeNumLabel = Label(categoryWindow, text = "Please input grade total numerator:")
    gradeNumLabel.grid(column = 0, row = 2)

    gradeNumEntry = Entry(categoryWindow, width = 10)
    gradeNumEntry.grid(column = 1, row = 2)

    gradeDenLabel = Label(categoryWindow, text = "Denominator:")
    gradeDenLabel.grid(column = 2, row = 2)

    gradeDenEntry = Entry(categoryWindow, width =10)
    gradeDenEntry.grid(column = 3, row = 2)

    weightLabel = Label(categoryWindow, text = "Please input weight as a percentage:")
    weightLabel.grid(column = 0, row = 3)

    weightEntry = Entry(categoryWindow, width = 10)
    weightEntry.grid(column = 1, row = 3)

    nameLabel = Label(categoryWindow, text = "Please input the category's name:")
    nameLabel.grid(column = 0, row = 4)

    nameEntry = Entry(categoryWindow, width = 10)
    nameEntry.grid(column = 1, row = 4)

# When submit button is pressed, the function is called and the values are stored as variables if the values are in the correct data type. They get added to the appropriate lists and text would be produced that shows the category name, grade, and weight in the main window if they are in the correct data type. An error message will show if they are not in the correct data type. 
    def submitCategory():
        try:
            gradeNum = float(gradeNumEntry.get())
            gradeDen = float(gradeDenEntry.get())
            weight = float(weightEntry.get())
            name = str(nameEntry.get())
        except ValueError:
            mb.showerror("Error!", "Please input the appriorate data type")
        gradesNum.append(gradeNum)
        gradesDen.append(gradeDen)
        weights.append(weight)
        names.append(name)
        categoryWindow.destroy()
        categoryLabel = Label(head, text = f"Category Name: {name}      Grade: {gradeNum}/{gradeDen}      Weight: {weight}")
        categoryLabel.pack()
        categoriesLabel.append(categoryLabel)
    
    submit = Button(categoryWindow, text = "Submit", command = submitCategory)
    submit.grid(column = 2, row = 5)

category = Button(buttons, text = "Add Category", command = addCategory)
category.pack(side='left', expand = True)

# When the add assignment button is pressed, the function is called and the user is prompted to give the assignment grade numerator and denominator and the category to which the assignment will be added
def addAssignment():
    #Creates the assignment window
    assignmentWindow = Toplevel(window)
    assignmentWindow.title("Add Assignment")
    assignmentWindow.geometry('900x200')
    #Labels, buttons, and entries in the assignment window
    title = Label(assignmentWindow, text="Swift Grade Calculator\n(Make sure to type the category correctly as it is case sensitive)")
    title.grid(column = 1, row = 0)

    assignmentNumLabel = Label(assignmentWindow, text = "Please input Assignment Grade numerator:")
    assignmentNumLabel.grid(column = 0, row = 1)

    assignmentNumEntry = Entry(assignmentWindow, width = 10)
    assignmentNumEntry.grid(column = 1, row = 1)

    assignmentDenLabel = Label(assignmentWindow, text = "Denominator:")
    assignmentDenLabel.grid(column = 2, row = 1)

    assignmentDenEntry = Entry(assignmentWindow, width = 10)
    assignmentDenEntry.grid(column = 3, row = 1)

    assignmentCategory = Label(assignmentWindow, text = "What category is this assignment in?")
    assignmentCategory.grid(column = 0, row = 2)

    categoryEntry = Entry(assignmentWindow, width = 10)
    categoryEntry.grid(column = 1, row = 2)

# When the assignment button is pressed, the function is called and the assignment numerator and denominator values are stored in variables if they are floats. If not, an error message will be shown to the user. Then, the inputted category is checked to see if it is in the names list. If the category is in the list then the index will be determined and stored in the variable, index. Using index, the gradesNum, gradesDen, weights, names, and categoryLabels values from that index will be searched and stored into variables. The text from the categoryLabel will then be updated.
    def submitAssignment():
        try:
            assignmentNum = float(assignmentNumEntry.get())
            assignmentDen = float(assignmentDenEntry.get())
        except ValueError:
            mb.showerror("Error!", "Please input the appriorate data type")
        if str(categoryEntry.get()) in names:
            index = names.index(str(categoryEntry.get()))
            gradeNum = gradesNum[index]
            gradeDen = gradesDen[index]
            name = names[index]
#The assignment numerator and grade numerator are added together and the item in the list is changed to the added value
            weight = weights[index]
            gradeNum = assignmentNum + gradeNum
            gradesNum[index] = gradeNum
#The assignment denominator and grade denominator are added together and the item in the list is changed to the added value
            gradeDen = assignmentDen + gradeDen
            gradesDen[index] = gradeDen
            categoryLabel = categoriesLabel[index]
            categoryLabel.config(text= f"Category Name: {name}      Grade: {gradeNum}/{gradeDen}      Weight: {weight}")
        else: 
            mb.showerror("Error!" "This category does not exist")       
        assignmentWindow.destroy()

    assignmentButton = Button(assignmentWindow, text="Submit", command = submitAssignment)
    assignmentButton.grid(column = 1, row = 3)

assignment = Button(buttons, text = "Add Assignment", command = addAssignment)
assignment.pack(side='left', expand = True)


#When the add assignment button is pressed, the function is called and the user is prompted to choose what type of calculation that they would like to do: weighted or unweighted. The user could also close the window instead.
def calculateGrade():
    #Calculation window gets created
    calculationWindow = Toplevel(window)
    #Widgets in the calculation window
    infoLabel = Label(calculationWindow, text = "Select what type of calculation you want to do.")
    infoLabel.grid(column = 0, row = 0)
    #When clicked the type value changed to Weighted
    weighted = Button(calculationWindow, text ="Weighted", command = lambda:calculate("Weighted"))
    weighted.grid(column = 0, row = 1)
    #When clicked the type value changed to Unweighted
    unweighted = Button(calculationWindow, text = "Unweighted", command = lambda:calculate("Unweighted"))
    unweighted.grid(column = 0, row = 2)
    #When clicked the type value changed to Close
    close = Button(calculationWindow, text ="Close", command = lambda:calculate("Close"))
    close.grid(column = 0, row = 3)
    #When either the weighted, unweighted, and close button is pressed, the function with the input variable type is called.
    def calculate(type):
        # If the type value is Weighted then the totalWeight will be added via a for loop. If the Weight does not equal to 100 an error will show. In addition a totalPoint will be added via another for loop. If the totalPoint is negative then an error message will shown. Else, the result given by grade which is totalPoint rounded by 2 decimal points will be written as the grade. The calculation window will be closed.
        if type == "Weighted":
            totalWeight = 0
            totalPoint = 0
            for weight in weights:
                totalWeight += weight
            for gradeNum, gradeDen, weight in zip(gradesNum, gradesDen, weights):
                totalPoint += (gradeNum/gradeDen)*weight 
                grade = round(totalPoint, 2)
            if totalWeight != 100:
                mb.showerror("Error!", f"The sum of the weights does not equal to 100. The total weight is {totalWeight}. ")
            elif totalPoint < 0:
                mb.showerror("Error!", "Grade cannot be negative")
            else:
                result = Label(head, text = f"Weighted Grade: {grade}")
                result.pack()
                calculationWindow.destroy()
        # If the type value is Unweighted then the totalGradeNum will be added via a for loop. The totalGradeDen will also be added via a for loop. If the grade is then calculated by dividing the total numerator by the total denominator and rounding by 2 decimal points. If grade is negative then an error message will be shown. Else a result will be written as the grade. The window is then closed
        elif type == "Unweighted":
            totalGradeNum = 0
            totalGradeDen = 0
            for gradeNum in gradesNum:
                totalGradeNum += gradeNum
            for gradeDen in gradesDen:
                totalGradeDen += gradeDen
            grade = round((totalGradeNum/totalGradeDen)*100, 2) 
            if grade < 0:
                mb.showerror("Error!", "Grade cannot be negative")
            else:
                result = Label(head, text = f"Unweighted Grade: {grade}")
                result.pack()
            calculationWindow.destroy()
        # If the type value is not Unweighted or Weighted the calculation window will be closed
        else:
            calculationWindow.destroy()

calculate = Button(buttons, text="Calculate Overall Grade", command = calculateGrade)
calculate.pack(side='left', expand = True)


window.mainloop()


