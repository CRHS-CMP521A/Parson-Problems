'''2numbers.py
Create a program that will ask the user to enter 2 numbers. 
Your program  will then display these 2 numbers and the SUM of these 2 numbers.
'''

num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))
result = num1 + num2
print("Your two numbers are " + str(num1) + " and " + str(num2))
print("The sum is " + str(result))

'''Q2 NameAge
Write a program that will ask the user to input their first name, last name and year they were born. The program will then print the person’s full name and their age.
'''
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
year = int(input("What year were you born? "))

age = 2025 - year
print("Hello " + firstName + " " + lastName + ", you are " + str(age) + " years old.")

'''radius.py
Create a program that will ask a user to enter the radius of a circle. Your program will then display the circumference of that circle and it’s area.
'''
import math  #this will access Python's extra math functions
PI = math.pi #this will store the value of pi (3.14159...) in a variable called PI

radius = float(input("What is the radius? "))
area = PI * radius **2
circumference = 2*PI*radius
print("The circumference is " + str(circumference)+ " and the area is "+ str(area) + ".")


'''fries.py
Create a program for calculating the price of a food order. 
Users should enter a number of fries orders and drinks. 
Program will show food ordered and total cost, including tax.
'''
numnFries = int(input("How many $4.00 fries do you want? "))
numPop = int(input("How many $1.00 pops do you want? "))
print("Order: " + str(numnFries) + " fries and " + str(numPop) + " pop.")
friesTotal = numnFries *4
popTotal = numPop *2
 
subtotal = friesTotal + popTotal
print("Subtotal: $" + str(friesTotal) + " + $"+str(popTotal)  + " =  $" + str(subtotal))
tax = subtotal*0.15
total = subtotal + tax
print("Total: $"+str(subtotal) + " + $"+"{:.2f}".format(tax) + " = $" + "{:.2f}".format(total) )


'''jumps.py
Create a program that will calculate the average of 3 jump lengths of a long-jump athlete.'''
#Remember that to average something you need to add up all the values and divide
jump1 = float(input("Length of first jump: "))
jump2 = float(input("Length of second jump: "))
jump3 = float(input("Length of third jump: "))
average = (jump1 + jump2 + jump3 ) / 3
print("Average jump: " + str(average))


''' T3-Q6-Temperature-Converter.py '''

tempC = float(input("Temperature (C): "))
convert2F = (tempC * 9/5) + 32
print("Temperature in F: " + str(convert2F) + 'F')


''' T3-Q7-Pythagorean-Theorem.py '''
import math

print("Pythagorean Theorem")
sideA = float(input("side a: "))
sideB = float(input("side b: "))
sideCsquared = sideA**2 + sideB**2
sideC = math.sqrt(sideCsquared)

print("Hypotenuse: " + str(sideC))



''' T3-Q8-Making-Change.py '''
print("Change Calculator")
print("What amount of change is needed? ")
change = float(input())

print("You need:")
numToonies = int(change // 2)
change = change % 2
print(str(numToonies) + " toonies")

numLoonies = int(change // 1)
change = change % 1
print(str(numLoonies) + " loonies")

numQuarters = int(change // 0.25)
change = change % 0.25
print(str(numQuarters) + " quarters")

numDimes = int(change // 0.10)
change = change % 0.10
print(str(numDimes) + " dimes")

numNickels = int(change // 0.05)
change = change % 0.05
#NO PENNY: check if rounding UP or DOWN
if change <= 0.02: 
    numNickels = numNickels #round DOWN, no added nickels
else: 
    numNickels = numNickels + 1 #round UP, need 1 more nickel
print(str(numNickels) + " nickels")
