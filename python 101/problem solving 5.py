# Day 1–5 — 30 Problem-Solving Questions:
print("Q1-------------------------------------------------------")
# Q1 / 30 — Easy
#Write a Python program that:
#* Creates a variable name with your name.
#* Creates a variable age with your age.
#* Creates a variable student with the value True.
#* Prints all three variables.
#* Prints the type of each variable.

nameQ1 = "bandar"
ageQ1 = 23
studentQ1 = True 
print (nameQ1)
print(ageQ1)
print(studentQ1)
print(type(nameQ1))
print(type(ageQ1))
print(type(studentQ1))

print("Q2-------------------------------------------------------")
# Q2 / 30 — Easy
#Write a Python program that:
#* Asks the user to enter their age.
#* Converts the input into an integer.
#* Adds 5 to the age.
#* Stores the result in a variable called future_age.
#* Prints future_age.
#* Prints its type.
ageQ2 = input ("enter your age : ")
ageQ21 = int(ageQ2)
ageQ21 += 5
future_age = ageQ21
print ("future age : ",future_age)
print(type(future_age))

print("Q3-------------------------------------------------------")
#Q3 / 30 — Easy
#Write a Python program that:
#Creates a variable price = 50
#* Creates a variable quantity = 3
#* Calculates the total price
#* Stores it in a variable called total
#* Prints the total
#* Then applies a RM10 discount using a short-form assignment operator
#* Prints the final price
price = 50 
quantity = 3
total = price * quantity 
print ("the price for 1 = ",price ,"the quantity: ",quantity ,"the total price = ", total)
total -= 10
print ("after discount = ",total )

print("Q4-------------------------------------------------------")
#Q4 / 30 — Easy — Student System
#You are making a small program for a university.
#A student has:
#* age = 20
#* has_id = True
#Write a program that:
#1. Checks if the student is 18 or older AND has an ID.
#2. If both are true, print: Student can enter the exam.
#3. Otherwise, print: Student cannot enter the exam.
ageQ4 = 20 
has_id = True 
if ageQ4 >= 18 and has_id :
    print("student can enter the exam")
else:
    print("student cannot enter the exam")

print("Q5-------------------------------------------------------")
#Q5 / 30 — Easy — Shopping Cart
#You are making a simple shopping program.
#A customer buys:
#* A laptop bag for RM80
#* A mouse for RM50
#* A keyboard for RM100
#Write a program that:
#1. Creates a variable for each price.
#2. Calculates the total price.
#3. Prints the total.
#4. The customer has a RM30 discount.
#5. Applies the discount using a short-form assignment operator.
#6. Prints the final price.
laptop = 80 
mouse = 50 
keyboard = 100 
total = laptop + mouse + keyboard 
print ("laptop =",laptop,"RM,","mouse= ",mouse,"RM,","keyboard= ",keyboard,"RM,","total = ",total,"RM")
total -= 30
print("after discount = ",total)

print("Q6-------------------------------------------------------")
#Q6 / 30 — Easy → Medium — Cinema Tickets 
#You are building a small cinema ticket system.
#A customer buys:
#* 2 adult tickets at RM25 each
#* 1 child ticket at RM15
#The customer pays RM100.
#Write a program that:
#1. Creates variables for the ticket prices.
#2. Calculates the total cost.
#3. Calculates how much money is left after paying.
#4. If the remaining money is greater than or equal to RM0, print:Payment successful
#5. Otherwise, print: Not enough money

ticket = 100 
adult = 25 
child = 15 
adult_quantity = 2
customer_total = adult * adult_quantity + child 
after_paying = ticket - customer_total  

if after_paying >= 0:
    print("payment successful")
else:
    print("Not enough money")


print("Q7-------------------------------------------------------")
#Q7 / 30 — Easy → Medium — Student Grades 
#A university wants a simple program to check a student’s result.
#The student has:
#* assignment = 25
#* midterm = 30
#* final = 35
#The maximum total is 100.
#Write a program that:
#1. Calculates the student’s total mark.
#2. Prints the total.
#3. If the total is 90 or higher, print Grade A
#4. If the total is 80 or higher, print Grade B
#5. If the total is 70 or higher, print Grade C
#6. Otherwise, print Fail