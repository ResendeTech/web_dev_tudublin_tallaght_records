#exercise_choice = int(input("Which exercise do you want to choose? "))


# if exercise_choice in range(7):
#     if exercise_choice == 1:
    
#     elif exercise_choice == 2:

#     elif exercise_choice == 3:

#     elif exercise_choice == 4:

#     elif exercise_choice == 5:
    
#     elif exercise_choice == 6:

#     elif exercise_choice == 7:




def ex_1():
    print("="*25, "Exercise 1", "="*25)

    user_input1 = input("Enter one word please:")
    user_input2 = input("Enter another word please:")
    user_input3 = input("Enter the third word please:")
    user_inputs = [user_input1, user_input2, user_input3]
    acronym = ""
    for user_input in user_inputs:
        f_letter = user_input[0]
        acronym += f_letter

    print(acronym.upper())
    
    print("=" * 62)

def ex_2():
    print("="*25, "Exercise 2", "="*25)

    password = input("please enter a password: ")
    print(len(password))
    print("Does this password contain the character '!'?", end=" ")
    print("!" in password)

    print("=" * 62)

def ex_3():
    print("="*25, "Exercise 3", "="*25)

    user_input = input("Enter a word that is longer than 4 characters: ")
    if len(user_input) >= 4:
        first_2_char = user_input[:2]
        last_2_char = user_input[-2:]
        word_mix = first_2_char + last_2_char
        print(f"user's input: {user_input}")
        print(f"first 2: {first_2_char} and last 2: {last_2_char}")
        print(f"concatenated word: {word_mix}")
    else: 
        print("The word is less than 4 characters. try again.")

    print("=" * 62)

def ex_4():
    print("="*25, "Exercise 4", "="*25)

    user_input = input("give me sentence: ")
    user_char = input("Enter a single character to search for in that sentence: ")

    print("Does the sentence contain that character?", user_char in user_input)
    print(user_input.index(user_char))
    censored_sentence = user_input.replace(user_char, "*"*len(user_char))
    print(f"censored sentence is: {censored_sentence}")
            
    print("=" * 62)

def ex_5():
    print("="*25, "Exercise 5", "="*25)

    sentence_user = input("Input a sentence: ")
    start_position = float(input("start position of splice: "))
    end_position = float(input("end position of splice: "))
    step_value = float(input("step value of splice: "))

    print(sentence_user[start_position:end_position:step_value])
    print(sentence_user[::-1])
    print(len(sentence_user))
    print(sentence_user.upper())

    print("=" * 62)

def ex_6():
    print("="*25, "Exercise 6", "="*25)

    user_number = float(input("Input an a number: "))
    print(f"Your number to the second power: {user_number ** 2} and to the 3rd power: {user_number ** 3}")

    print("=" * 62)

def ex_7():
    print("="*25, "Exercise 7", "="*25)

    celcius_temp = float(input("please input a temperature in Celcius: "))
    celcius_to_farenheit = (celcius_temp * 9/5) + 32
    print(f"{celcius_temp} degrees celcius is equal to {celcius_to_farenheit} degrees farenheit")

    print("=" * 62)


exercises = {
    1: ex_1,
    2: ex_2,
    3: ex_3,
    4: ex_4,
    5: ex_5,
    6: ex_6,
    7: ex_7
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


