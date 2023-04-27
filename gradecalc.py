import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

#window
window = Tk()
window.title("Swift Grade Calculator")
window.geometry('700x400')

#frames
head = Frame(window, width = 100, height = 100)
head.pack()

buttons = Frame(window, width = 100, height = 100)
buttons.pack(pady = 30)

#list
names = []
gradesNum = []
gradesDen = []
weights = []
categoriesLabel = []

#labels and buttons
title = Label(head, text="Swift Grade Calculator")
title.pack()
info = Label(head, text = "Welcome to Swift Grade Calculator.\nWith this calculator, you will be able to add categories and add assignments in the categories.\nThis will help be able to calculate your grades easier.")
info.pack()
def addCategory():
    #window
    categoryWindow = Toplevel(window)
    categoryWindow.title("Add Category")
    categoryWindow.geometry('800x200')
    #labels, buttons, and entries
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

def addAssignment():
    #window
    assignmentWindow = Toplevel(window)
    assignmentWindow.title("Add Assignment")
    assignmentWindow.geometry('900x200')
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

    def submitAssignment():
        #find the category in names and determine the grade for that category
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
            weight = weights[index]
            gradeNum = assignmentNum + gradeNum
            gradesNum[index] = gradeNum
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



def calculateGrade():
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
        result = Label(head, text = f"Grade: {grade}")
        result.pack()


calculate = Button(buttons, text="Calculate Overall Grade", command = calculateGrade)
calculate.pack(side='left', expand = True)


window.mainloop()
