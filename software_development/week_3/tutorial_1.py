print("="*25, "Exercise 1", "="*25)

#If the integer variables a, b and c contain 11,55 and 2 respectively what happens
# when the following three assignment statements are executed? Assume that they
# are executed with the initial values specified above.
A = 11
B = 55 
C = 2

a = A + B - C
print(f"a: {a}")
c = C % 3
print(f"First c: {c}")
c = (A + 22) % 2
print(f"Second c: {c}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 2", "="*25)

# 2. What is the numeric value of each of the following expressions as evaluated by python

exercises = {
    "ex_1": 4 + 6 * 3,
    "ex_2": 6 / 3 * 7,
    "ex_3": 18 / 2 + 14 / 2,
    "ex_4": 16 / 2,
    "ex_5": 17 / 2,
    "ex_6": 28 // 5,
    "ex_7": 16 % 2,
    "ex_8": 17 % 2,
    "ex_9": 28 % 5,
    "ex_10": 28 % 5 * 3 + 1,
    "ex_11": (2 + 3) * 4,
    "ex_12": 20 / (4 + 1)
}

for exercise, answer in exercises.items():
    print(f"the answer for {exercise} in python is {answer}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 3", "="*25)

#What happens when each of the three statements is executed? The variables a,b
#and c contain 23 3 and 1 respectively.

a1 = 23
b1 = 3
c1 = 1

a1 += b1
c1 *= c
b1 %= 3

print(f"a equals to {a1}, b equals to {b1} and c equals to {c1}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 4", "="*25)

# Write the Python code to calculate your age in seconds, the user should enter their
# age in years, a whole number

age_years = int(input("What is yo age? "))

age_in_seconds = age_years * 365 * 24 * 60**2
print("-"*40)
print(f"Your age in years: {age_years}")
print(f"Your age in years: {age_in_seconds}")
print("-"*40)

print("=" * 62)
print("\n")

print("="*25, "Exercise 5", "="*25)

# Suppose the retail cost of a book is €24.95, but book shops get a 40% discount on
# the retail cost. Shops pay a shipping cost of €2 per copy. Write the Python code to
# determine and print the shop cost for a number of copies entered by the user, print
# the shipping cost and the total cost of the books for the shop.

BOOK_SHOP_DISCOUNT = 0.4
BOOK_COST = 24.95
SHIPPING_COST = 2

quantity_of_books = int(input("Please enter the number of copies required: "))

cost_of_books = BOOK_COST * (1 - BOOK_SHOP_DISCOUNT) * quantity_of_books
cost_of_shipping = quantity_of_books * SHIPPING_COST
total_cost = cost_of_books + cost_of_shipping

print("Book Shop System")
print(f"Cost of the books: {cost_of_books}")
print(f"Cost of shipping: {cost_of_shipping}")
print(f"Overall cost: {total_cost}")

print("=" * 62)
