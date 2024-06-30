'''TODO: Create a basic calculator''' 

calculate = ""

def add_to_calculate(symbol):
    global calculate
    calculate += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculate)

def calculation():
    global calculate
    try:
        calculate = str(eval(calculate))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, calculate)
    except:
        clear()
        text_res.insert(1.0, "Error")

def clear():
    global calculate
    calculate = ""
    text_res.delete(1.0, "end")

