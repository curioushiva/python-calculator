print("<==== Simple python calculator ====>")

while True:
    print("\n1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Divison")
    print("5. Modulus")
    print("6. Exit")

    operation = input("\nEnter your choice: ")

    if operation == "6":
        print("Calculator is closed.")
        break

    if operation not in ("1", "2", "3", "4", "5"):
        print("\nInvalid choice. Try again.")
        continue

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "1":
        print(f"Result is: {num1 + num2}")

    elif operation == "2":
        print(f"Result is: {num1 - num2}")

    elif operation == "3":
        print(f"Result is: {num1 * num2}")

    elif operation == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result is: {num1 / num2}")

    elif operation == "5":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result is: {num1 % num2}")
