
# string1 = "hello"
# answer=string1*3
# print(answer)

# string1 = "hello"
# string2 = (string1 + " ")* 2 + string1
# print(string2)

# print("----...more...----")
# print("-"*90)

# string3 = "hello"
# length = len(string3)
# print(length)

# slide 16: FINALLY f-STRINGSS, better than I ever knewwww

# ":" allows for the f string to give an expression to the variable. 
price = 123.987
print(f"price: {price:.2f}") # f stands for floating point number, so it rounds it basically to that floating point number

huge_number = 123588750197102983
print(f"{huge_number:,}") # "," basically adds a comma for ever 3rd digit 

progress = 0.756
print(f"Progress: {progress:.1%}") # .1 gives the decimal place (in this case, 1 decimal place), same as the previous one. While the percentage multiplies the number by 100 and adds a percentage to it

# allows for customisation of location for the text in the terminal

name = "john"
print(f"{name:>10}") # right align
print(f"{name:<10}") # left align
print(f"{name:^10}") # centre align

# you can also combine multiple types of expressions into one, for example:
product = "Laptop"
price = 1599.99
print(f"{product:<10} | {price:,.2} euros") # so the , adds the comma every 3rd digit, the .2 selects the total amount of decimal places that is shown. finally, f makes the number into a floating point number, otherwise it is printed in scientific notation.