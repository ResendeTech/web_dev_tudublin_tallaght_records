def ex_1():
    length = float(input("Enter length of rectangle that is greater than 0: "))
    width = float(input("Enter width of rectangle that is greater than 0: "))

    while length <= 0:
        length = float(input("Error, length is 0 or less. Enter length of rectangle that is greater than 0: "))
    while width <= 0:
        width = float(input("Error, width is 0 or less. Enter width of rectangle that is greater than 0: "))

    area = width * length
    print(f"Area of rectangle of width {width} and length {length}: {area}")

def ex_2():
    custo_present = input("Are there any customers for the screening? [yes/no] ").lower()

    count = 1
    total = 0
    while custo_present == "yes":
        custo_age = int(input(f"How old is customer {count}? "))

        if custo_age < 18:
            ticket_price = 2.5
            total += ticket_price
        else:
            ticket_price = 5.5
            total += ticket_price

        print(f"For customer {count}, age {custo_age}, the ticket price is: {ticket_price:.2f} euros.")
        count += 1
        custo_present = input("Are there any more customers for the screening? [yes/no] ").lower()

    if total == 0:
        print(f"No customers were present for the screening, since total taking is: {total:.2f} euros.")
    else:
        print(f"Total takings: {total:.2f} euros")

def ex_3():
    int_1 = int(input("Enter integer 1: "))
    int_2 = int(input("Enter integer 2: "))
    int_3 = int(input("Enter integer 3: "))

    while int_1 == int_2 or int_1 == int_3 or int_2 == int_1 or int_2 == int_3 or int_3 == int_1 or int_3 == int_2:
        print("Number must be unique. Please try to enter again.")
        int_1 = int(input("Enter integer 1: "))
        int_2 = int(input("Enter integer 2: "))
        int_3 = int(input("Enter integer 3: "))

    if int_1 > int_2 and int_1 > int_3:
        print(f"The largest number is the first integer: {int_1}")
    elif int_2 > int_1 and int_2 > int_3:
        print(f"The largest number is the second integer: {int_2}")
    else:
        print(f"The largest number is the third integer: {int_3}")
    



exercises = {
    1: ex_1,
    2: ex_2,
    3: ex_3,
}

while True:

    exercise_choice = int(input("Which exercise do you want to choose? If you want every exercise, type '100':  "))

    if int(exercise_choice) in exercises:
        exercises[exercise_choice]()
    elif exercise_choice == 100:
            for exercise in exercises.values():
                exercise()
    else:
        print("Invalid number. Please input another number")