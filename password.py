from tkinter import *
import random
import string


def generate():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    result.set(password)


root = Tk()
root.title("Password Generator")
root.geometry("400x220")
root.resizable(False, False)

Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Enter Password Length").pack()

length_entry = Entry(root, width=20)
length_entry.pack(pady=5)

Button(root, text="Generate Password", command=generate).pack(pady=10)

result = StringVar()
Entry(root, textvariable=result, width=40, justify="center").pack(pady=5)

root.mainloop()