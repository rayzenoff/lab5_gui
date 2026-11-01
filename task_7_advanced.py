import sqlite3
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox


DB_PATH = Path(__file__).with_name("contacts.db")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()

    root = tk.Tk()
    root.title("Справочник контактов — SQLite")
    root.geometry("600x400")

    form = ttk.Frame(root, padding=12)
    form.pack(fill="x")

    ttk.Label(form, text="Имя:").grid(
        row=0, column=0, padx=5, pady=5
    )
    name_entry = ttk.Entry(form, width=35)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(form, text="Телефон:").grid(
        row=1, column=0, padx=5, pady=5
    )
    phone_entry = ttk.Entry(form, width=35)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    columns = ("id", "name", "phone")
    table = ttk.Treeview(
        root, columns=columns, show="headings",
        selectmode="browse"
    )

    table.heading("id", text="ID")
    table.heading("name", text="Имя")
    table.heading("phone", text="Телефон")

    table.column("id", width=50, stretch=False)
    table.column("name", width=200)
    table.column("phone", width=200)

    def refresh_contacts():
        for item in table.get_children():
            table.delete(item)

        cursor = conn.execute(
            "SELECT id, name, phone FROM contacts ORDER BY id"
        )
        for contact in cursor.fetchall():
            table.insert("", tk.END, values=contact)

    def add_contact():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning(
                "Ошибка", "Заполните имя и телефон!"
            )
            return

        conn.execute(
            "INSERT INTO contacts (name, phone) VALUES (?, ?)",
            (name, phone)
        )
        conn.commit()

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        refresh_contacts()

    def delete_contact():
        selected = table.selection()

        if not selected:
            messagebox.showwarning(
                "Ошибка", "Выберите контакт для удаления!"
            )
            return

        contact_id = table.item(
            selected[0], "values"
        )[0]

        conn.execute(
            "DELETE FROM contacts WHERE id = ?",
            (contact_id,)
        )
        conn.commit()
        refresh_contacts()

    buttons = ttk.Frame(root, padding=10)
    buttons.pack(fill="x")

    ttk.Button(
        buttons,
        text="Добавить",
        command=add_contact
    ).pack(side="left", padx=5)

    ttk.Button(
        buttons,
        text="Удалить",
        command=delete_contact
    ).pack(side="left", padx=5)

    ttk.Button(
        buttons,
        text="Обновить",
        command=refresh_contacts
    ).pack(side="left", padx=5)

    table.pack(
        fill="both", expand=True,
        padx=12, pady=10
    )

    def on_close():
        conn.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    refresh_contacts()
    root.mainloop()


if __name__ == "__main__":
    main()
