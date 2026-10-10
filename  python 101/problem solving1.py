#day 1 
#------------------------------------------------------------------------------
#Practice — Question 1
#Variables & print()

Name = "Bandar khaled"
age = 23
University = "city University"

print("Name:",Name)
print("Age:",age)
print("University:",University)

#Question 2 — Input
Name1 = input("please write your name: ")
Age1 = input("please write your age: ")
university1 = input("please write your university: ")

print("Name:",Name1)
print("Age:",Age1)
print("university:",university1)

#Question 3 — Data Types
name2 = "bandar"
age2 = 23
height = 181.0
is_student = True 
address = None 
 
print(type(name2))
print(type(age2))
print(type(height))
print(type(is_student))
print(type(address))

#Question 4 — Type Conversion
age3 = 23 
weight3 = 64.5 

age4 = float(age3)
print (type(age4))
print (age4)


weight4 = int(weight3)
print(type(weight4))
print (weight4)

weight5 = str(weight3)
print(type(weight5))
print(weight5)

# Question 5 — Arithmetic Operators
x = 10 
y = 3 

print(x + y, ",", x - y, ",", x / y, ",", x % y,",",x*y)

#Question 6 — Short Form Operators
number = 10 
number += 5
number -=2
number *=3
number /=2
print (number)

#Question 7 — Comparison Operators
age01 = 23 
print ("Is age equal to 23?", age01 == 23)
print ("Is age greater than 18?", age01 > 18)
print ("Is age less than 30?" , age01 < 30 )
print ("Is age not equal to 20?", age01 != 20)


#Write 3 print() statements:
#1. Check if the person is 18 or older AND has an ID.
#2. Check if the person is under 18 OR has an ID.
#3. Check if the person does NOT have an ID.

age9 = 23 
has_id = True 

print ("Are you 18 old or older? and have id ?",age9 > 18 and has_id )
print("Are you under 18 or have id?",age9 < 18 or has_id)
print("Do you have an Id ?",not has_id)


#Next: Question 9 
#1. Calculate x + y
#2. Calculate x * y
#3. Check if x is greater than y
#4. Check if x + y is greater than 20

x = 15 
y = 4 

print ( x + y)
print (x * y)
print (x > y)
print ( x+y > 20)

# Question 10 — Input + Type Conversion
first = int(input("Enter your first number: "))
second= int(input("Enter your second number: "))

print (first + second)
print (first * second)


#Question 11 — Logical Operators

temperature = 30
is_sunny = True

print (temperature > 25 and is_sunny)
print(temperature < 20 or is_sunny)
print(not is_sunny)

#Question 12 — Final Practice
#Create a program that asks the user for:

#Name:
#Age:
#Number:
#Your program should:

#1. Store the name as a String.
#2. Convert age to an Integer.
#3. Convert number to an Integer.
#4. Print the user’s name.
#5. Add 10 to the number and print the result.
#6. Check if the user’s age is 18 or older.
#7. Check if the number is greater than 50.
#8. Use and to check if age ≥ 18 AND number > 50.

name010 = str(input("Enter your name: "))
age010 =  int(input("Enter your ege: "))
number010 = int(input("Enter any number you like: "))

print (name010)
print("resulte: ",number010 + 10)
print (age010 >= 18)
print(number010 > 50)
print (age010 >= 18 and number010 > 50)
