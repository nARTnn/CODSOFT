min_len = 5
max_len = 13

def password_len():
    
    while  True :
        pw_len = input("Enter a number: ")
        if pw_len.isalpha():
            print("Invalid number. Please enter a valid number")
        else:
            if pw_len < min_len:
                print("Password is too short")
            elif pw_len > max_len:
                print("Password too long")
            else:
                print(pw_len)
                break
            
            
    # while True:
    #     pw_len = input('How long would you like your password to be (between 5 and 13): ')
    #     if pw_len.isalpha():
    #         print('Invalid input.')
    #     else:
    #         if pw_len < min_len:
    #             print("Password is too short")
    #         elif pw_len > max_len:
    #             print("Password too long")
    #         else:
    #             print(pw_len)
    #             break
     

password_len()