def ex_1():
    number = 50
    total = 0
    total_1 = 0
    
    while number <= 100:
        total += number
        number += 1
    print(total)

    for n in range(50, 101):
        total_1 += n
    print(total_1)

def ex_2():

    sum = 0
    for n in range(1, 6):
        float_n = float(input(f"Input float number {n}: "))
        sum += float_n
    avg = sum / n
    print(f"The average of the numbers is: {avg}")

def ex_3():
    even_sum = 0
    odd_sum = 0
    for n in range(1, 21):
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    print(f"Odd sum: {odd_sum}\nEven sum: {even_sum}")

def ex_4():
    EURO_TO_JAPANESE = 165
    while True:
        euros = int(input("Please enter a euro amount (enter 0 to exit the program): "))
        if euros == 0:
            break
        japanese_yen = euros * EURO_TO_JAPANESE
        print(f"The yen value for {euros:.1f} euros is {japanese_yen:.1f} yen.")
    print("Thank you for using the currency converter program")

def ex_5():
    start_n = int(input("Please input a starting number: "))
    end_n = int(input("Please input an ending number: "))
    step = int(input("Please input the step value: "))
    total = 0
    for n in range(start_n, end_n + step, step):
        total += n
        print(n)
    print(f"The total of the numbers from {start_n} to {end_n} in steps of {step} is: {total}")



exercises = {
    1: ex_1,
    2: ex_2,
    3: ex_3,
    4: ex_4,
    5: ex_5,
    # 6: ex_6,
    # 7: ex_7,
    # 8: ex_8,
    # 9: ex_9,
    # 10: ex_10
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
