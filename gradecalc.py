import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *
# Create the main window
window = tk.Tk()
window.title("Final Grade Calculator")

#Create a frame
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame(window)
frame5 = Frame(window)
# Create a list to store the grades and weights
grades = []
weights = []

# Create a function to add a new assignment
def add_assignment():
    # Create a new window for the user to input the grade and weight
    new_window = tk.Toplevel(window)
    new_window.title("New Assignment")

    # Create labels and entry boxes for the grade, weight, and name
    grade_label = tk.Label(new_window, text="Grade(%):")
    grade_label.grid(row=0, column=0)
    grade_entry = tk.Entry(new_window)
    grade_entry.grid(row=0, column=1)

    weight_label = tk.Label(new_window, text="Weight(%):")
    weight_label.grid(row=1, column=0)
    weight_entry = tk.Entry(new_window)
    weight_entry.grid(row=1, column=1)

    name_label = tk.Label(new_window, text="Category Name:")
    name_label.grid(row=2, column=0)
    name_entry = tk.Entry(new_window)
    name_entry.grid(row=2, column=1)
    # Create a function to add the grade and weight to the list
    def add_grade():
        try:
            grade = float(grade_entry.get())
            weight = float(weight_entry.get())
        except ValueError:
            mb.showerror("Error!", "Please input a number!")
        grades.append(grade)
        weights.append(weight)
        new_window.destroy()

    # Create a button to add the grade and weight
    add_button = tk.Button(new_window, text="Add", command=add_grade)
    add_button.grid(row=3, column=0, columnspan=2)

# Create a function to calculate the final grade
def calculate_grade():
    # Calculate the total weight
    total_weight = sum(weights)

    # Calculate the weighted average of the grades
    weighted_grades = [grade * weight for grade, weight in zip(grades, weights)]
    total_weighted_grades = sum(weighted_grades)
    final_grade = total_weighted_grades / total_weight

    # Create a label to display the final grade
    result_label = tk.Label(frame5, text=f"Final Grade: {final_grade:.2f}")
    frame5.pack()
    result_label.pack(side=LEFT)

def erase_grade():
    grades.clear()
    weights.clear()
    mb.showinfo("Information", "Your grades have been cleared")
    result_label.destroy()
# Create labels and buttons for adding assignments and calculating the final grade
info_label = tk.Label(frame1, text = "Welcome to Swift Grade Calculator. Please add your categories by clicking on 'add a catageory'.")
frame1.pack()
info_label.pack(side=LEFT)
add_label = tk.Label(frame2, text="Add a category:")
frame2.pack()
add_label.pack(side=LEFT)
add_button = tk.Button(frame2, text="+", command=add_assignment, width = 10, height = 1)
frame2.pack()
add_button.pack(side=LEFT)

calculate_button = tk.Button(frame3, text="Calculate Final Grade", command=calculate_grade, width = 20, height = 1)
frame3.pack()
calculate_button.pack(side=LEFT)
erase_button = tk.Button(frame4, text="Erase grade data", command=erase_grade, width = 20, height =1)
frame4.pack()
erase_button.pack(side=LEFT)
# Start the main event loop
window.mainloop()
