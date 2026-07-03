from tkinter import *

root = Tk()
root.title("Contact Book")
root.geometry("500x450")
root.config(bg="#D6EAF8")

contacts = []

# ---------- Functions ----------
def add():
    contacts.append([name.get(), phone.get(), email.get(), address.get()])
    show()

def show():
    listbox.delete(0, END)
    for c in contacts:
        listbox.insert(END, f"{c[0]}   |   {c[1]}")

def search():
    listbox.delete(0, END)
    for c in contacts:
        if name.get().lower() in c[0].lower() or phone.get() in c[1]:
            listbox.insert(END, f"{c[0]}   |   {c[1]}")

def delete():
    if listbox.curselection():
        contacts.pop(listbox.curselection()[0])
        show()

def update():
    if listbox.curselection():
        i = listbox.curselection()[0]
        contacts[i] = [name.get(), phone.get(), email.get(), address.get()]
        show()

# ---------- Variables ----------
name = StringVar()
phone = StringVar()
email = StringVar()
address = StringVar()

# ---------- Title ----------
Label(root,
      text="CONTACT BOOK",
      font=("Arial", 18, "bold"),
      bg="#3498DB",
      fg="white",
      pady=10).pack(fill=X)

# ---------- Input Frame ----------
frame = Frame(root, bg="white", bd=2, relief=RIDGE)
frame.pack(pady=15)

Label(frame, text="Name", bg="white").grid(row=0, column=0, padx=10, pady=5)
Entry(frame, textvariable=name, width=30).grid(row=0, column=1)

Label(frame, text="Phone", bg="white").grid(row=1, column=0)
Entry(frame, textvariable=phone, width=30).grid(row=1, column=1)

Label(frame, text="Email", bg="white").grid(row=2, column=0)
Entry(frame, textvariable=email, width=30).grid(row=2, column=1)

Label(frame, text="Address", bg="white").grid(row=3, column=0)
Entry(frame, textvariable=address, width=30).grid(row=3, column=1)

# ---------- Button Frame ----------
btn = Frame(root, bg="#D6EAF8")
btn.pack()

Button(btn, text="Add", width=10, bg="#2ECC71", fg="white", command=add).grid(row=0, column=0, padx=5)
Button(btn, text="Search", width=10, bg="#3498DB", fg="white", command=search).grid(row=0, column=1, padx=5)
Button(btn, text="Update", width=10, bg="#F39C12", fg="white", command=update).grid(row=0, column=2, padx=5)
Button(btn, text="Delete", width=10, bg="#E74C3C", fg="white", command=delete).grid(row=0, column=3, padx=5)

# ---------- Listbox ----------
listbox = Listbox(root, width=55, height=10, font=("Arial", 10))
listbox.pack(pady=15)

root.mainloop()