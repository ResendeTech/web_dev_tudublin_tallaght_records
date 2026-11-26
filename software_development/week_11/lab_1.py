import random

ADMIN_USERNAME = "Admin"
ADMIN_PASS = "AD2026"
STRIKER_COUNT = 2
PAY_PER_GOAL = 49.5
BONUS_GOAL_PAY = 100.50

print("Welcome to the Dublin Football League Analysis System")
print("Welcome Screen")

username = input("Enter username: ")
password = input("Enter password: ")

if username != ADMIN_USERNAME or password != ADMIN_PASS:
    print("Access Denied. Program Ending.")
    quit()

print("Access Granted\n")

choice_1 = False
while True:
    print("=====MAIN MENU=====")
    print("1. Enter Striker Details & Calculate Pay")
    print("2. Determine Player for Promotional Function")
    print("3. Exit Program")
    choice = input("Enter your choice: ")
    if not choice.isdigit() or int(choice) > 3 or int(choice) < 1:
        print("Invalid selection, please choose a number from 1-3\n")
        continue

    if int(choice) == 1:
        choice_1 = True
        print("---Enter Striker Details---\n")
        striker_pay = 0
        total_team_pay = 0
        striker_details = {}
        for i in range(1, STRIKER_COUNT + 1):
            print(f"Striker {i}")
            striker_name = input("Enter name: ")
            striker_goals = int(input("Enter goals scored this week: "))

            striker_pay += PAY_PER_GOAL * striker_goals
            if striker_goals >= 3:
                print("BONUS AWARDED: Player has earned the goal bonus!")
                striker_pay += BONUS_GOAL_PAY
            total_team_pay += striker_pay

            striker_details.update({
                f"striker_{i}": {
                    "name": striker_name,
                    "goals": striker_goals,
                }}
            )
            
            print(f"Pay for {striker_name} is {striker_pay:.2f} euros")

            striker_pay = 0
        print(f"Total striker pay for the team: {total_team_pay:.2f} euros")

    if int(choice) == 2:
        if choice_1 == False:
            print("\nError: Enter striker details first.")
            continue
        
        sentence = ""
        if striker_details['striker_1']['goals'] == striker_details['striker_2']['goals']:
            random_n = random.randint(1, 2)
            print("---Promotional Function Selection---")
            sentence = f"{striker_details[f'striker_{random_n}']['name']} has been randomly selected."

        elif striker_details['striker_1']['goals'] > striker_details['striker_2']['goals']:
            sentence = f"{striker_details[f'striker_1']['name']} has been selected."
        
        else:
            sentence = f"{striker_details[f'striker_2']['name']} has been selected."

        if sentence is not "":
            print("---Promotional Function Selection---")
        print(sentence)
        print("\n")

    if int(choice) == 3:
        print("Program ending. Goodbye!")
        break
