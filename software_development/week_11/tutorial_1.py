def ex_1():
    n = int(input("Please input an integer: "))
    while True:
        n_power = int(input("Please input an integer that will be the exponent of the previous value (must be >= 0): "))
        if n_power >= 0:
            break
        print(f"The exponent, {n_power}, has to be greater or equal to 0. Please try again.")
    
    if n_power == 0:
        n = 1
        print(f"Calculating: {n} to the power of {n_power}")
        print(f"Step 1: ans = {n}")
    else:
        multiplier = n
        i = 1
        print(f"Calculating: {n} to the power of {n_power}")
        print(f"Step {i}: ans = {n}")
        for i in range(1, n_power):
            n *= multiplier
            print(f"Step {i}: ans = {n}")
        print(f"Final answer: {n}")

def ex_2():
    factorial_n = int(input("Input a positive integer: "))
    total = 1
    for i in range(1, factorial_n + 1):
        total *= i
    print(f"{factorial_n}! = {total}")

def ex_3():
    GRAVITATIONAL_ACCELARATION = 9.80665

    t = int(input("Enter limit value: "))

    print("Seconds\t\tDistance\n-------\t\t--------\n")
    for i in range(t + 1):
        distance = (1/2) * GRAVITATIONAL_ACCELARATION * i ** 2
        print(f"{i}\t\t{distance:.4f}\n")

def ex_4():
    sentence = input("Enter sentence: ")
    reversed = ""
    for character in range(len(sentence) - 1, -1, -1):
        reversed += sentence[character]
    print(reversed)

    if sentence.lower() == reversed.lower():
        print("The sentence is a palindrome!")
    else:
        print("The sentence is not a palindrome...")


exercises = {
    1: ex_1,
    2: ex_2,
    3: ex_3,
    4: ex_4,
    # 5: ex_5,
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