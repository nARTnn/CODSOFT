'''TODO: Use a combination of random characters to
generate a password of the specified length.'''

import string
import random
 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
 
def number_of_char():
    min = 6
    max = 16
    while True:
        user_input = input("How many characters do you want in your password? ")
        try:
            characters_number = int(user_input)
            if characters_number < min:
                print("Your number should be at least 6.")
            elif characters_number > max:
                print("Password is too long. You might forget it.")
            else:
                return characters_number 
        except:
            print("Please, Enter numbers only.")

def shuffle(characters_number):
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    
    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))
    return part1, part2

def result(part1, part2):
    result = []
    
    for x in range(part1):
    
        result.append(s1[x])
        result.append(s2[x])
    
    for x in range(part2):
    
        result.append(s3[x])
        result.append(s4[x])
    
    random.shuffle(result)
    
    password = "".join(result)
    print("Strong Password: ", password)

if __name__ == "__main__":
    characters_number = number_of_char()
    part1, part2 = shuffle(characters_number)
    result(part1, part2)
    