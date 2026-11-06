import tkinter as tk
from tkinter import messagebox, simpledialog
import random



class MemoryTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Оценка памяти на числа")
        self.root.geometry("450x380")
        self.root.minsize(400, 300)
        self.digits_count = 1   
        self.secret_number = 0    
        self.best_score = 0      
        self.timer_id = None        

    def _create_menu(self):
        menubar = tk.Menu(self.root)

        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="Начать заново", command=self.start_game)
        game_menu.add_separator()
        game_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Игра", menu=game_menu)

        size_menu = tk.Menu(menubar, tearoff=0)
        size_menu.add_command(label="Маленькое (400x350)", command=lambda: self.set_window_size(400, 350))
        size_menu.add_command(label="Среднее (500x350)", command=lambda: self.set_window_size(500, 350))
        size_menu.add_command(label="Большое (600x450)", command=lambda: self.set_window_size(600, 450))

        self.root.config(menu=menubar)

    def start_game(self):
        self.digits_count = 1
        self.start_btn.config(text="Начать заново")

    def _create_widgets(self):
        self.stats_label = tk.Label(self.root, text="Текущая длина: 3 | Рекорд: 0 цифр", font=("Arial", 11))
        self.stats_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Нажмите «Старт», чтобы проверить память", font=("Arial", 12), wraplength=380)
        self.info_label.pack(pady=10)

        self.number_label = tk.Label(self.root, text="---" ,font=("Arial", 28, "bold"), fg="#2c3e50")
        self.number_label.pack(pady=15)
        self.answer_entry = tk.Entry(self.root, font=("Arial", 16), justify="center", state="disabled")
        self.answer_entry.pack(pady=10, ipadx=10, ipady=3)

        self.answer_entry.bind("<Return>", lambda event: self.check_answer())

        self.check_btn = tk.Button(self.root, text="Проверить", font=("Arial", 12), state="disabled", width=15, command=self.check_answer)
        self.check_btn.pack(pady=5)
        self.start_btn = tk.Button(self.root, text="Старт", font=("Arial", 12, "bold"), width=15, command=self.start_game)
        self.start_btn.pack(pady=5)

    def start_game(self):
        self.digits_count = 3
        self.start_btn.config(text="Начать заново")
        self.next_round()

    def next_round(self):
        """Генерация нового числа и показ его на 2.5 секунды"""
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)

        self.update_stats()

        low = 10 ** (self.digits_count - 1)
        high = (10 ** self.digits_count) - 1
        self.secret_number = random.randint(low, high)

        self.answer_entry.config(state="normal")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.config(state="disabled")
        self.check_btn.config(state="disabled")

        self.info_label.config(text="Запомните число:")
        self.number_label.config(text=str(self.secret_number))
        self.timer_id = self.root.after(2500, self.hide_number)

    def hide_number(self):
        """Скрытие числа и разблокировка поля ввода"""
        self.number_label.config(text="???")
        self.info_label.config(text="Введите число, которое вы видели:")
        self.answer_entry.config(state="normal")
        self.answer_entry.focus_set()  
        self.check_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryTrainerApp(root)
    root.mainloop()
