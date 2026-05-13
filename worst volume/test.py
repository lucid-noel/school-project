import tkinter as tk
import random

def move_button(event=None):
    x = random.randint(0, 300)
    y = random.randint(0, 200)
    btn.place(x=x, y=y)

root = tk.Tk()
root.title("Button")
root.geometry("400x300")

label = tk.Label(root, text="click the button", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(root, text="Click Me")

btn.place(x=150, y=100)

btn.bind("<Enter>", move_button)

root.mainloop()