def code():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("A person's age can't be a word or decimal. Please enter a whole number.")
    else:
        if age % 2 == 0:
            print(f"Your age: {age} is even")
        else:
            print(f"Your age: {age} is odd")
code()