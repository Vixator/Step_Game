import random

range(1,100)
number=random.randint(range)

low=1
high=100
mid=(low+high)/2
while True:
    if number==mid:
        print("Win")
    elif number>mid:
        low==mid+1
        high==100
        mid==(low+high)/2
    else:
        low==1
        high==mid-1
        mid==(low+high)/2
    if high==1:
        break

