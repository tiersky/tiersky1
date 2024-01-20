# This is a simple Python script

# Ask the user for their name
name = input("Please enter your name: ")

# Ask the user for their age
age = input("Please enter your age: ")

# Print a welcome message
print(f"Hello {name}, you are {age} years old.")

# Additional functionality: Calculate the year when the user will turn 100
current_year = 2024  # Assuming the current year is 2024
age_100 = 100 - int(age)
year_when_100 = current_year + age_100
print(f"{name}, you will turn 100 years old in the year {year_when_100}.")
