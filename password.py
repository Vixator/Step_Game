defaultpassword = "skooliskool"
attempts = 5

while True:
    userinput = input("What is the password (or type 'forgot' if you forgot your password): ")
    
    if userinput == "forgot":
        newpassword = input("What is the new password: ")
        defaultpassword = newpassword
        print("Password updated successfully!")

    if userinput != defaultpassword:
        print("Wrong password")
        attempts -= 1
        print(f"You have {attempts} attempts left")
        
        if attempts == 0:
            print("Too many attempts, Try again later")
            break
    else:
        print("Correct password")
        break
