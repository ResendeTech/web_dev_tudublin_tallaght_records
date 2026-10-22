def ex_1():
	#Wrong code
	# if grant = True
	#     print(“Grant awarded”)
	# else
	#     print(“No grant awarded”)

	#Right code
	grant = True
	if grant == True:
		print("Grant awarded")
	else:
		print("No grant awarded")

def ex_2():
	print("Answer is D, neither")

def ex_3():
	print("Answer is A, q > 0:")

def ex_4():
	r = 8
	#a
	if r > 1:
		print("YYY")
	else:
		print("ZZZ")
		print("A is correct answer")
	#b
	if r < 1:
		print("YYY")
	else:
		print("ZZZ")
		print("B is correct answer")
	#c
	if r != 1:
		print("YYY")
	else:
		print("ZZZ")
		print("C is correct answer")

def ex_5():
	print("Answer is B, BBB")

def ex_6():
	# t = 10
	# if t > 7:
	# 	print("“AAA”")
   	#    print("“BBB”")
	print("Answer is D, Nothing")

def ex_7():
	print("Answer is A, both a > b and c > d must be true for x to be set to 0")

def ex_8():
	print("Output of the answer:\nFirst\nSecond")

def ex_9():
	USER_PASS_GUEST = "guest"
	PASS_DAWSON = "nos123"
	USER_DAWSON = "M.Dawson"

	username = input("Please enter your username (if you are a guest, enter your username and password as guest): ")
	password = input("Please enter your password: ")

	security = 0
	if username == USER_DAWSON:
		if password == PASS_DAWSON:
			security = 5
			print(f"Hello, {USER_DAWSON}! You are logged in. Your security level is {security}")
		else:
			print("Password is incorrect.")
	elif username == USER_PASS_GUEST:
		if password == USER_PASS_GUEST:
			print(f"Hello, {USER_PASS_GUEST}. You are logged in as a guest. Your security level is {security}")
		else:
			print("Password is incorrect.")
	else:
		print(f"There are no users named {username} in our database.")

def ex_10():
	USER_PASS_GUEST = "guest"
	USER_DAWSON = "M.Dawson"
	USER_WRIGHT = "W.Wright"
	USER_BROWN = "J.Brown"

	PASS_DAWSON = "nos123"
	PASS_WRIGHT = "einstein"
	PASS_BROWN = "Victorian"


	username = input("Please enter your username (if you are a guest, enter your username and password as guest): ")
	password = input("Please enter your password: ")

	security = 0
	if username == USER_DAWSON and password == PASS_DAWSON:
		security = 5
		print(f"Hello, {USER_DAWSON}! You are logged in. Your security level is {security}")

	elif username == USER_WRIGHT and password == PASS_WRIGHT:
		security = 5
		print(f"Hello, {USER_WRIGHT}. You are logged in as a guest. Your security level is {security}")

	elif username == USER_PASS_GUEST and password == USER_PASS_GUEST:
		security = 1
		print(f"Hello, {USER_PASS_GUEST}. You are logged in as a guest. Your security level is {security}")

	elif username == USER_BROWN and password == PASS_BROWN:
		security = 5
		print(f"Hello, {USER_BROWN}. You are logged in as a guest. Your security level is {security}")

	else:
		print(f"Either password or username is incorrect.")



exercises = {
	1: ex_1,
	2: ex_2,
	3: ex_3,
	4: ex_4,
	5: ex_5,
	6: ex_6,
	7: ex_7,
	8: ex_8,
	9: ex_9,
	10: ex_10
}

while True:

	exercise_choice = int(input("Which exercise do you want to choose? If you want every exercise, type '100':  "))

	if int(exercise_choice) in exercises:
		exercises[exercise_choice]()
	elif exercise_choice == 100:
			for exercise in exercises.values():
				exercise()
	else:
		print("Invalid number. Please input another number")