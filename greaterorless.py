
    
num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))
num3 = int(input("What is your third number: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f"{num1} is the greatest, {num2} is the second greatest, {num3} is the least")
    else:
        print(f"{num1} is the greatest, {num3} is the second greatest, {num2} is the least")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"{num2} is the greatest, {num1} is the second greatest, {num3} is the least")
    else:
        print(f"{num2} is the greatest, {num3} is the second greatest, {num1} is the least")
else:
    if num1 >= num2:
        print(f"{num3} is the greatest, {num1} is the second greatest, {num2} is the least")
    else:
        print(f"{num3} is the greatest, {num2} is the second greatest, {num1} is the least")

num1=input("What is your first number: ")
num2=input("What is your second number: ")
if num1>num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
    