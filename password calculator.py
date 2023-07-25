def login():
    default_password = "skooliskool"
    default_username = "prithvi"
    attempts = 0

    while attempts < 5:
        username_input = input("What is your username (or type 'forgot' if you forgot your username'): ")
        user_input = input("What is the password (or type 'forgot' if you forgot your password): ")

        if username_input == "forgot":
            new_username = input("What is the new username: ")
            default_username = new_username
            print("Username updated successfully!")
            continue

        if user_input == "forgot":
            new_password = input("What is the new password: ")
            default_password = new_password
            print("Password updated successfully!")
            continue

        if default_username == username_input and default_password == user_input:
            print("Correct username and password")
            return True

        print("Wrong username or password")
        attempts += 1

    print("Too many attempts")
    return False

if login():
    print("Welcome to the calculator")

    while True:
        try:
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        operation = input("What operation do you want (*, /, +, -) (or type 'end' to finish): ").lower()

        if operation == "end":
            break

        if operation in ("*", "/", "+", "-"):
            if operation == "*":
                answer = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Can't divide by 0")
                    continue
                else:
                    answer = num1 / num2
            elif operation == "-":
                answer = num1 - num2
            elif operation == "+":
                answer = num1 + num2
            print("The answer is:", answer)
        else:
            print("Invalid operation")
