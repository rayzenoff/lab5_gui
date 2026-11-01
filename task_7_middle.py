import tkinter as tk


def main():
    root = tk.Tk()
    root.title("GUI Application")
    root.geometry("400x250")

    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.destroy)

    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    root.mainloop()


if __name__ == "__main__":
    main()
