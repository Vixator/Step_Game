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
