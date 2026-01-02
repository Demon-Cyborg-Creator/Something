import tkinter as tk
import time
import threading
import random

# Window setup
root = tk.Tk()
root.title("Glow Text")
root.geometry("700x400")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(root, width=700, height=400, bg="black", highlightthickness=0)
canvas.pack()

text = "Nirvana loves 7 Girls"
x, y = 350, 180

# Function to create glowing text
def glow_text():
    for i in range(1, 11):
        canvas.delete("all")

        # Glow layers
        for glow in range(5):
            canvas.create_text(
                x, y,
                text=text,
                fill="#ff8800",
                font=("Arial", 32, "bold")
            )

        root.update()
        time.sleep(0.2)

    add_hearts()

# Function to add heart emojis around text
def add_hearts():
    hearts = ["❤️", "🧡", "💖", "💕"]
    for _ in range(30):
        hx = random.randint(50, 650)
        hy = random.randint(50, 350)
        canvas.create_text(
            hx, hy,
            text=random.choice(hearts),
            fill="orange",
            font=("Arial", 20)
        )
        root.update()
        time.sleep(0.05)

# Run animation in separate thread
threading.Thread(target=glow_text).start()

root.mainloop()

