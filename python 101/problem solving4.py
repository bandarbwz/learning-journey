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


print("Q12#------------------------------------------------------------------------------------------------------------")
#Q12/25
#Write a Python program that:
#* Creates age = 23
#* Creates has_id = True
#* Checks if the person is 18 or older AND has an ID
#* Prints "Allowed" if both conditions are true
#* Otherwise, prints "Not Allowed"
age12 = 23
has_id = True 

if age12 >= 18 and has_id:
    print("allowed")
else:
    print("not allowed")


print("Q13#------------------------------------------------------------------------------------------------------------")
#Q13/25
#Write a Python program that:
#* Creates a list called students containing "Ali", "Ahmed", and "Sara"
#* Prints the list
#* Prints the first student
#* Changes "Ahmed" to "Omar"
#* Prints the updated list

students13 = ["ali","ahmad","sara"]
print (students13)
print (students13 [0])
students13 [1] = "omar"
print(students13)

print("Q14#------------------------------------------------------------------------------------------------------------")
#Q14/25
#Write a Python program that:
#* Creates a list called fruits containing "Apple" and "Banana"
#* Adds "Orange" to the end of the list
#* Adds "Mango" at the beginning of the list
#* Prints the final list

fruits = ["apple","banana"]
fruits.append("orange")
fruits.insert(0,"mango")
print(fruits)

print("Q15------------------------------------------------------------------------------------------------------------")
#Q15/25
#Write a Python program that:
#* Creates a list called tasks containing "Study", "Exercise", "Shopping", and "Gaming"
#* Removes "Shopping" from the list
#* Prints the list
#* Clears the entire list
#* Prints the list again

tasks = ["study", "Exercise","shopping","gaming"]
tasks.remove("shopping")
print(tasks)
tasks.clear()
print(tasks)

print("Q16------------------------------------------------------------------------------------------------------------")
#Q16/25
#Write a Python program that:
#* Creates a tuple called colors containing "Red", "Green", and "Blue"
#* Prints the tuple
#* Prints the first element of the tuple
#* Prints the last element of the tuple
#* Prints the type of colors using type()

colors = ("red","green","blue")
print(colors)
print(colors [0])
print(colors [2])
print(type(colors))

print("Q17------------------------------------------------------------------------------------------------------------")
#Q17/25
#Write a Python program that:
#* Creates a dictionary called student
#* Adds:
#* "name" → "Ali"
#* "age" → 23
#* "score" → 85
#* Prints the dictionary
#* Prints the student’s name using the dictionary
#* Changes the student’s score to 90
#* Adds "status" → "Passed"
#* Prints the updated dictionary

student17 = {
    "name":"ali",
    "age":23,
    "score":85
}
print (student17)
print (student17 ["name"])
student17 ["score"] = 90
student17 ["status"]="passed"
print (student17)

print("Q18------------------------------------------------------------------------------------------------------------")
#Q18/25
#Write a Python program that:
#* Creates a dictionary called student with:
#* "name" → "Ali"
#* "age" → 23
#* "score" → 90
#* "status" → "Passed"
#* Prints all the dictionary keys using keys()
#* Prints all the dictionary values using values()
#* Deletes the "status" key using del
#* Prints the updated dictionary

print (student17.keys())
print(student17.values())
print(student17)
del student17 ["status"]
print(student17)

print("Q19------------------------------------------------------------------------------------------------------------")
#Q19/25
#Write a Python program that:
#* Creates a list called numbers containing 10, 20, 30, and 40
#* Prints the type of numbers
#* Uses a for loop to print every number in the list.

numbers = [10,20,30,40]
print(type(numbers))
for nums in numbers:
    print(nums)


print("Q20------------------------------------------------------------------------------------------------------------")
#Q20/25
#Write a Python program that:
#* Uses range() to print the numbers from 1 to 5
#* Then uses a for loop with range() to calculate the sum of the numbers from 1 to 5
#* Prints the final sum.

total = 0 
for n in range(1,6):
    total +=n
print(total)

print("Q20R------------------------------------------------------------------------------------------------------------")
#Q20-C
#write a Python program that:
#* Uses range() to go from 5 to 10
#* Uses a for loop to calculate the sum of all the numbers
#* Prints the final sum.

result = 0
for r in range(5,11):
    result += r

print(result)

print("Q21------------------------------------------------------------------------------------------------------------")
#Q21
#Write a Python program that:
#* Creates a while loop
#* Starts a variable at 1
#* Prints the variable each time
#* Increases the variable by 1
#* Stops when the variable reaches 6.
