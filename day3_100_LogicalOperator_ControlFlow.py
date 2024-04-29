print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("you can ride the rollercoaster")
else:
  print("Sorry, you can't ride")

# Exercise 1 - odd or even
"""
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
"""
# Which number do you want to check?
number = int(input())
check = int(number % 2)

if check == 0:
  print ("This is an even number.")
else:
  print("This is an odd number.")

# Nested if / else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("what is your age")) 
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("Sorry, you can't ride")

# Exercise 2 - BMI 2.0 
"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
"""
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
BMI = weight/(height**2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")

# Challenge - if it is leap or not 
"""
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
This is how you work out whether if a particular year is a leap year.
on every year that is divisible by 4 with no remainder
except every year that is evenly divisible by 100 with no remainder
unless the year is also divisible by 400 with no remainder
"""
# Which year do you want to check?
year = int(input())
if (year%4 == 0 and year %100 != 0) or (year/400%2 == 0):
  print("Leap year")
else:
  print("Not leap year")

# Method 2
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# Multiple if statement in succession

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")
    # Additional photo costs $3
    wants_photo = input("Do you want a photo taken? (Y or N) ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you can't ride.")

# Challenge - Pizza Order 
"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill +=2
  if extra_cheese == "Y":
    bill +=1
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill +=3
  if extra_cheese == "Y":
    bill +=1
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill +=3
  if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}.")

# method 2
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0

if size == "S":
  bill +=15
elif size == "M":
  bill +=20
else:
  bill +=25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}.")

#logical Operators ,and ,or ,not

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    else:
      #include Mid-life crisis free of charge
      if (age >= 45 and age <= 55):
        print("Mid-life crisis $0")
      else:
        bill = 12
        print("Adult ticket is $12")
    # Additional photo costs $3
    wants_photo = input("Do you want a photo taken? (Y or N) ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you can't ride.")

# Challenge - love calculator 
"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combine_name = str(name1+name2)
lower_case = combine_name.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
first_digit = t + r + u + e
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e_second = lower_case.count("e")  # Use a different variable for 'e' in the second digit calculation
second_digit = l + o + v + e_second
score = int(str(first_digit)+str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

