import tkinter as tk
from PIL import Image, ImageTk

def open_list():
    # Действия при выборе кнопки "Список"
    print("Выбран пункт меню 'Список'")

def open_administration():
    # Действия при выборе кнопки "Администрирование"
    print("Выбран пункт меню 'Администрирование'")

def exit_app():
    # Действия при выборе кнопки "Выйти"
    print("Выбран пункт меню 'Выйти'")
    root.destroy()

def on_enter(e):
    e.widget.config(bg='#FFA500')  # Измененный цвет на светло-оранжевый при наведении

def on_leave(e):
    e.widget.config(bg='#4169E1')  # Возвращение к обычному цвету при уходе мыши

# Создание главного окна
root = tk.Tk()

# Добавление фона
background_image = tk.PhotoImage(file='C:/Users/kadry/Downloads/catridge-img.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Размещение изображения на весь экран
background_label.image = background_image  # Сохраняем ссылку на изображение, чтобы избежать удаления из памяти


# Создание фрейма для кнопок
button_frame = tk.Frame(root)
button_frame.pack()

# Создание кнопок
open_list_button = tk.Button(button_frame, text="Список", width=30, height=10, command=open_list, bg='#4169E1', fg='black')  # Измененный цвет на светло-синий
open_administration_button = tk.Button(button_frame, text="Администрирование", width=30, height=10, command=open_administration, bg='#4169E1', fg='black')  # Измененный цвет на светло-синий
exit_button = tk.Button(button_frame, text="Выйти", width=30, height=10, command=exit_app, bg='#4169E1', fg='black')  # Измененный цвет на светло-синий

# Привязка событий наведения мыши на кнопки
open_list_button.bind("<Enter>", on_enter)
open_list_button.bind("<Leave>", on_leave)
open_administration_button.bind("<Enter>", on_enter)
open_administration_button.bind("<Leave>", on_leave)
exit_button.bind("<Enter>", on_enter)
exit_button.bind("<Leave>", on_leave)

# Размещение кнопок с использованием менеджера геометрии grid
open_list_button.grid(row=1, column=0, pady=50)
open_administration_button.grid(row=2, column=0, pady=100)  # Измененное размещение кнопки "Администрирование"
exit_button.grid(row=3, column=0, pady=150)  # Измененное размещение кнопки "Выйти"

# Расположение кнопок по центру экрана
root.update_idletasks()
width = root.winfo_width()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2) + 50  # Измененное размещение кнопки "Выйти"
root.geometry(f"+{x}+{y}")

root.attributes('-fullscreen', True)

# Запуск главного цикла приложения
root.mainloop()
