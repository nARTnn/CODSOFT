# ##Creating a basic calculator

import tkinter as tk
import calculator
from calculator import *
# operatitors = ["+", "-", "*", "/"]

# def numbers():
    
#     #This function requests 2 numbers from a user
    
#     max = 2
#     times = 0
#     list_of_nums = []
#     while times < max :
#         # if times < max:
#         num = input("Enter a number: ")
#         if num.isalpha():
#             print("Invalid number. Please enter a valid number")
#         else:
#             times += 1
#             num = int(num)
#             list_of_nums.append(num)
#     print(list_of_nums)    
#     return list_of_nums


# def calculator(list_of_nums):
    
#     #In this function, the user is requested an operator and it is also where the calculation is done.
    
#     while True:
#         user_op = input("Choose an operator (-, +, *, / ): ")
#         if user_op == "-" in operatitors:
#             res = list_of_nums[0] - list_of_nums[1]
#             print(res)
#             break
#         elif user_op == "+" in operatitors:
#             res = list_of_nums[0] + list_of_nums[1]
#             print(res)
#             break
#         elif user_op == "*" in operatitors:
#             res = list_of_nums[0] * list_of_nums[1]
#             print(res)
#             break
#         elif user_op == "/" in operatitors:
#             if list_of_nums[1] == 0:
#                 print("Can't divide by zero")
#                 break
#             else:
#                 res = list_of_nums[0] / list_of_nums[1]
#                 print(res)
#                 break
#         else:
#             print("Invalid operator, please choose from these operators (-, +, *, /)")
#     return res        
    
# if __name__ == "__main__":
#     list_of_nums = numbers()
#     calculator(list_of_nums)
    
    
    
##creating the window for gui

root = tk.Tk()
root.geometry("400x400")
root.title("Basic Calculator")

text_res = tk.Text(root, height=2, width=22, font=("Arial", 18))
text_res.pack(padx=20, pady=20)
text_res.grid(columnspan=8)

bt1 = tk.Button(root, text="1", command=lambda: add_to_calculate(1), width=5, font=("Arial", 12))
bt1.grid(row=4, column=1)

bt2 = tk.Button(root, text="2", command=lambda: add_to_calculate(2), width=5, font=("Arial", 12))
bt2.grid(row=4, column=2)

bt3 = tk.Button(root, text="3", command=lambda: add_to_calculate(3), width=5, font=("Arial", 12))
bt3.grid(row=4, column=3)

bt4 = tk.Button(root, text="4", command=lambda: add_to_calculate(4), width=5, font=("Arial", 12))
bt4.grid(row=3, column=1)

bt5 = tk.Button(root, text="5", command=lambda: add_to_calculate(5), width=5, font=("Arial", 12))
bt5.grid(row=3, column=2)

bt6 = tk.Button(root, text="6", command=lambda: add_to_calculate(6), width=5, font=("Arial", 12))
bt6.grid(row=3, column=3)

bt7 = tk.Button(root, text="7", command=lambda: add_to_calculate(7), width=5, font=("Arial", 12))
bt7.grid(row=2, column=1)

bt8 = tk.Button(root, text="8", command=lambda: add_to_calculate(8), width=5, font=("Arial", 12))
bt8.grid(row=2, column=2)

bt9 = tk.Button(root, text="9", command=lambda: add_to_calculate(9), width=5, font=("Arial", 12))
bt9.grid(row=2, column=3)

bt0 = tk.Button(root, text="0", command=lambda: add_to_calculate(0), width=5, font=("Arial", 12))
bt0.grid(row=5, column=1)

bt_open = tk.Button(root, text="(", command=lambda: add_to_calculate("("), width=5, font=("Arial", 12))
bt_open.grid(row=5, column=2)

bt_close = tk.Button(root, text=")", command=lambda: add_to_calculate(")"), width=5, font=("Arial", 12))
bt_close.grid(row=5, column=3)

bt_clear_screen = tk.Button(root, text="C", command=lambda: add_to_calculate("C"), width=5, font=("Arial", 12))
bt_clear_screen.grid(row=6, column=1)

bt_clear_lastEntry = tk.Button(root, text="CE", command=lambda: add_to_calculate("CE"), width=5, font=("Arial", 12))
bt_clear_lastEntry.grid(row=6, column=2)

bt_decimal = tk.Button(root, text=".", command=lambda: add_to_calculate("."), width=5, font=("Arial", 12))
bt_decimal.grid(row=6, column=3)

bt_plus = tk.Button(root, text="+", command=lambda: add_to_calculate("+"), width=5, font=("Arial", 12))
bt_plus.grid(row=2, column=5)

bt_minus = tk.Button(root, text="-", command=lambda: add_to_calculate("-"), width=5, font=("Arial", 12))
bt_minus.grid(row=3, column=5)

bt_multiply = tk.Button(root, text="*", command=lambda: add_to_calculate("*"), width=5, font=("Arial", 12))
bt_multiply.grid(row=4, column=5)

bt_divide = tk.Button(root, text="/", command=lambda: add_to_calculate("/"), width=5, font=("Arial", 12))
bt_divide.grid(row=5, column=5)

bt_equal = tk.Button(root, text="=", command=lambda: add_to_calculate("="), width=5, font=("Arial", 12))
bt_equal.grid(row=6, column=5)


root.mainloop()