from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

user = StringVar()
computer = StringVar()
result = StringVar()

def play(choice):
    global user_score, computer_score

    comp = random.choice(choices)

    user.set("You : " + choice)
    computer.set("Computer : " + comp)

    if choice == comp:
        result.set("Result : It's a Tie")
    elif (choice == "Rock" and comp == "Scissors") or \
         (choice == "Paper" and comp == "Rock") or \
         (choice == "Scissors" and comp == "Paper"):
        user_score += 1
        result.set("Result : You Win!")
    else:
        computer_score += 1
        result.set("Result : Computer Wins!")

    score.config(text=f"Score  You: {user_score}   Computer: {computer_score}")

Label(root, text="Rock Paper Scissors",
      font=("Arial", 18, "bold")).pack(pady=10)

Button(root, text="Rock", width=12,
       command=lambda: play("Rock")).pack(pady=5)

Button(root, text="Paper", width=12,
       command=lambda: play("Paper")).pack(pady=5)

Button(root, text="Scissors", width=12,
       command=lambda: play("Scissors")).pack(pady=5)

Label(root, textvariable=user, font=("Arial", 11)).pack()
Label(root, textvariable=computer, font=("Arial", 11)).pack()
Label(root, textvariable=result,
      font=("Arial", 12, "bold")).pack(pady=10)

score = Label(root, text="Score  You: 0   Computer: 0",
              font=("Arial", 12))
score.pack()

root.mainloop()