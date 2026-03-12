import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sys
from PIL import Image,ImageTk
import ast
from quick_generate import * #там же импорты других программ и quick_cast
from settings import *
from task1_menu import *




def close_window():
    """Закрывает окно."""
    root.destroy()


    
def Page2_button1(root, login_user):
    root.destroy()
    mode_menu(login_user)
def Page2_button2(root):
     root.destroy()
     settings_menu()
    
def second_menu(login_user):
    root = tk.Tk()
    root.title("Главное меню")

    # Заголовок
    header_frame = tk.Frame(root, bg="#40C4FF", height=40)  # Цвет заголовка
    header_frame.pack(fill=tk.X)
    header_label = tk.Label(header_frame, text=f"Пользователь: {login_user}", fg="white", bg="#40C4FF", font=("Arial", 12))
    header_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Кнопка выхода (справа)
    exit_button = tk.Button(header_frame, text="→", command=root.quit, bg="#40C4FF", fg="white", font=("Arial", 12))
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Основное содержимое
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(expand=True, fill=tk.BOTH)


    # Кнопка 1

    button1 = ttk.Button(main_frame, text="Линейная Алгебра", command=lambda: Page2_button1(root, login_user), width=20, style="my.TButton")
    button1.pack(pady=20)

    # Кнопка 2
    button2 = ttk.Button(main_frame, text="Настройки",command =lambda: Page2_button2(root), width=20, style="my.TButton")
    button2.pack(pady=10)


    # Настройка стиля кнопок (опционально, для более привлекательного вида)
    style = ttk.Style()
    style.configure("my.TButton", background="#D3D3D3", foreground="black", padding=10, relief="flat", borderwidth=0)


    root.mainloop()


def login():
    login_user = entry_login.get()
    password_user = entry_password.get()
    f = open('users.txt', 'r')
    x = f.read()
    x = ast.literal_eval(x)
    #привет, если ты читаешь это, то достаточно заинтересован. Если бы я проводил ctf
    #то сказал бы, что это то самое место, откуда ты можешь залезть в файлы логин-пароля инъекцией
    #код логин-пароля парсится в формат словаря, так что выйди за пределы словаря
    #так же ты можешь просто вызвать другие функции
    if login_user in x and x[login_user] == password_user:
        messagebox.showinfo("Информация", f"Доступ {login_user} разрешён ")
        root.destroy()
        second_menu(login_user)
    else:
        messagebox.showinfo("Ошибка", f"Пользователь {login_user} не существует")
        root.destroy()
    

