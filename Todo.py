from tkinter import *
from tkinter import messagebox

# Window
root = Tk()
root.title("Simple To-Do List")
root.geometry("400x400")

# Functions
def add():
    if task.get() != "":
        listbox.insert(END, task.get())
        task.set("")
    else:
        messagebox.showwarning("Warning", "Enter a task")

def update():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        listbox.insert(index, task.get())
        task.set("")
    except:
        messagebox.showwarning("Warning", "Select a task")

def delete():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task")

def clear():
    listbox.delete(0, END)

# Variable
task = StringVar()

# Widgets
Label(root, text="TO-DO LIST", font=("Arial", 16, "bold")).pack(pady=10)

Entry(root, textvariable=task, width=30).pack(pady=5)

Frame1 = Frame(root)
Frame1.pack()

Button(Frame1, text="Add", width=10, command=add).grid(row=0, column=0, padx=5)
Button(Frame1, text="Update", width=10, command=update).grid(row=0, column=1, padx=5)
Button(Frame1, text="Delete", width=10, command=delete).grid(row=0, column=2, padx=5)

Button(root, text="Clear All", width=15, command=clear).pack(pady=10)

listbox = Listbox(root, width=40, height=12)
listbox.pack(pady=10)

root.mainloop()