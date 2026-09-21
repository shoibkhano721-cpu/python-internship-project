print("===== Interactive Calculator & Unit Converter =====")

while True:
    print("\n1. Arithmetic Calculator")
    print("2. KM to Miles")
    print("3. Celsius to Fahrenheit")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print("Result =", num1 + num2)
            elif operator == "-":
                print("Result =", num1 - num2)
            elif operator == "*":
                print("Result =", num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result =", num1 / num2)
            else:
                print("Invalid operator.")

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "2":
        try:
            km = float(input("Enter distance in kilometres: "))
            miles = km * 0.621371
            print("Miles =", miles)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Fahrenheit =", fahrenheit)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice. Please try again.")