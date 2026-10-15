def ex_1():
    surname = input("Please enter your surname").title()

    if surname == "Andrade Resende":
        print("Surname entered correctly")
    else: 
        print("Error, surname entered incorrectly.")

def ex_2():
    mark = int(input("Please enter the mark you have: "))

    grades = {
        range(0, 34): "F",
        range(35, 39): "D",
        range(45, 49): "C2",
        range(50, 54): "C1",
        range(55, 59): "B3",
        range(60, 64): "B2",
        range(65, 69): "B1",
        range(70, 74): "A3",
        range(75, 79): "A2",
        range(80, 100): "A1"
    }

    for grade_range, grade in grades.items():
        if mark in grade_range:
            print(f"For {mark} points, your grade is: {grade}")
        elif mark not in grade_range:
            continue
        else:
            print("Your mark is not in the range of 0-100 points")

def ex_3():
    table_costs = [225, 100, 310]
    table_names = ["Oak", "Pine", "Mahogany"]
    table_code = int(input("Enter the code for a table (1-3): "))

    if table_code <= 3:
        print(f"The {table_names[table_code - 1]} tables costs {table_costs[table_code - 1]} euros")
        quanity = int(input("\nHow many tables do you want? "))
        total_cost = table_costs[table_code - 1] * quanity
        print(f"{quanity} of {table_names[table_code - 1]} tables will cost a total of {total_cost:,} euros")
    else:
        print("Invalid table code has been entered. Will not ask for quantity required or give a total cost of the table/s.")    
        



exercises = {
    1: ex_1,
    2: ex_2,
    3: ex_3,
}

while True:

    exercise_choice = int(input("Which exercise do you want to choose? If you want every exercise, type '9':  "))

    if exercise_choice in exercises:
        exercises[exercise_choice]()
    elif exercise_choice == 9:
            for exercise in exercises.values():
                exercise()
    else:
        print("Invalid number. Please input another number")

