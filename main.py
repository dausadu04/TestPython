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
    number = {9, 10}

    try:
        user_number = {}
        output_number = {}

        user_number = int(input("Your number: "))

        output_number.update(user_number)
        output_number.update(number)

        for i in output_number:
            print(i)

    except ValueError:
        number = [9, 10]
        for i in number:
            print(i)


# task3()

def task4():
    