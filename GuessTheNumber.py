import random
print("Rishi Chaturvedi, USN: 1AY24AI089, SEC: O")

num = int(input("Enter the number between 1 to 9: "))

# Validate input
while num < 1 or num > 9:
    num = int(input("Invalid input! Please enter a number between 1 to 9: "))

print(num, "is the number entered by user")

# Computer random number
comp_num = random.randint(1, 9)
print(comp_num, "is the number randomly taken by computer")

# Compare and display result
if num == comp_num:
    print("User guess is Absolutely Correct!!!!!!!!!!")
else:
    print("Oh NO! User guess is Incorrect!!!!!!!!!!")
