import time
import tkinter as tk
from tkinter import ttk


class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Секундомер")
        self.root.geometry("380x230")
        self.root.resizable(False, False)

        self.running = False
        self.elapsed = 0.0
        self.start_time = 0.0
        self.after_id = None

        self.time_var = tk.StringVar(value="00:00.0")

        frame = ttk.Frame(root, padding=25)
        frame.pack(expand=True)

        ttk.Label(
            frame,
            text="Секундомер",
            font=("Arial", 16)
        ).pack(pady=10)

        ttk.Label(
            frame,
            textvariable=self.time_var,
            font=("Arial", 36, "bold")
        ).pack(pady=15)

        buttons = ttk.Frame(frame)
        buttons.pack()

        ttk.Button(
            buttons,
            text="Старт",
            command=self.start
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            buttons,
            text="Пауза",
            command=self.pause
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            buttons,
            text="Сброс",
            command=self.reset
        ).grid(row=0, column=2, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def get_elapsed(self):
        if self.running:
            return self.elapsed + time.perf_counter() - self.start_time
        return self.elapsed

    def update_display(self):
        total = int(self.get_elapsed() * 10)
        minutes, remainder = divmod(total, 600)
        seconds, tenths = divmod(remainder, 10)

        self.time_var.set(
            f"{minutes:02d}:{seconds:02d}.{tenths}"
        )

        self.after_id = None
        if self.running:
            self.after_id = self.root.after(
                50, self.update_display
            )

    def start(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            self.update_display()

    def pause(self):
        if self.running:
            self.elapsed = self.get_elapsed()
            self.running = False

            if self.after_id is not None:
                self.root.after_cancel(self.after_id)
                self.after_id = None

            self.update_display()

    def reset(self):
        self.pause()
        self.elapsed = 0.0
        self.update_display()

    def close(self):
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
        self.root.destroy()


def main():
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()


if __name__ == "__main__":
    main()
