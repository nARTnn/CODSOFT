'''TODO: Create a basic calculator''' 

calculate = ""

def add_to_calculate(symbol, text_res):
    global calculate
    calculate += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculate)

def calculation(text_res):
    global calculate
    try:
        calculate = str(eval(calculate))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, calculate)
    except Exception:
        clearAll(text_res)
        text_res.insert(1.0, "Error")

def clearAll(text_res):
    global calculate
    calculate = ""
    text_res.delete(1.0, "end")
    
def clear(text_res, d : int):
    global calculate
    calculate = calculate[0:-1]
    text_res.delete(1.0, "end")
    text_res.insert("end", calculate)