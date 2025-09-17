try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
