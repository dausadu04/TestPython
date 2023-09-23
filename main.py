def task1():
    number = [4, 8, 15, 16, 23, 42]

    for i in number:
        print(i, end=" ")


# task1()

def task2():
    number = [4, 8, 15, 16, 23, 42]

    for i in number:
        print(i, " ")


# task2()

def task3():
    default_numbers = {9, 10}

    try:
        user_input = int(input("Enter your number: "))
        output_numbers = {user_input} | default_numbers

        for number in output_numbers:
            print(number)

    except ValueError:
        for number in default_numbers:
            print(number)


# task3()

def task4():
    try:
        first_number = int(input("first number: "))
        second_number = int(input("second number: "))
        third_number = int(input("third number: "))

        numbers = {first_number, second_number, third_number}

        total_numbers = first_number + second_number + third_number

        for i in numbers:
            print(i)

        print(total_numbers)
    except TypeError:
        print("Please, write down only numbers, not other")


# task4()


def task5():
    try:
        user_input = int(input(""))

        total = (user_input ** 3)

        total_surface_area = 6 * (user_input ** 2)

        print("Volume = ", total)
        print("Total surface area", total_surface_area)

    except TypeError:
        print("Please, write down only numbers, not other")


# task5()


def task2_1():
    try:
        student = int(input("student: "))
        mandarin = int(input("mandarin: "))

        basket = mandarin % student

        total = mandarin // student

        print(total)
        print(basket)

    except TypeError:
        print("Please, write down only numbers, not other")


# task2_1()

def task2_2():
    try:
        user_input = int(input("Your number: "))
        number = 999

        if user_input > number:
            str_user_input = str(user_input)
            print("The digit in the thousands position is ", str_user_input[0])
            print("The number in the hundreds position is ", str_user_input[1])
            print("The digit in the tens position is ", str_user_input[2])
            print("The digit in the position of units  ", str_user_input[3])
        else:
            print("Your digit is not a four-digit number")

    except TypeError:
        print("Please, write down only numbers, not other")


# task2_2()


def task2_3():
    try:
        people = int(input("People: "))

        float_num = people % 2

        if float_num > 0:
            people += 1
            print(people)
    except TypeError:
        print("Please, write down only numbers, not other")


# task2_3()


def task2_4():
    try:
        user_input = int(input("Your input: "))

        if user_input == 0:
            print("Your number is zero")
        else:
            print("The result of << is", user_input + 1)

    except TypeError:
        print("Please, write down only numbers, not other")


# task2_4()

def task2_5():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
        else:
            print("Error: Invalid operation")

        if operation in ('+', '-', '*', '/') and num2 != 0:
            print(f"{num1} {operation} {num2} = {result:.3f}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as dauletsuper:
        print(f"An error occurred: {dauletsuper}")

# task2_5()