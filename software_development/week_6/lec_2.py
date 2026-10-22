# SLide 19
# email = input("Enter your email address: ")

# if "@" in email and "." in email and len(email) >= 6:
#     print(f"Valid email address")
# else:
#     print(f"Invalid email address")

email = input("Enter your email address: ")

if "@" in email and "." in email and len(email) >= 6:
    if email.index("@") < email.index("."):
        print(f"Valid email address")
    else:
        print(f"invalid email: @ is before the full stop")
else:
    print(f"Invalid email address")