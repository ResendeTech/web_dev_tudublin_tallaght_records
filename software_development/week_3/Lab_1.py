print("="*25, "Exercise 1", "="*25)

a = "1"
b = 2
print(int(a) + b)

print("=" * 62)
print("\n")

print("="*25, "Exercise 2", "="*25)

print("You are part of a group of pirates who found a chest full of gold")

total_gold_coins = int(input("How many gold coins was there? "))
total_pirates = int(input("How many pirates in total are there? "))

gold_for_each_pirate = total_gold_coins // total_pirates
gold_leftover = total_gold_coins % total_pirates

print(f"Total coins: {total_gold_coins}")
print(f"Total number of pirates: {total_pirates}")
print(f"Each pirate gets {gold_for_each_pirate} gold coins")
print(f"Coins left over: {gold_leftover}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 3", "="*25)

num_hours = int(input("Please enter the number of hours: "))
num_mins = int(input("Please enter the number of minutes: "))
num_seconds = int(input("Please enter the number of seconds: "))

hours_to_seconds = num_hours * 60**2
minutes_to_seconds = num_mins * 60
total_seconds = hours_to_seconds + minutes_to_seconds + num_seconds

print(f"Total number of seconds: {total_seconds}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 4", "="*25)

PI = 3.14159
radius = float(input("Please enter the radius: "))
area_of_circle = PI * radius**2

print(f"The area of the circle with radius {radius} is {round(area_of_circle, 3)}")

print("=" * 62)
print("\n")

print("="*25, "Exercise 5", "="*25)

BASE = 60
total_input_seconds = int(input("Please enter the number of seconds: "))
mins_and_seconds = total_input_seconds / BASE
#seconds = (mins_and_seconds - int(mins_and_seconds)) * 60
seconds = total_input_seconds % BASE
hours = mins_and_seconds // BASE
mins = int(mins_and_seconds % BASE)

print(f"Hours: {hours}, Minutes: {mins}, Seconds: {seconds}")

print("=" * 62)
