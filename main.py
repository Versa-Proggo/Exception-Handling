try:
    num1,num2 = eval(input("Enter 2 numbers,seperated by a comma:"))
    result = num1/num2
    print(f"Result is {result}")
except ZeroDivisionError:
    print("Division by 0 == ERROR")
except SyntaxError:
    print("Comma is missing you someone from somewhere, Enter no.seperated by comma like; 1,2 ....")
except:
    print('Invalid input')
else:
    print("No errors")
finally:
    print("This wiil execute no matter what")
valid = False
while  not valid:
    try:
        n = int(input("Enetr a number: "))
        while n % 2 == 0:
            print("Bye")
        
        else:
            print("This is odd")
            valid = True
    except ValueError:
        print("Invalid")