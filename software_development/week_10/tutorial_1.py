def ex_1():
    sum_1 = 0
    for i in range (5, 11):
        sum_1 += i
    print(sum_1)

    sum_2 = 0
    for i in range (10, -1, -1):
        sum_2 += i
    print(sum_2)

    sum_3 = 0
    for i in range (20, -1, -1):
        if i % 2 == 0:
            sum += i
        sum_3 += i
    print(sum_3)

def ex_2():
    for n in range (1, 4):
        print(n)

    for n in range(4, 1, -1):
        print(n)
    
    for n in range(4, 1, -2):
        print(n)

def ex_3():
    import random

    secret_number = random.randint(1, 5)

    is_running = True
    while is_running:
        secret_number_user = int(input("Guess a number between 1-5: "))
        if secret_number_user == secret_number:
            print(f"You got it! The number was {secret_number}")
            is_running = False
        elif secret_number_user > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Nope! {secret_number_user} was too low! Try again!")

def ex_4():
    import random

    secret_number = random.randint(1, 5)
    guesses = 0

    is_running = True
    while is_running and guesses < 3:
        if guesses < 3:
            secret_number_user = int(input("Guess a number between 1-5: "))
        
        if secret_number_user == secret_number:
            print(f"You got it! The number was {secret_number}")
            is_running = False
        elif secret_number_user > secret_number:
            guesses += 1
            if guesses < 3:
                print("Too high! Try again.")
                print(f"you have {3 - guesses} guess/es left...")
        else:
            guesses += 1
            if guesses < 3:
                print(f"Nope! {secret_number_user} was too low! Try again!")
                print(f"you have {3 - guesses} guess/es left...")
    print(f"You LOST, since you did not guess the correct number in {guesses} tries :( ")
    
def ex_5():
    lower_limit = 2
    higher_limit = 10

    while True:
        user_value = int(input("Input a number: "))
        if user_value in range(lower_limit, higher_limit):
            break
        if user_value > higher_limit:
            print("Your inputted value is higher than the higher limit of the program. Try again.")
        elif user_value < lower_limit:
            print("Your inputted value is lower than the lower limit of the program. Try again.")
    print(f"Your inputted value ({user_value}) is a valid value between the upper and lower limits.")

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