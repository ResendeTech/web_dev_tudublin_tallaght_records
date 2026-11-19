# Slide 4 
# sentence = "!!Python"
# sentence = sentence.strip("!")
# print(sentence)

# sentence = "Pyth!on"
# index_to_edit = sentence.index("!")
# new_string = sentence[:index_to_edit] + sentence[index_to_edit + 1:]
# print(new_string)

#Slide 6
# sentence = input("Enter sentence: ")
# print(len(sentence))
# sentence = sentence.strip()
# print(len(sentence))
# space_count = 0
# counter = 0 # Loop controlled variable - LCV

# while counter < len(sentence):
#     if sentence[counter] == " ":
#         space_count += 1
#     # elif sentence[counter:counter + 1] == "  ":
#     #     sentence[counter:counter + 1].strip()
#     #     space_count += 1
#     counter += 1

# words = space_count + 1
# print(f"space_count is {space_count} and word count is {words}")

# Slide 8
# sentence = input("Enter sentence: ")
# print(len(sentence))
# sentence = sentence.strip()
# print(len(sentence))
# space_count = 0

# for character in sentence:
#     if character == " ":
#         space_count += 1
#     # if character == " " and sentence[character + 1] == " ":
#     #     sentence[character + 1] = ""
#     #     space_count += 1
# words = space_count + 1
# print(f"space_count is {space_count} and word count is {words}")

# #Slide 10
# maximum = int(input("Enter upper limit: "))
# for number in range(1, (maximum + 1), 2):
#     print(number)

# Slide 12
# sentence = input("Enter sentence: ").lower()
# vowel_count = 0

# for character in sentence:
#     if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
#         vowel_count += 1
# print(vowel_count)

# Slide 14
# sentence = input("Enter sentence: ")
# reversed = ""
# for character in range(len(sentence) - 1, -1, -1):
#     reversed += sentence[character]
#     print(reversed)

# for character in sentence:
#     reversed = character + reversed
#     print(reversed)

