correct_password = "12345"

#To set the maximum number of attempts
max_attempts = 5
attempts_left = max_attempts

#Start the password entry process
while attempts_left > 0:
    user_password = input(f"Enter the password (Attempts left: {attempts_left}): ")
    
    #To check if the entered password is correct or incorrect
    if user_password == correct_password:
        print("Correct Password! Access granted.")
        break
    else:
        #If incorrect password entered, The number of attempts will be reduced
        attempts_left -= 1
        
        #To inform the user about remaining attempts
        if attempts_left > 0:
            print(f"Incorrect password. You have {attempts_left} attempts remaining.")
        else:
            print("Incorrect password. You are out of attempts. Authorities have been alerted.")
            break
