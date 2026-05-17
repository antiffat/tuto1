# Create a program that asks for the user for email address.
# An email is valid if:
# It contains “@”
# It ends with “.com”
# It does not contain spaces
# Keep asking until the email is valid.
# If invalid:
# Print “email invalid”
# If valid:
# Print “email valid”
while True:
    email = input("Enter email: ")

    if "@" in email and email.endswith(".com") and " " not in email:
        print("Valid email")
        break
    else:
        print("Invalid email")
