# Import Section

from datetime import datetime

# Flower Box Section
#########################################################
#
#   Name:  Abdullahi Abdulkareem L20581655
#   Date:  01/28/24
#   Program Description:
#
#   Description: This program takes user input for employee data, generates usernames, removes duplicates, and provides relevant outputs.
#########################################################

# Input section
employee_data_list = []

for i in range(5):  # Prompt user for information for 5 employees
    # Get user input for employee details
    first_name = input("Enter your first name? ")
    last_name = input("Enter your last name? ")
    birth_year = input("Enter the year were you born ")

    # Validate the length of users input
    if first_name.__len__ < 2 or last_name.__len__ < 2 or birth_year.__len__ != 4:
        print("Invalid input. Please make sure your first and last names are at least 2 characters long, and birth year is 4 characters long.")
        continue

    # Display information for confirmation
    print("\nEmployee Information:")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Birth Year: {birth_year}")

    confirm = input("Is the information correct? (Yes/No): ").lower()

    if confirm == 'yes':
        employee_data_list.append((first_name, last_name, birth_year))
    else:
        print("Please enter the information again.\n")

# Process section
# Create employee usernames
usernames = []
employee_data = {}

for first_name, last_name, birth_year in employee_data_list:
    username = f"{first_name[0].lower()}{last_name.lower()}{str(birth_year)[-2:]}"

    # Check for duplicates
    if username in usernames:
        new_username = f"{first_name.lower()}{last_name[0].lower()}{str(birth_year)[-2:]}"
        usernames.append(new_username)
        employee_data[new_username] = (first_name, last_name, birth_year)
    else:
        usernames.append(username)
        employee_data[username] = (first_name, last_name, birth_year)

# Copy username list without duplicates
username_copy = list(set(usernames))

# Sort the username copy list
username_copy.sort()

# Output section
# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d')

# Print
print("\nUsername:", today_date)
print("Employee Data list used to gather user input:", employee_data_list)
print("Username list with all usernames (even the duplicates):", usernames)
print("Employee Data dictionary:", employee_data)
print("Username list that has been sorted:", username_copy)
