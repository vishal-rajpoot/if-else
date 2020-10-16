age=int(input("what is your age: "))
if age>18 and age<100:
    print("you can drive")
elif age==18:
    print("we can't decide, you can come to our office then we check your mental health ")
elif age<18 and age>7:
    print("you can't drive")
else:
    print("please enter a valid age")