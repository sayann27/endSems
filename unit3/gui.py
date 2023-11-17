from tkinter import messagebox
from tkinter import *

def summation():
    first = num1_entry.get()
    second = num2_entry.get()
    result = float(first) + float(second)
    msg = Message(root, text=f"The sum is: {str(result)}")
    msg.pack()


root = Tk()
root.title("Practice")
root.geometry("600x600")

num1 = Label(root, text="Enter the first number")
num1_entry = Entry(root)
num1.pack()
num1_entry.pack()

num2 = Label(root, text="Enter the second number")
num2_entry = Entry(root)
num2.pack()
num2_entry.pack()

btn = Button(root, text="Add", command=summation)
btn.pack()


root.mainloop()
