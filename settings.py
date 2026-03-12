import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import ast

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def update_data(root,username_entry,password_entry):
    login_user = username_entry.get()
    password_user = password_entry.get()
    f = open('users.txt', 'r+') # Открываем файл для чтения и записи
    file_content = f.read()
    if file_content:  # Проверка на пустоту файла
        modified_content = file_content[:-1] + ',' + "'" + login_user + "'" + ':' + "'" + password_user + "'" + '}' # Удаляем последний символ
        f.seek(0)
        f.write(modified_content)  # Записываем изменённое содержимое
        f.truncate()  # Удаляем оставшиеся данные после изменённого содержимого
    f.close()
    root.destroy()
    
    
def settings_menu():
    root = tk.Tk()
    root.title("Настройки")
    # Style
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background = "white")
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TCheckbutton", font=("Arial", 12))
    #style.configure("TFrame", background="white")
    style.configure("TFrame", background="#e0f2f7")  # Light blue background
    
    print(style)
    
    
    # Top frame (title and exit button)
    top_frame = ttk.Frame(root, style="TFrame")
    top_frame.pack(fill=tk.X)
    
    # title_label = tk.Label(top_frame, text="Настройки", font=("Arial", 16, "bold"), padding=(10, 5))
    # title_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    header_frame = tk.Frame(root, bg="#40C4FF", height=40)  # Цвет заголовка
    header_frame.pack(fill=tk.X)
    header_label = tk.Label(header_frame, text="Настройки", fg="white", bg="#40C4FF", font=("Arial", 16, "bold"))
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    exit_button = ttk.Button(header_frame, text="Выйти", command=root.destroy, style="TButton")
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)
    
    
    # Main frame (settings)
    main_frame = tk.Frame(root, bg = "white")
    main_frame.pack(expand=True, fill=tk.BOTH)
    
    
    # User name
    username_label = ttk.Label(main_frame, text="Имя пользователя", style="TLabel")
    username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    username_entry = ttk.Entry(main_frame, style="TEntry")
    username_entry.grid(row=0, column=1, sticky=tk.E+tk.W, padx=5, pady=5)
    
    
    # Password
    password_label = ttk.Label(main_frame, text="Пароль", style="TLabel")
    password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    password_entry = ttk.Entry(main_frame, style="TEntry", show="*")
    password_entry.grid(row=1, column=1, sticky=tk.E+tk.W, padx=5, pady=5)
    
    
    # Working directory
    directory_label = ttk.Label(main_frame, text="Рабочая директория", style="TLabel")
    directory_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    directory_entry = ttk.Entry(main_frame, style="TEntry")
    directory_entry.grid(row=2, column=1, sticky=tk.E+tk.W, padx=5, pady=5)
    browse_button = ttk.Button(main_frame, text="Обзор", command=browse_directory, style="TButton")
    browse_button.grid(row=2, column=2, padx=5, pady=5)
    
    
    # Discipline name
    discipline_label = ttk.Label(main_frame, text="Название по дисциплине", style="TLabel")
    discipline_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
    discipline_entry = ttk.Entry(main_frame, style="TEntry")
    discipline_entry.grid(row=3, column=1, sticky=tk.E+tk.W, padx=5, pady=5)
    
    
    # Default ticket name
    ticket_label = ttk.Label(main_frame, text="Название билета по умолчанию", style="TLabel")
    ticket_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
    ticket_entry = ttk.Entry(main_frame, style="TEntry")
    ticket_entry.grid(row=4, column=1, sticky=tk.E+tk.W, padx=5, pady=5)

    #Update data button
    update_button = ttk.Button(main_frame, text="Ввод", command=lambda: update_data(root, username_entry, password_entry), style="TButton")
    update_button.grid(row=5, column=2, padx=5, pady=5)
    
    # Show warning checkbox
    warning_check = ttk.Checkbutton(main_frame, text="Показывать предупреждение при замене сеанса", style="TCheckbutton")
    warning_check.grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
    
    
    root.mainloop()