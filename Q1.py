# Q1: Username Validation System

# Accept the username from the user
username = input("Enter a username: ")

# Rule checks (using string operations and comparison operators)
only_spaces = username.strip() == ""        # True if empty or only spaces
too_short = len(username) < 5               # fewer than 5 characters
is_admin = username.lower() == "admin"      # ignore uppercase/lowercase

# Check the rules one by one and show a meaningful reason on rejection
if only_spaces:
    print("Invalid username: it cannot contain only spaces.")
elif too_short:
    print("Invalid username: it must contain at least 5 characters.")
elif is_admin:
    print("Invalid username: 'admin' is not allowed (in any letter case).")
else:
    print("Valid username:", username)
