import numpy as np

def calculator():
    while True:
        print("Advanced Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square root")
        print("7. Exit")

        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice == '7':
            break

        num1 = np.float64(input("Enter first number: "))

        if choice != '6':
            num2 = np.float64(input("Enter second number: "))

        if choice == '1':
            result = np.add(num1, num2)
            print("Result: ", result)

        elif choice == '2':
            result = np.subtract(num1, num2)
            print("Result: ", result)

        elif choice == '3':
            result = np.multiply(num1, num2)
            print("Result: ", result)

        elif choice == '4':
            if num2 != 0:
                result = np.divide(num1, num2)
                print("Result: ", result)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == '5':
            result = np.power(num1, num2)
            print("Result: ", result)

        elif choice == '6':
            if num1 >= 0:
                result = np.sqrt(num1)
                print("Result: ", result)
            else:
                print("Error! Square root of negative number is not allowed.")

        else:
            print("Invalid input")

calculator()
