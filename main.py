# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = (input("What was the total bill? $"))
bill = int(bill)
percentage_tip = (input("How much tip would you like to give? %"))
percentage_tip = int(percentage_tip)
number_of_people = (input("How many people to split the bill? "))
number_of_people = int(number_of_people)
cost = float((percentage_tip / 100) * (bill/ number_of_people)) + (bill / number_of_people)
cost = round(cost, 2)
print(f"Each person should pay ${cost}")
