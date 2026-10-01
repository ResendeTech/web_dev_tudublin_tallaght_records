# Slide 7
# print("Please enter your name:", end="")
# name = input()
# print("Hello", name)

#Slide 8
# name = input("Please enter your name: \n")
# print("Hello", name)

# Slide 9
# age = input("please enter your age: ")
# age = int(input("please enter your age: "))
# age = int(age)
# print(f"You are {age} years old")

#Slide 10
# print("\t\tFinal Cost Program\n")

# price=float(input("Enter initial cost of product: "))
# tax=float(input("Enter tax rate for product: %"))

# tax_amount=price*(tax/100)
# final_cost=price+tax_amount

# print("")
# print("Cost before tax:€",price)
# print("Final Cost with tax: €",final_cost)
# print("Tax amount paid:€",round(tax_amount,2))

#Slide 11

print("\t\tBirthday Countdown")

name = input("Please enter your name: ")
age = int(input("Give me your age plss: "))
years_ahead = int(input("How many years do you wanna look ahead, mate? "))

future_age = age + years_ahead
years_in_months = years_ahead * 12

print(f"\nHello, {name}.\nIn {years_ahead} years, you will be {future_age} years old.\n{years_ahead} years is {years_in_months} months, so use it wisely.")

