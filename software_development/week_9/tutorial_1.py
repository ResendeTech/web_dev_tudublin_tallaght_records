def ex_1():
    print(
        """ # 1. Loop controlled variable, so Intialisation of LCV
            # 2. Condition of execution i.e. guard
            # 3. Body of the loop
            # 4. Make progress""")

def ex_2():
    # Exercise A
    count = 1
    sum = 0
    while count <= 100:
        sum += count
        count += 1
        print(sum)
    # Exercise B
    count = 5
    sum = 0
    while count <= 50:
        sum += count
        count += 5
        print(sum)

    # Exercise C
    count = 1
    sum = 0
    while count <= 19:
        sum += count
        count += 2
        print(sum)
    
    # Exercise D
    count = 1
    sum = 1
    while count <= 10:
        sum *= count
        count += 1
        print(sum)

    # Exercise E
    count = 2
    sum = 1
    while count <= 20:
        sum *= count
        count += 2
        print(sum)

def ex_3():
    count = 0
    while count < 5:
        count -= 1
    print(f"Count after loop {count}")

def ex_4():
    number = int(input("Input a number greater than 0: "))
    while number < 0:
        number = int(input("Input a number greater than 0: "))

    while number >= 1:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
        number -= 1
    print("Program is done!")
        


    
        

    
        




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