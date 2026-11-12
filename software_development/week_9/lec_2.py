# import math

# radius = float(input("Enter radius of circle (r > 0): "))

# while radius <= 0:
#     radius = float(input("Re-enter radius (previous value was <= 0, r must be greater than 0): "))

# area = math.pi * (radius ** 2)
# area = round(area, 4)
# print(f"The area is: {area}")

#Slide 6
# mark = float(input("Enter the student mark, range 0...100: "))

# while mark < 0 or mark > 100:
#     mark = float(input("Re-enter the student mark, range 0...100: "))

# print(f"Your mark is: {mark}")

# Write the code that will only accept a value greater than 0 but less than 130 for a person’s age.
# If an input value is invalid, then the code will repeat until the valid input is read.
# Slide 8

# age = int(input("Enter your age, between 1 and 129: "))

# while age <= 0 or age >+ 130:
#     print("Re input the age that is between 1 and 129: ")

# print(f"Yo age is: {age}") 

#Slide 14

# total = 0
# counter = 1
# input_number = int(input("Enter first number or 0 to exit: "))

# while input_number != 0:
#     total += input_number
#     counter += 1
#     input_number = int(input(f"Enter the next number (number {counter}) or 0 to exit: "))
# print(f"The total is: {total}")

#Slide 15
import random

secret_number = random.randint(1, 10)

is_running = True
while is_running:
    secret_number_user = int(input("Guess a number between 1-10: "))
    if secret_number_user == secret_number:
        print(f"You got it! The number was {secret_number}")
        is_running = False
    elif secret_number_user > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Nope! {secret_number_user} was too low! Try again!")
