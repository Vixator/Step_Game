defaultpassword = "skooliskool"
defaultusername = "prithvi"
attempts = 0
userattempts = 0
check = False

while True:
    usernameinput = input("What is your username (or type 'forgot' if you forgot your username'): ")
    userinput = input("What is the password (or type 'forgot' if you forgot your password): ")

    if usernameinput == "forgot":
        newusername = input("What is the new username: ")
        defaultusername = newusername
        print("Username updated successfully!")
        continue

    if userinput == "forgot":
        newpassword = input("What is the new password: ")
        defaultpassword = newpassword
        print("Password updated successfully!")
        continue

    if defaultusername == usernameinput and defaultpassword == userinput:
        print("Correct username and password")
        check = True
        break

    print("Wrong username or password")
    userattempts += 1

    if userattempts == 5:
        print("Too many attempts")
        break

if check:
    print("Welcome to the calculator")
    while True:
        try:
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        odo = input("What operation do you want (*, /, +, -) (or type 'end' to finish): ").lower()

        if odo == "end":
            break

        if odo == "*":
            answer = num1 * num2
        elif odo == "/":
            if num2 == 0:
                print("Can't divide by 0")
                continue
            else:
                answer = num1 / num2
        elif odo == "-":
            answer = num1 - num2
        elif odo == "+":
            answer = num1 + num2
        else:
            print("Invalid operation")
            continue

        print("The answer is:", answer)
        break
