import random

number = random.randint(1, 100)

low = 1
high = 100

while True:
    mid = (low + high) // 2  
    if number == mid:
        print("Win")
        break
    elif number > mid:
        low = mid + 1
    else:
        high = mid - 1

    if high < low:
        print("Number not found in the range.")
        break
