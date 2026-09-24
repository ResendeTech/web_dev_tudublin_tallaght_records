a = 5
b = 6
c = 7
length = [a, b, c]

avg = (a + b + c) / len(length)

print("="*25, "Exercise 1", "="*25)

print("The average of a, b and c is:", avg)
print("The average of a, b and c is: " + str(avg))
print("the average of a, b and c is: {0}".format(avg))

print("=" * 62)
print("\n")

print("="*25, "Exercise 2", "="*25)
CALORIES_PER_POUND = 19
weight_pounds = 750

needed_calories_daily = CALORIES_PER_POUND * weight_pounds

print("This person weighs", weight_pounds, "and needs", needed_calories_daily, "calories daily")
print("This person weighs " + str(weight_pounds) + " and needs " + str(needed_calories_daily) + " calories daily")
print("This person weighs {0} and needs {1} calories daily".format(weight_pounds, needed_calories_daily))

print("=" * 62)
print("\n")

print("="*25, "Exercise 3", "="*25)

EARTH_YEAR = 365
AGE = 18
mercury_year = 88
venus_year = 225
jupiter_year = 4380
saturn_year = 10767
planet_years = [mercury_year, venus_year, jupiter_year, saturn_year]
planets = ["Mercury", "Venus", "Jupiter", "Saturn"]
i = 0

for planet_year in planet_years:
    planet_age = (AGE * EARTH_YEAR) / planet_year
    print(f"This {AGE} year old person is {round(planet_age, 3)} years old in {planets[i]}")
    i += 1

print("=" * 62)




