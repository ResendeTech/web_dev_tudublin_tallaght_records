def ex_1():
	LETTER_STANDARD_PRC = 10.5
	LETTER_PRIORITY_PRC = 12
	
	BOX_1ST_POUND_PRIORITY = 15.75
	BOX_1ST_POUND_STANDARD = 13.75
	
	BOX_EACH_POUND_PRIORITY = 1.25
	BOX_EACH_POUND_STANDARD = 1

	POUND_TO_OUNCES = 16
	
	package_type = input("What is the type of package you wish to order (letter or box)? ").lower()
	service_type = input("What type of service you want (standard or priority)? ").lower()
	
	if package_type == "letter":
		weight = float(input("What is the weight of your letter in ounces? "))
		round(weight)
		if service_type == "standard":
			print(f"The fee is {LETTER_STANDARD_PRC} euros for a package with:\n{'type:':>12} {package_type}\n{'Service:':>15} {service_type}\n{'Ounces:':>14} {weight}")
		elif service_type == "priority":
			print(f"The fee is {LETTER_PRIORITY_PRC} euros for a package with:\n{'type:':>12} {package_type}\n{'Service:':>15} {service_type}\n{'Ounces:':>14} {weight}")

	elif package_type == "box":
		pass
	
	else:
		print(f"{package_type} is not a valid package type.")

	if package_type == "box":
		weight = float(input("What is the weight of your box in pounds? "))
		round(weight)
		if service_type == "standard":
			if weight <= 1:
				total_cost = BOX_1ST_POUND_STANDARD
			elif weight >= 2:
				weight -= 1
				print(weight)
				total_cost = (BOX_EACH_POUND_STANDARD * weight) + BOX_1ST_POUND_STANDARD
				weight += 1

			weight = weight * POUND_TO_OUNCES
			print(f"The fee is {total_cost} euros for a package with:\n{'type:':>12} {package_type}\n{'Service:':>15} {service_type}\n{'Ounces:':>14} {weight}")
				
		elif service_type == "priority":
			if weight <= 1:
				total_cost = BOX_1ST_POUND_PRIORITY
			elif weight >= 2:
				weight -= 1
				print(weight)
				total_cost = (BOX_EACH_POUND_PRIORITY * weight) + BOX_1ST_POUND_PRIORITY
				weight += 1

			weight = weight * POUND_TO_OUNCES
			print(f"The fee is {total_cost} euros for a package with:\n{'type:':>12} {package_type}\n{'Service:':>15} {service_type}\n{'Ounces:':>14} {weight}")
	
	elif package_type == "letter":
		pass
	
	else:
		print(f"{package_type} is not a valid package type.")

def ex_2():
	STANDARD_WORKING_WEEK = 39
	STANDARD_PAY_RATE = 35
	OVERTIME_RATE = 50
	TAX = 0.21
	WEEKLY_TAX_ALLOWANCE = round(18000 / 52, 2)

	work_time = int(input("Please enter hours worked this week: "))

	if work_time <= STANDARD_WORKING_WEEK:
		standard_pay = work_time * STANDARD_PAY_RATE
		gross_pay = standard_pay
		overtime_pay = 0
	elif work_time > STANDARD_WORKING_WEEK:
		overtime = work_time - STANDARD_WORKING_WEEK
		standard_pay = STANDARD_WORKING_WEEK * STANDARD_PAY_RATE
		overtime_pay = overtime * OVERTIME_RATE
		gross_pay = overtime_pay + standard_pay


	if gross_pay > WEEKLY_TAX_ALLOWANCE:
		taxed_pay = gross_pay - WEEKLY_TAX_ALLOWANCE
		total_tax = taxed_pay * TAX
	else:
		total_tax = 0

	net_pay = gross_pay - total_tax
	print(f"Hours: {work_time:.1f}\nStandard pay amount: {standard_pay:.2f} euros\nOver-time pay amount: {overtime_pay:.2f} euros\nGross Pay: {gross_pay:.2f} euros\n{'-' * 35}\nTotal Tax: {total_tax:.2f} euros\n{'-' * 35}\nNet Pay: {net_pay:.2f} euros")



exercises = {
	1: ex_1,
	2: ex_2,
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