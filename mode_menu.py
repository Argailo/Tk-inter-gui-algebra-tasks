import tkinter as tk
from tkinter import messagebox, ttk, filedialog

def Page3_button1(root, login_user):
    root.destroy()
    generator_page(login_user)
def Page3_button2(root):
    root.destroy()
    quick_cast()
    messagebox.showinfo("Информация", f"Билеты сгенерированны!")

def mode_menu(login_user):
    window = tk.Tk()
    window.title("Главное меню")

    # Заголовок
    header_frame = tk.Frame(window, bg="#40C4FF", height=40)  # Цвет заголовка
    header_frame.pack(fill=tk.X)
    header_label = tk.Label(header_frame, text=f"Пользователь: {login_user}", fg="white", bg="#40C4FF", font=("Arial", 12))
    header_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Кнопка выхода (справа)
    exit_button = tk.Button(header_frame, text="→", command=window.quit, bg="#40C4FF", fg="white", font=("Arial", 12))
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Основное содержимое
    main_frame = tk.Frame(window, bg="white")
    main_frame.pack(expand=True, fill=tk.BOTH)


    # Кнопка 1

    button1 = ttk.Button(main_frame, text="Создание билетов", command=lambda: Page3_button1(window, login_user), width=20, style="my.TButton")
    button1.pack(pady=20)

    # Кнопка 2
    button2 = ttk.Button(main_frame, text="Быстрая генерация",command =lambda: Page3_button2(window), width=20, style="my.TButton")
    button2.pack(pady=10)


    # Настройка стиля кнопок (опционально, для более привлекательного вида)
    style = ttk.Style()
    style.configure("my.TButton", background="#D3D3D3", foreground="black", padding=10, relief="flat", borderwidth=0)


    window.mainloop()