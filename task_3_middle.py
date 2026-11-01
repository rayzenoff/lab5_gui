import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Простой калькулятор")
    root.geometry("370x240")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Первое число:").grid(
        row=0, column=0, sticky="w", pady=5
    )
    first_entry = ttk.Entry(frame)
    first_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Второе число:").grid(
        row=1, column=0, sticky="w", pady=5
    )
    second_entry = ttk.Entry(frame)
    second_entry.grid(row=1, column=1, pady=5)

    result_var = tk.StringVar(value="Результат: ")

    def calculate(operation):
        try:
            a = float(first_entry.get().replace(",", "."))
            b = float(second_entry.get().replace(",", "."))

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b == 0:
                    result_var.set("Ошибка: деление на ноль")
                    return
                result = a / b

            result_var.set(f"Результат: {result:g}")

        except ValueError:
            result_var.set("Ошибка: введите числа")

    operations = ["+", "-", "*", "/"]

    for i, operation in enumerate(operations):
        button = ttk.Button(
            frame,
            text=operation,
            command=lambda op=operation: calculate(op)
        )
        button.grid(
            row=2, column=i, padx=5, pady=15
        )

    ttk.Label(
        frame,
        textvariable=result_var,
        font=("Arial", 12)
    ).grid(row=3, column=0, columnspan=4, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
