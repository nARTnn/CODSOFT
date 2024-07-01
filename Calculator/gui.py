import tkinter as tk
# import calculator
from calculator import add_to_calculate, clear, calculation

##creating the window for gui
def runGUI():
    
    root = tk.Tk()
    root.geometry("300x275")
    root.title("Basic Calculator")

    text_res = tk.Text(root, height=2, width=22, font=("Arial", 18))
    text_res.pack(padx=20, pady=20)
    text_res.grid(columnspan=8)

    bt1 = tk.Button(root, text="1", command=lambda: add_to_calculate(1, text_res), width=5, font=("Arial", 12))
    bt1.grid(row=4, column=1)

    bt2 = tk.Button(root, text="2", command=lambda: add_to_calculate(2, text_res), width=5, font=("Arial", 12))
    bt2.grid(row=4, column=2)

    bt3 = tk.Button(root, text="3", command=lambda: add_to_calculate(3, text_res), width=5, font=("Arial", 12))
    bt3.grid(row=4, column=3)

    bt4 = tk.Button(root, text="4", command=lambda: add_to_calculate(4, text_res), width=5, font=("Arial", 12))
    bt4.grid(row=3, column=1)

    bt5 = tk.Button(root, text="5", command=lambda: add_to_calculate(5, text_res), width=5, font=("Arial", 12))
    bt5.grid(row=3, column=2)

    bt6 = tk.Button(root, text="6", command=lambda: add_to_calculate(6, text_res), width=5, font=("Arial", 12))
    bt6.grid(row=3, column=3)

    bt7 = tk.Button(root, text="7", command=lambda: add_to_calculate(7, text_res), width=5, font=("Arial", 12))
    bt7.grid(row=2, column=1)

    bt8 = tk.Button(root, text="8", command=lambda: add_to_calculate(8, text_res), width=5, font=("Arial", 12))
    bt8.grid(row=2, column=2)

    bt9 = tk.Button(root, text="9", command=lambda: add_to_calculate(9, text_res), width=5, font=("Arial", 12))
    bt9.grid(row=2, column=3)

    bt0 = tk.Button(root, text="0", command=lambda: add_to_calculate(0, text_res), width=5, font=("Arial", 12))
    bt0.grid(row=5, column=1)

    bt_open = tk.Button(root, text="(", command=lambda: add_to_calculate("(", text_res), width=5, font=("Arial", 12))
    bt_open.grid(row=5, column=2)

    bt_close = tk.Button(root, text=")", command=lambda: add_to_calculate(")", text_res), width=5, font=("Arial", 12))
    bt_close.grid(row=5, column=3)

    bt_clear_entry = tk.Button(root, text="C", command=lambda: clear(text_res, -1), width=5, font=("Arial", 12))
    bt_clear_entry.grid(row=6, column=1)

    bt_decimal = tk.Button(root, text=".", command=lambda: add_to_calculate(".", text_res), width=5, font=("Arial", 12))
    bt_decimal.grid(row=6, column=2)

    bt_plus = tk.Button(root, text="+", command=lambda: add_to_calculate("+", text_res), width=5, font=("Arial", 12))
    bt_plus.grid(row=2, column=4)

    bt_minus = tk.Button(root, text="-", command=lambda: add_to_calculate("-", text_res), width=5, font=("Arial", 12))
    bt_minus.grid(row=3, column=4)

    bt_multiply = tk.Button(root, text="*", command=lambda: add_to_calculate("*", text_res), width=5, font=("Arial", 12))
    bt_multiply.grid(row=4, column=4)

    bt_divide = tk.Button(root, text="/", command=lambda: add_to_calculate("/", text_res), width=5, font=("Arial", 12))
    bt_divide.grid(row=6, column=3)

    bt_equal = tk.Button(root, text="=", command=lambda: calculation(text_res), height=3,width= 5, font=("Arial", 12))
    bt_equal.grid(row=5, column=4, rowspan=2)
    
    root.mainloop()
    

runGUI()