import numpy as np
import tkinter as tk
from tkinter import messagebox

def solve_complex_system(A, B):
    A = np.array(A, dtype=complex)
    B = np.array(B, dtype=complex)

    D = np.linalg.det(A)

    if D == 0:
        raise ValueError("Система не имеет единственного решения (D = 0)")

    n = A.shape[0]
    solutions = []

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B
        Di = np.linalg.det(Ai)
        x_i = Di / D
        solutions.append(x_i)

    return solutions

def round_complex(c, decimal_places=2):
    return complex(round(c.real, decimal_places), round(c.imag, decimal_places))

def calculate_solutions():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("Количество уравнений должно быть положительным числом.")
        
        A = []
        for i in range(n):
            row = entry_A[i].get()
            A.append([complex(num) for num in row.split()])

        B = []
        for i in range(n):
            b = complex(entry_B[i].get())
            B.append(b)

        solutions = solve_complex_system(A, B)
        result_text = "Решения:\n"
        for i, sol in enumerate(solutions):
            rounded_sol = round_complex(sol, decimal_places=2)
            result_text += f"x_{i + 1} = {rounded_sol}\n"
        
        messagebox.showinfo("Решения", result_text)

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def setup_input_fields():
    n = int(entry_n.get())
    for widget in frame_A.winfo_children():
        widget.destroy()
    for widget in frame_B.winfo_children():
        widget.destroy()

    for i in range(n):
        label = tk.Label(frame_A, text=f"Коэффициенты {i + 1}:")
        label.pack()
        entry = tk.Entry(frame_A)
        entry.pack()
        entry_A.append(entry)

        label_b = tk.Label(frame_B, text=f"Свободный член {i + 1}:")
        label_b.pack()
        entry_b = tk.Entry(frame_B)
        entry_b.pack()
        entry_B.append(entry_b)

# Создаем главное окно
root = tk.Tk()
root.title("Решатель системы линейных уравнений с комплексными переменными")

# Ввод количества уравнений
frame_n = tk.Frame(root)
frame_n.pack(pady=10)

label_n = tk.Label(frame_n, text="Введите количество уравнений (и переменных):")
label_n.pack()

entry_n = tk.Entry(frame_n)
entry_n.pack()

button_setup = tk.Button(frame_n, text="Установить", command=setup_input_fields)
button_setup.pack()

# Ввод коэффициентов
frame_A = tk.Frame(root)
frame_A.pack(pady=10)

entry_A = []

# Ввод свободных членов
frame_B = tk.Frame(root)
frame_B.pack(pady=10)

entry_B = []

# Кнопка для расчета решений
button_calculate = tk.Button(root, text="Решить", command=calculate_solutions)
button_calculate.pack(pady=20)

# Запускаем главный цикл
root.mainloop()
