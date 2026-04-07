#WAP to input First name, middle name & last name into the variables a apply them concatation.
first_name = input("Enter First Name: ")
middle_name = input("Enter Middle Name (press enter if none): ")
last_name = input("Enter Last Name: ")

full_name = f"{first_name} {middle_name} {last_name}".strip()

full_name = " ".join(full_name.split())

print("Full Name:", full_name)
