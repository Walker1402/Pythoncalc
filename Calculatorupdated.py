while True:
    # InputEngine
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))

    # OperatorsEngine
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y

    # UserInputForOperation(UIFO)
    operation = input("What operation would you like to do? ")

    if operation == 'add':
        print(add)
    elif operation == 'subtract':
        print(subtract)
    elif operation == 'multiply':
        print(multiply)
    elif operation == 'divide':
        print(divide)
    else:
        print("Invalid operation")

    repeat = input("Do you want to continue? (yes/no) ")
    
    if repeat.lower() != 'yes':
        break
