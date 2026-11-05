# Slide 3 Fermat's theorem tested in code bruv 

# a = int(input("Please enter the integer for value a: "))
# b = int(input("Please enter the integer for value b: "))
# c = int(input("Please enter the integer for value c: "))
# n = int(input("Please enter the integer for value n: "))

# testing_answer = (a ** n) + (b ** n)
# actual_answer = c ** n

# if n > 2:
#     if testing_answer == actual_answer:
#         print(f"testing answer equals to: {testing_answer}")
#         print(f"Actual answer is: {actual_answer}")
#         print("Fermat's theorem does not hold true")
#     else:
#         print(f"testing answer equals to: {testing_answer}")
#         print(f"Actual answer is: {actual_answer}")
#         print("Fermat's theorem does hold true")
# else:
#     print("The exponent n must be greater than 2 for this formula")

# I dont get this bs, move on lil bro

# Slide 4
# import time
# # strftime im guessing means string format time
# print(time.strftime("%Y:%m:%d:%H:%M:%S")) # % means what format you want based on the logic implemented
# print(time.strftime("%D")) # D also give the date, with the month and the year.
# print(time.strftime("%y:%m:%d")) # this is another way to do it.
# print(time.strftime("%I")) # this is for a 12 hour clock

# hours = print(time.strftime("%H"))
# minutes = print(time.strftime("%M"))
# seconds = print(time.strftime("%S"))
# print(hours)
# print(minutes)
# print(seconds)

# Slide 6
# import time

# birth_month = int(input("Enter the month of your birth: "))
# current_month = int(time.strftime("%m"))

# if current_month > birth_month:
#     months_to_birthday = birth_month + (12 - current_month)
# elif current_month == birth_month:
#     months_to_birthday = 0
# else:
#     months_to_birthday = birth_month - current_month

# print(f"Your birthday is {months_to_birthday} months away")

# Slide 9
stick_a = float(input("Enter the size of stick a: "))
stick_b = float(input("Enter the size of stick b: "))
stick_c = float(input("Enter the size of stick c: "))

if stick_a > stick_b and stick_a > stick_c: 
    hypotenuse = stick_a
    side_1 = stick_b
    side_2 = stick_c

elif stick_b > stick_a and stick_b > stick_c:
    hypotenuse = stick_b
    side_1 = stick_a
    side_2 = stick_c

else:
    hypotenuse = stick_c
    side_1 = stick_b
    side_2 = stick_a

if (side_1 ** 2 + side_2 ** 2) == hypotenuse ** 2:
    print("You can make a right angle triangle with your sticks!")
else:
    print("Womp womp, you cant make a right angle triangle with these horrible numbers :( ")


