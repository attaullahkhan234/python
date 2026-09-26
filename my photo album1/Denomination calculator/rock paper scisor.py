import tkinter as tk
import random

def play(choice):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if choice == computer:
        result = "Tie!"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"You: {choice}\nComputer: {computer}\n{result}")

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x300")

tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18)).pack(pady=20)

result_label = tk.Label(window, text="Choose one")
result_label.pack(pady=10)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(window, text=choice, command=lambda x=choice: play(x)).pack(pady=5)

window.mainloop()