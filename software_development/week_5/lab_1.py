def ex_1():
    # variables
    SINGLE = 0.2
    MARRIED = 0.23
    TAX_ALLOWANCE_1 = 25000
    TAX_ALLOWANCE_2 = 20000

    print(f"{'Welcome to the Payroll Program':>30}")

    id = input("Please enter your employee identification number: ")
    name = input("Please enter your full name: ").title()
    address = input("Please enter your address: ")
    marital_status = input("Please enter your marital status as either single (type 's') or married (type 'm'): ").lower()
    gross_pay = float(input("Please enter your gross pay: "))

    if gross_pay < 50000:
        taxable_pay = gross_pay - TAX_ALLOWANCE_1
    elif gross_pay >= 50000:
        taxable_pay = gross_pay - TAX_ALLOWANCE_2

    if marital_status == "s":
        taxed_pay = taxable_pay * (1 - SINGLE)
        tax_paid = taxable_pay - taxed_pay
        if gross_pay < 50000:
            net_pay = taxed_pay + TAX_ALLOWANCE_1
        elif gross_pay >= 50000:
            net_pay = taxed_pay + TAX_ALLOWANCE_2

    elif marital_status == "m":
        taxed_pay = taxable_pay * (1 - MARRIED)
        tax_paid = taxable_pay - taxed_pay
        if gross_pay < 50000:
            net_pay = taxed_pay + TAX_ALLOWANCE_1
        elif gross_pay >= 50000:
            net_pay = taxed_pay + TAX_ALLOWANCE_2


    print(f"Payroll Details For Employee {id}\nId: {id}\nName: {name}\nAddress: {address}\nMarital Status: {marital_status}")
    print(f"For a gross pay of {gross_pay:,.2f} euros, a net pay of {net_pay:,.2f} euros and total tax of {tax_paid:,.2f} euros.")

    print("Security Feature")
    password = input("Please enter your password: ")
    pass_confirmation = input("Please re-enter your password: ")

    if password == pass_confirmation:
        print("Passwords are the same.")
    elif password != pass_confirmation:
        print("Passwords are not the same.")

def ex_2():
    HOURLY_WAGE = 12.25
    OVERTIME_WAGE = 1.5 * 12.25
    WORK_WEEK_HOURS = 38
    COMMISION = 0.05
    COMMISION_REQUIREMENT = 50

    total_hours = int(input("Enter total hours worked: "))
    total_sales = int(input("Enter total sales in euros: "))

    pay = total_hours * HOURLY_WAGE
    employees_with_com = 0
    if total_hours > WORK_WEEK_HOURS:
        overtime_pay = OVERTIME_WAGE * (total_hours - WORK_WEEK_HOURS)
        pay += overtime_pay
    elif total_sales > COMMISION_REQUIREMENT:
        commision_pay = total_sales * COMMISION
        pay += commision_pay
        employees_with_com += 1

    print(f"\nNumbers of hours worked: {total_hours:>24} hours\nTotal sales: {total_sales:>39.2f} euros\nPay: {pay:>48.2f} euros\nNumbers of employees who earned commision: {employees_with_com:>5} employees")



exercises = {
    1: ex_1,
    2: ex_2,
}

while True:

    exercise_choice = int(input("Which exercise do you want to choose? If you want every exercise, type '9':  "))

    if exercise_choice in exercises:
        exercises[exercise_choice]()
    elif exercise_choice == 9:
            for exercise in exercises.values():
                exercise()
    else:
        print("Invalid number. Please input another number")
