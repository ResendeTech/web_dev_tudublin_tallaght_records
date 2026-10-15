# Class example 2

# TAX = 25.0
# TAX_BRACKET = 100

# hours_worked = int(input("Enter the number of hours worked as an integer: "))
# rate_of_pay = float(input("Enter your pay rate per hour: "))

# gross_pay = hours_worked * rate_of_pay

# if gross_pay > TAX_BRACKET:
#     net_pay = gross_pay - TAX
# else: 
#     net_pay = gross_pay

# print(f"You worked {hours_worked} hours at a rate of €{rate_of_pay} Euro per hour")
# print(f"You earned {gross_pay:.2f} Euro gross pay")
# print(f"You earned {net_pay:.2f} Euro net pay")

# GPA Exercise
# gpa = float(input("Enter your GPA: "))

# num_fails = 0
# num_passes = 0
# num_merits = 0

# if gpa < 2.0:
#     print("You have failed, lol my guy")
#     num_fails += 1
# elif gpa < 2.5:
#     print("You have passed, just barley")
#     num_passes += 1
# else:
#     print("You have received a merit pass")
#     num_merits += 1

# print(f"{'Total fails:':<10} {num_fails}.\nTotal Passes: {num_passes}.\nTotal Merits: {num_merits}.")

#Even or odd exercise

# integer = int(input("Give me a whole number: "))
# result = integer % 2

# if result == 0:
#     print(f"the integer {integer} is an even number")
# else:
#     print(f"The integer {integer} is an odd number")

# email address exercise

email = input("Email address pls: ")
if "@" in email:
    print(f"@ is present in the email '{email}'")
else:
    print(f"@ is not present in the email '{email}'")