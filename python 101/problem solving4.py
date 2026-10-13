print("Q1------------------------------------------------------------------------------------------------------------")
#Q1/25 — Variables & Data Types
#Write a Python program that:
#* Creates a variable called name containing your name.
#* Creates a variable called age containing your age.
#* Creates a variable called height containing a decimal number.
#* Creates a variable called student containing True.
#* Prints all four variables.

name_q1 = "bandar"
age_q1 = 23
height_q1 = 181.5
student_q1 = True 

print(name_q1)
print(age_q1)
print(height_q1)
print(student_q1)

print("Q2------------------------------------------------------------------------------------------------------------")
#Q2/25 — input() + Type Conversion
#Write a Python program that:
#* Asks the user to enter their age.
#* Converts the input into an integer.
#* Adds 5 to the age.
#* Prints the new age.

age_q2= int(input("write your age :"))
age_q2 +=5
print (age_q2)

print("Q3------------------------------------------------------------------------------------------------------------")
#Q3/25 — Arithmetic Operators
#Write a Python program that:
#* Creates two variables: a = 20 and b = 6.
#* Calculates and prints:
#* Addition , #* Subtraction ,#* Multiplication ,#* Division , #* Remainder

a = 20 
b = 6
print (
    "20 + 6 = ", a + b ,
    "20 - 6 = ",a - b,
    "20 * 6 = ",a * b,
    "20 / 6 = ",a / b ,
    "20 % 6 = ",a % b
)


print("Q4------------------------------------------------------------------------------------------------------------")
#Q4/25 — Comparison + Logical Operators
#Write a Python program that:
#* Creates age = 23.
#* Checks if age is greater than or equal to 18.
#* Checks if age is less than 30.
#* Uses and to combine the two conditions.
#* Prints the final result (True or False).

age_q4 = 23 
print(age_q4 >= 18 and age_q4 < 30)

print("Q5------------------------------------------------------------------------------------------------------------")
#Q5/25
#Write a Python program that:
#* Creates price = 50
#* Creates quantity = 3
#* Calculates the total price
#* Stores the result in total
#* Prints total

price =50 
quantity = 3

total = price * quantity 
print ("total : ", total)

print("Q6------------------------------------------------------------------------------------------------------------")
#Q6/25
#Write a Python program that:
#* Creates age = 23
#* Converts age from an integer to a float
#* Stores the result in age_float
#* Prints age_float

age_q6 = 23
age_float = float(age_q6)

print (age_float)


print("Q7------------------------------------------------------------------------------------------------------------")
#Q7/25
#Write a Python program that:
#* Creates score = 80
#* Adds 10 to score using a short-form assignment operator
#* Prints score

score_q7 = 80 
score_q7 += 10 
print(score_q7)


print("Q8------------------------------------------------------------------------------------------------------------")
#Q8/25
#Write a Python program that:
#* Creates name = "Bandar"
#* Prints the first character of name
#* Prints the last character of name

name_q8 = "bandar"
print (name_q8[0])
print(name_q8 [5])

print("Q8R------------------------------------------------------------------------------------------------------------")
#Q8/25 — Replacement
#Write a Python program that:
#* Creates num1 = 20
#* Creates num2 = 6
#* Calculates the remainder when num1 is divided by num2
#* Stores the result in remainder
#* Prints remainder

num1 = 20 
num2 = 6

remainder = num1 % num2 
print ("remainder:",remainder)


print("Q9------------------------------------------------------------------------------------------------------------")
#Q9/25
#Write a Python program that:
#* Creates temperature = 35
#* Checks if temperature is greater than 30
#* Prints the result (True or False)

#first way 
temperature = 35 
if temperature > 30 :
    print ("true")
else:
    print("false")

#another way 
result = temperature > 30 
print("result: ",result)


print("Q10------------------------------------------------------------------------------------------------------------")
#Q10/25
#Write a Python program that:
#* Creates age = 23
#* Checks if age is greater than or equal to 18
#* If it is, print "Adult"
#* Otherwise, print "Minor"
age_q10 = 23
if age_q10 >= 18:
    print("adult")
else:
    print ("minor")


print("Q11#------------------------------------------------------------------------------------------------------------")
#Q11/25
#Write a Python program that:
#* Creates score = 78
#* If the score is 90 or above, print "Excellent"
#* If the score is 80 or above, print "Very Good"
#* If the score is 70 or above, print "Good"
#* Otherwise, print "Needs Improvement"

score11 = 78 
if score11 >= 90:
    print("excellent")
elif score11 >= 80 :
    print("very good")
elif score11 >= 70 :
    print("good")
else:
   print ("needs improvement")