def create_rounded_rectangle(canvas, x1, y1, x2, y2, r=20, **kwargs):
    """Создает закругленный прямоугольник на канвасе."""
    canvas.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_rectangle(x1 + r, y1, x2 - r, y2, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_rectangle(x1, y1 + r, x1 + r, y2 - r, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
    canvas.create_rectangle(x2 - r, y1 + r, x2, y2 - r, fill=kwargs.get('fill'), outline=kwargs.get('outline'))


def exit_app():
    root.destroy()

def  gen(data):

    #print(f"t1_1_1 = {data.t1_1_1.get()}")
    
    selected_methods = [data.methods[i] for i, data.var in enumerate(data.checkboxes) if data.var.get()]
    print(selected_methods)
    # gen_window = tk.Tk()
    # gen_window.title("Выбранные методы")
    if selected_methods:
    #     result_label = tk.Label(gen_window, text="\n".join(selected_methods))
    #     result_label.pack(padx=10, pady=10)

        # В секции ифов вставть свои программы
        if "Перемножение двух матриц" in selected_methods:
            #print((int(data.t1_1_1.get()),int(data.t1_1_2.get())),(int(data.t1_2_1.get()),int(data.t1_2_2.get())),(int(data.t1_3_1.get()),int(data.t1_3_2.get())))
            first_task_menu((int(data.t1_1_1.get()),int(data.t1_1_2.get())),(int(data.t1_2_1.get()),int(data.t1_2_2.get())),(int(data.t1_3_1.get()),int(data.t1_3_2.get())))
            #first_task_menu((1,2),(2,1),(1,10))
        if "СЛАУ методом Крамера" in selected_methods:
            print('Гойда2')
        if "СЛАУ методом обратной матрицы" in selected_methods:
            print('Гойда3')
        if "Матричные уравнения вида AXB=C" in selected_methods:
            print('Гойда4')
        if "СЛАУ методом Гаусса" in selected_methods:
            print('Гойда5')
        if "Ручное составление" in selected_methods:
            print('Гойда6')
            
    else:
        result_label = tk.Label(new_window, text="Вы не выбрали ни одного метода. Пожалуйста не играйтесь с моими терпением.")
        result_label.pack(padx=10, pady=10)

def generator_page(login_user):
    root = tk.Tk()
    root.title("Генератор задач")
    
    # Пользователь

    canvas = tk.Canvas(root, width=root.winfo_screenmmwidth(), height=30, bg="#40C4FF")  # Настраиваемый цвет и размер
    canvas.create_text(10, 15, anchor=tk.W, text=f"Пользователь: {login_user}", font=("Arial", 14), fill="black")
    canvas.grid(row=0, column=0, columnspan=3, sticky="ew") # Растягиваем на всю ширину

        
    exit_button = ttk.Button(root, text="Выйти", command=exit_app)
    exit_button.grid(row=0, column=2, sticky=tk.E, padx=10, pady=10)
    
    # Методы
    class data_container:
        methods = [
            "Перемножение двух матриц",
            "СЛАУ методом Крамера",
            "СЛАУ методом обратной матрицы",
            "Матричные уравнения вида AXB=C",
            "СЛАУ методом Гаусса"]
        checkboxes = []
        var= tk.BooleanVar()

    
    data = data_container()
    #data.var = tk.BooleanVar()
    for i, method in enumerate(data.methods):
        print(i, method)
        data.var = tk.BooleanVar()
        data.checkbox = ttk.Checkbutton(root, text=method, variable=data.var)
        data.checkbox.grid(row=i + 1, column=0, sticky=tk.W, padx=10, pady=5)
        data.checkboxes.append(data.var)
    
    
    # Параметры для каждого метода (простые Entry поля, для демонстрации)
    params_frames = []
    for i in range(len(data.methods)):
        frame = ttk.LabelFrame(root, text=f"Параметры для {data.methods[i]}")
        frame.grid(row=i + 1, column=1, columnspan=2, padx=10, pady=5, sticky=tk.W)
        params_frames.append(frame)
    
        # Пример параметров для одного из методов
        if i == 0:
            ttk.Label(frame, text="Размер матрицы A").grid(row=0, column=0)
            data.t1_1_1 = ttk.Entry(frame, width=5)
            data.t1_1_1.grid(row=0, column=1)  # Строки
            data.t1_1_2 = ttk.Entry(frame, width=5)
            data.t1_1_2.grid(row=0, column=2)  # Столбцы
            ttk.Label(frame, text="Размер матрицы B").grid(row=0, column=3)
            data.t1_2_1 = ttk.Entry(frame, width=5)
            data.t1_2_1.grid(row=0, column=4)  # Строки
            data.t1_2_2 = ttk.Entry(frame, width=5)
            data.t1_2_2.grid(row=0, column=5)  # Столбцы
            ttk.Label(frame, text="Диапазон").grid(row=1,column=0,columnspan=2)
            data.t1_3_1 = ttk.Entry(frame, width=5)
            data.t1_3_1.grid(row=1, column=2)  # От
            data.t1_3_2 = ttk.Entry(frame, width=5)
            data.t1_3_2.grid(row=1, column=3)  # До
            #print(data.t1_1_1)
    
    # Билеты
    ttk.Label(root, text="Количество билетов", font=("Arial", 12)).grid(row=len(data.methods) + 2, column=0, columnspan=2, padx=10, pady=10)
    ttk.Entry(root, width=20).grid(row=len(data.methods) + 2, column=1,columnspan=2, padx=10, pady=10)
    
    
    generate_button = ttk.Button(root, text="Генерация билетов",command=lambda: gen(data),width=20) 
    generate_button.grid(row=len(data.methods) + 3, column=1, columnspan=2, pady=10)
    
    root.mainloop()


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
    
# Создание основного окна
root = tk.Tk()
root.title("Programm name")
root.geometry("400x300")
root.configure(bg="white")

# Создание канваса для рисования
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack()

# Добавление закругленного фона
create_rounded_rectangle(canvas, 50, 50, 350, 200, r=20, fill="white", outline="white")

# Добавление места для иконки
icon_frame =tk.Canvas(root, bg="white", width=50, height=50)
img= ImageTk.PhotoImage(Image.open("icon.png"))
testImg = icon_frame.create_image(2,2, anchor = 'nw', image = img)
icon_frame.place(x=175, y = 10)

# Закругленные поля ввода
create_rounded_rectangle(canvas, 100, 90, 300, 120, r=15, fill="lightgray", outline="lightgray")
entry_login = tk.Entry(root, width=30, bd=0, highlightthickness=0, background = 'lightgray')
entry_login.place(x=110, y=95)

print(entry_login)

create_rounded_rectangle(canvas, 100, 140, 300, 170, r=15, fill="lightgray", outline="lightgray")
entry_password = tk.Entry(root, show='*', width=30, bd=0, highlightthickness=0, background="lightgray")
entry_password.place(x=110, y=145)

# Создание кнопки для входа
username = "admin"
create_rounded_rectangle(canvas, 110, 200, 300, 240, r=10, fill="lightblue", outline="lightblue")
button_login = tk.Button(root, text="Войти в аккаунт", command=login, bg='lightblue', font=("Helvetica", 12), relief="flat")

button_login.place(x=150, y=205, width=120)

# Запуск главного цикла приложения
root.mainloop()