import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Цветная панель")
    root.geometry("400x300")

    colors = ["red", "green", "blue", "yellow", "purple"]
    current_color = 0

    panel = tk.Frame(root, bg=colors[current_color])
    panel.pack(pady=20, padx=20, fill="both", expand=True)

    def change_color():
        nonlocal current_color
        current_color = (current_color + 1) % len(colors)
        panel.config(bg=colors[current_color])

    button = tk.Button(
        root,
        text="Изменить цвет",
        command=change_color
    )
    button.pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()
