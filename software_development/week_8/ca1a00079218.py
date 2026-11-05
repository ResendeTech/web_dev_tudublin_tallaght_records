# Name: Victor Andrade Resende
# Student Number: A00079218

# Exercise a
# The constants of the file
WEEKLY_WAGE = 100
COMMISION_RATE_1 = 0
COMMISION_RATE_2 = 3
COMMISION_RATE_3 = 5
TAX = 0.15
COMPANY_TEAM_SIZE = 17
COMPANY_TEXT = "PTLT"

# Inputs for employee name, number and the value of treats
employee_name = input("Please enter your name: ")
employee_number = input("Please enter your employee number (The first 4 characters must be PTLT): ")
value_of_treats = float(input("Please enter the value of the treats sold: "))


# Paid commission is kept like this because there is no multiple loops
paid_no_commission = 0 

# commision rate is calculated here
if value_of_treats < 20:
    commision_rate = value_of_treats * (COMMISION_RATE_1 / 100)
elif value_of_treats >= 20 and value_of_treats <= 50:
    commision_rate = value_of_treats * (COMMISION_RATE_2 / 100)
    paid_no_commission += 1
else:
    commision_rate = value_of_treats * (COMMISION_RATE_3 / 100)
    paid_no_commission += 1

# Gross pay, tax_pay and net pay is calculated
gross_pay = WEEKLY_WAGE + commision_rate
tax_paid = gross_pay * TAX
net_paid = gross_pay - tax_paid


# The print statements for the employee details
print(f"{'-' * 25}Employee details{'-' * 25}")
print(f"Employee name: {employee_name}\nEmployee number: {employee_number}\nValue of treat sales: {value_of_treats:.2f} euros\nGross pay: {gross_pay:.2f} euros\nNet pay: {net_paid:.2f} euros\nTax paid: {tax_paid:.2f} euros\nNumber of employees who were paid 0% commission: {paid_no_commission}")
print("\n\n")

# exercise b
# Using indeces for the letters
if 'PTLT' in employee_number[0:4]:
    print(f"Employee number contains {COMPANY_TEAM_SIZE} in the first 4 characters")
else:
    print(f"Warning: The characters {COMPANY_TEAM_SIZE} are not located correctly in the employee number")
print("\n\n")


# exercise c
# Using remainder as the main method of these calculations
teams_in_4s = COMPANY_TEAM_SIZE // 4
remainder = COMPANY_TEAM_SIZE % 4

if remainder > 1:
    teams_in_3s = remainder // 3
    remainder %= 3
    if remainder > 1:
        teams_in_2s = remainder // 2
        remainder %= 2
        if remainder > 1:
            teams_in_1s = remainder
        else:
            teams_in_1s = 0
    else:
        teams_in_1s = 0
        teams_in_2s = 0
else:
    teams_in_3s = 0
    teams_in_2s = 0
    teams_in_1s = remainder

print(f"There will be {teams_in_4s} Teams of 4")
print(f"There will be {teams_in_3s} Teams of 3")
print(f"There will be {teams_in_2s} Teams of 2")
print(f"There will be {teams_in_1s} left without a team")

