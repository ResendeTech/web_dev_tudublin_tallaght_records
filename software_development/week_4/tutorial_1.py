print("="*25, "Exercise 1", "="*25)
string1 = "Python"
print(string1[1:])
print(string1[0:3])
print(string1[:4])
print(string1[:-1])
print(string1[-4:-2])

print("=" * 62)
print("\n")

print("="*25, "Exercise 2", "="*25)

user_input = input("Please enter a word or a sentence pls thanks: ")
print(user_input[:3])
print(user_input[-3:])
print(user_input[::-1])
print(user_input[::2])

print("=" * 62)
print("\n")

print("="*25, "Exercise 3", "="*25)
sentence_user = input("Input a sentence pls: ")
start_position = int(input("start position of splice: "))
end_position = int(input("end position of splice: "))
step_value = int(input("step value of splice: "))

print(sentence_user[start_position:end_position:step_value])
print(sentence_user[::-1])
print(len(sentence_user))
print(sentence_user.upper())

print("=" * 62)
print("\n")

print("="*25, "Exercise 4", "="*25)

user_sentence = input("ENTER A SENTENCE NOW: ")
word_search = input("Now search for a word in that sentence by typing it here: ")
if word_search in user_sentence:
    print("is the word real?", word_search in user_sentence)
    print(f"the word {word_search} is in the sentence!")
    word_index = user_sentence.index(word_search)
    print(f"The word appears first at the index {word_index}")
else:
    print("The word did not match the life")
censored_sentence = user_sentence.replace(word_search, "*"*len(word_search))
print(f"censored sentence is: {censored_sentence}")


print("=" * 62)
print("\n")

print("="*25, "Exercise 5", "="*25)

print(f"{456.8787:.2f}€")
print(f"{456654777:,}€")
print(f"{0.768:.1%}")
print(f"Next year you will be {56+1}")

print("=" * 62)
print("\n")
