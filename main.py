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


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryTrainerApp(root)
    root.mainloop()
