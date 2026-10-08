# slide 3 
# This gives the first character of the string
my_string = "Monty python"
print(my_string[0])

# slide 4
# this starts at the end character of the string
my_string = "Monty python"
print(my_string[-1])

# slide 5 and 6
# This is the same way to get the end character but through an expression
my_string = "Monty python"
print(my_string[len(my_string) - 1])

# slide 7 and 8
# This is called string slicing, as we are choosing the characters we are choosing to print from the string
my_string = "Monty python"
print(my_string[6:10])

# slide 9
print(my_string[:5]) # prints all the charaters until the 5th index
print(my_string[5:]) # prints all the characters from the 5th index
print(my_string[:]) # Just prints the whole string, same thing as just without the brackets

# slide 10
my_string = "Monty python"
print(my_string[1:5:2]) # Basically, the first value indicates the start where the slicing will begin, the 2nd value indicates the end of the slicing, while the third value indicates a specific step to move by each time (so basically, if it is set to 2, then it starts with o, then goes to t, then blank space and then the slice runs out)

# slide 11
my_name = "joe bloggs"
my_name[0] = "J" # This does not work as you cannot change a string, because it is immutable, meaning they cannot be changed in place after they are created.

# Slide 12
# Although I believe this method works quite fine for replacing string characters. But this is just creating a new string and sending the old one to GC (garbage collection and deleting it)
my_name = "joe bloggs"
my_name = my_name.replace("j", "J")
print(f"MY name is: {my_name}")

# Slide 13
my_name = "Joe Bloggs"
print(" " in my_name) # in this case, the in operator is used to check for characters in the string, which will return either true or false.

# Slide 14 and 15
my_name = "JoeBloggs"
print(" " in my_name) # This one prints false
print("oe" in my_name) # This one prints true
print("Oe" in my_name) # This one prints false
print("og" in my_name) # This one also prints true

# Slide 16
my_name = "Joe Bloggs"
location = my_name.index(" ")
print(f"Location of space in my_name: {location}")

# Slide 18
my_name = "Joe Bloggs"
loc = my_name.index("Bloggs")
print(f"Location of substring: {loc}")

# Classwork
full_name = input("Please input your full name: ")
space_location = full_name.index(" ")
f_name = full_name[:space_location]
s_name = full_name[space_location:]
# f_name.capitalize()
# s_name.strip("")
print(f"Your first name is: {f_name.capitalize()} and your surname name is: {s_name.strip()}")