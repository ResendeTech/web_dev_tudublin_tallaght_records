# Slide 12 and 14
# age = int(input("Enter you age: "))
# if age >= 17:
#     print("You are eligible to apply for a driving license")
# else:
#     print("You are not eligible to apply for a driving license")

# slide 16
# age = int(input("Enter you age: "))
# if age > 17:
#     print("You are eligible to apply for a driving license")
# elif age == 17:
#     print("You are just eligible for a driving license")
# else:
#     print("You are not eligible to apply for a driving license")

#Slide 25
hours = int(input("Enter the number of hours worked as an integer: "))
rate = float(input("What is the hourly rate? "))

pay = hours * rate

if hours > 40:
    pay = pay + (hours - 40) * (rate * 0.5)

# Using f strings
print(f"You worked {hours} hours at a rate of {rate:.2f} euro per hour")
print(f"You earned {pay:.2f} Euros")

# Using round()
print(f"You worked {hours} hours at a rate of {round(rate, 2)} euro per hour")
print(f"You earned {round(pay, 2)} Euros")