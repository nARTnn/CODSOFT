##Creating a basic calculator

operators = ["+", "-", "*", "/"]

def numbers():
    
    #This function requests 2 numbers from a user
    
    max = 2
    times = 0
    list_of_nums = []
    while times < max :
        num = input("Enter a number: ")
        if num.isalpha():
            print("Invalid number. Please enter a valid number")
        else:
            times += 1
            num = int(num)
            list_of_nums.append(num)
    print(list_of_nums)    
    return list_of_nums


def calculator(list_of_nums):
    
    #In this function, the user is requested an operator and it is also where the calculation is done.
    
    while True:
        user_op = input("Choose an operator (-, +, *, / ): ")
        if user_op == "-" in operators:
            res = list_of_nums[0] - list_of_nums[1]
            break
        elif user_op == "+" in operators:
            res = list_of_nums[0] + list_of_nums[1]
            break
        elif user_op == "*" in operators:
            res = list_of_nums[0] * list_of_nums[1]
            break
        elif user_op == "/" in operators:
                if list_of_nums[1] == 0:
                    print("Can't divide by zero")
                    break
                else:
                    res = list_of_nums[0] / list_of_nums[1]
                    break
        else:
            print("Invalid operator, please choose from these operators (-, +, *, /)")
        return res        
    
if __name__ == "__main__":
    list_of_nums = numbers()
    print(calculator(list_of_nums))
    