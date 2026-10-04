import tkinter as tk
from tkinter import messagebox, font
import random


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.root.geometry("420x360")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        self.low = 1
        self.high = 100
        self.max_attempts = 10
        self.reset_game()

        title_font = font.Font(family="Helvetica", size=20, weight="bold")
        normal_font = font.Font(family="Helvetica", size=11)
        big_font = font.Font(family="Helvetica", size=14, weight="bold")

        self.title_label = tk.Label(
            root,
            text="Guess the Number",
            font=title_font,
            bg="#2b2b2b",
            fg="#ffffff",
        )
        self.title_label.pack(pady=(20, 5))

        self.info_label = tk.Label(
            root,
            text=f"I'm thinking of a number between {self.low} and {self.high}.",
            font=normal_font,
            bg="#2b2b2b",
            fg="#cccccc",
        )
        self.info_label.pack(pady=(0, 5))

        self.attempts_label = tk.Label(
            root,
            text=self.attempts_text(),
            font=normal_font,
            bg="#2b2b2b",
            fg="#ffd700",
        )
        self.attempts_label.pack(pady=(0, 10))

        self.entry = tk.Entry(
            root,
            font=big_font,
            width=8,
            justify="center",
            bg="#3c3f41",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
        )
        self.entry.pack(pady=(0, 10))
        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.make_guess())

        self.guess_button = tk.Button(
            root,
            text="Guess",
            font=normal_font,
            width=10,
            bg="#4caf50",
            fg="#ffffff",
            activebackground="#45a049",
            activeforeground="#ffffff",
            relief="flat",
            command=self.make_guess,
        )
        self.guess_button.pack(pady=(0, 10))

        self.hint_label = tk.Label(
            root,
            text="",
            font=normal_font,
            bg="#2b2b2b",
            fg="#ffffff",
            wraplength=380,
            justify="center",
        )
        self.hint_label.pack(pady=(0, 10))

        self.restart_button = tk.Button(
            root,
            text="New Game",
            font=normal_font,
            width=10,
            bg="#2196f3",
            fg="#ffffff",
            activebackground="#1976d2",
            activeforeground="#ffffff",
            relief="flat",
            command=self.reset_and_start,
        )
        self.restart_button.pack(pady=(5, 10))

    def reset_game(self):
        self.target = random.randint(self.low, self.high)
        self.attempts_left = self.max_attempts
        self.game_over = False

    def attempts_text(self):
        return f"Attempts left: {self.attempts_left} / {self.max_attempts}"

    def reset_and_start(self):
        self.reset_game()
        self.info_label.config(
            text=f"I'm thinking of a number between {self.low} and {self.high}."
        )
        self.attempts_label.config(text=self.attempts_text())
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.entry.focus()

    def make_guess(self):
        if self.game_over:
            return

        raw = self.entry.get().strip()
        if not raw:
            self.hint_label.config(text="Please enter a number.", fg="#ff9800")
            return

        try:
            guess = int(raw)
        except ValueError:
            self.hint_label.config(text="That's not a valid integer.", fg="#ff9800")
            return

        if guess < self.low or guess > self.high:
            self.hint_label.config(
                text=f"Out of range! Enter a number from {self.low} to {self.high}.",
                fg="#ff9800",
            )
            return

        self.attempts_left -= 1
        self.entry.delete(0, tk.END)

        if guess == self.target:
            self.game_over = True
            used = self.max_attempts - self.attempts_left
            self.hint_label.config(
                text=f"Correct! You got it in {used} attempt(s).",
                fg="#4caf50",
            )
            self.attempts_label.config(text="You win!")
            self.entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            messagebox.showinfo(
                "Winner!", f"You guessed {self.target} in {used} attempt(s)."
            )
            return

        if self.attempts_left == 0:
            self.game_over = True
            self.hint_label.config(
                text=f"Out of attempts! The number was {self.target}.",
                fg="#f44336",
            )
            self.attempts_label.config(text="Game over")
            self.entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            messagebox.showinfo(
                "Game Over", f"No attempts left. The number was {self.target}."
            )
            return

        if guess < self.target:
            self.hint_label.config(text="Too low! Try higher.", fg="#ff9800")
        else:
            self.hint_label.config(text="Too high! Try lower.", fg="#ff9800")

        self.attempts_label.config(text=self.attempts_text())


def main():
    root = tk.Tk()
    GuessNumberGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()