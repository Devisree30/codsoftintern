from tkinter import *

# Function
def press(num):
    entry.insert(END, num)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Window
root = Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# Display
entry = Entry(root, font=("Arial", 20), bd=8, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        Button(root, text=btn, width=8, height=3,
               command=equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=btn, width=8, height=3,
               command=lambda b=btn: press(b)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button
Button(root, text="C", width=35, height=2,
       bg="red", fg="white",
       command=clear).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()