option = int(input("Choose an operation (1: Add, 2: Subtract, 3: multiply, 4 : Divide): "))
result = None 

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 =int(input("Enter second number: "))

    if option == 1:
        result = num1 + num2 
    elif option == 2:
        result = num1 - num2 
    elif option == 3:
        result = num1 * num2 
    elif option == 4:
        if num2 != 0:
           result = num1 // num2
        else:
            print("Error: Cannot divide by zero.")
else:
    print("Invalid operation entered")

if result is not None:
    print("The result of the operation is{}".format(result))
