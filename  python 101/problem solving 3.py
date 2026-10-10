#mix day 1,2 and 3 to make sure we understand evrything 

print("Q1------------------------------------------------------------------------------------------------------------")
#Question 1/20 — Variables + input() + Type Conversion + print() + type()
#Create a program that asks the user for their name, age, and university.
#Your program should:
#* Store the name as a string.
#* Convert the age to an integer.
#* Print the name, age, and university.
#* Print the data type of the age.

name = input("write your name: ")
age = input("write your age: ")
uni = input("write your uni:")

age1 = int(age)
print(type(age1))

print(name)
print(age1)
print(uni)


print("Q2------------------------------------------------------------------------------------------------------------")
#Question 2/20 — Data Types + type() + None
#Create five variables representing:
#* A person’s name
#* Their age
#* Their height
#* Whether they are a student
#* An address that currently has no value

name1 = "bandar"
age2 = 23
height = 181.5
is_student = True
adress = None 

print(type(name1)) 
print(type(age2)) 
print(type(height)) 
print(type(is_student)) 
print(type(adress)) 


print("Q3------------------------------------------------------------------------------------------------------------")
#Question 3/20 — Type Conversion + Arithmetic Operators
#Create two variables:
#* A person’s age as an integer
#* Their weight as a float
#Then:
#1. Convert the age to a float.
#2. Convert the weight to an integer.
#3. Convert the weight to a string.
#4. Add 5 to the original age.
#5. Multiply the original weight by 2.
#6. Print the results.

person_age = 23
person_weight = 78.50

person_age1 = float(person_age)
person_weight1 = int(person_weight)
person_weight2= str(person_weight)

print ("resulte = ", person_age + 5)
print("reslte =", person_weight * 2)
print(person_age1)
print(person_weight1)
print(person_weight2)
print(type(person_age1 ))
print(type(person_weight1))
print(type(person_weight2))

print("Q4------------------------------------------------------------------------------------------------------------")
#Question 4/20 — Arithmetic + Short-form Operators
#Create a number with an initial value of 20.
#Then perform these operations in order:
#1. Add 10 using a short-form operator.
#2. Subtract 5 using a short-form operator.
#3. Multiply by 2 using a short-form operator.
#4. Divide by 5 using a short-form operator.
#5. Print the final result.
#Then create two other numbers and print their:
#* Addition * Subtraction * Multiplication * Division * Remainder

number =20 
number +=10
number -=5 
number *=2
number /=5
print("the result of 20 + 10 - 5 * 2 / 5 = ",number)

num1 = 2
num2 = 2
print ("2 + 2 = ",num1 + num2,"|","2-2 = ",num1 - num2,"|","2 x 2 = ",
       num1 * num2 ,"|","2 / 2 = ",num1 / num2 ,"|", "2 % 2 = ", num1 % num2)

print("Q5------------------------------------------------------------------------------------------------------------")
#Question 5/20 — Input + Type Conversion + Comparison Operators + Logical Operators + if/else
#A student enters their age and exam score.
#Create a program that:
#* asks for the age
#* asks for the exam score
#* converts both inputs to numbers
#* checks whether the student is 18 or older AND has a score of 50 or higher
#* if both conditions are true, print "Eligible"
#* otherwise, print "Not eligible"
#* also print the data type of the age and score

name_student = input ("what is your name ? ")
age_student = input ("How old are you ? ")
exam_score = input("what is your score at exam ? ")

age_student1 = int(age_student)
exam_score1 = int(exam_score)

if age_student1 >= 18 and exam_score1 >= 50:
    print ("Eligible")
else:
    print ("Not eligible")

print (type(age_student1))
print(type(exam_score1))


print("Q6------------------------------------------------------------------------------------------------------------")
#Question 6/20 — Lists + Indexing + Changing Elements + append()
#Create a list containing 5 different items.
#Then:
#1. Print the first item.
#2. Print the last item.
#3. Change the third item to something else.
#4. Add a new item to the end of the list.
#5. Print the final list.

num_list = [1,2,3,4,5]
print (num_list [0])
print (num_list [4])
num_list[2] = 20
num_list.append(30)
print(num_list)

print("Q7------------------------------------------------------------------------------------------------------------")
#Question 7/20 — Lists + insert() + remove() + clear()
#Create a list containing 5 items.
#Then:
#1. Add a new item at index 2.
#2. Remove one specific item from the list.
#3. Print the list.
#4. Remove all remaining items from the list.
#5. Print the list again.

number_list = [1,2,3,4,5]
number_list.insert(2,30)
number_list.remove(1)
print(number_list)
number_list.clear()
print(number_list)

print("Q8------------------------------------------------------------------------------------------------------------")
#Question 8/20 — Lists + type() + Index
#Create a list containing 4 different items.
#Then:
#1. Print the type of the variable.
#2. Print the index of each item by accessing the items using their indexes.
#3. Change the last item.
#4. Print the final list.

list_letters = ["A","B","C","D"]
print(type(list_letters))
print(list_letters[0])
print(list_letters[1])
print(list_letters[2])
print(list_letters[3])
list_letters [3] = 30
print(list_letters)

print("Q9------------------------------------------------------------------------------------------------------------")
#Question 9/20 — Tuples + Accessing Elements
#Create a tuple containing 5 different items.
#Then:
#1. Print the first item.
#2. Print the third item.
#3. Print the last item.
#4. Print the type of the tuple.

number_tuple = (1,2,3,4,5)
print(number_tuple [0])
print(number_tuple[2])
print(number_tuple[4])
print(type(number_tuple))

print("Q10------------------------------------------------------------------------------------------------------------")
#Question 10/20 — Dictionaries + Accessing + Changing Values
#Create a dictionary containing information about a student:
#* Name * Age * University * Major
#Then:
#1. Print the student’s name.
#2. Print the student’s university.
#3. Change the student’s major to something else.
#4. Print the updated dictionary.

student = {
    "name": "bandar khaled salem",
    "age": 20,
    "university" : "city uni",
    "major":"CS"
}

print(student["name"])
print(student["university"])
student ["major"] = "data seince"
print(student)

print("Q11------------------------------------------------------------------------------------------------------------")
#Question 11/20 — Dictionaries + Adding Elements + keys() + values()
#Create a dictionary containing 3 items.
#Then:
#1. Add a new item to the dictionary.
#2. Print all the keys.
#3. Print all the values.
#4. Print the final dictionary.

students_class = {
    "name":"bandar",
    "age":23,
    "major":"CS"
}

students_class ["univercity"] = "city u"

print (students_class)
print (students_class.keys())
print (students_class.values())
print (students_class)


print("Q12------------------------------------------------------------------------------------------------------------")
#Question 12/20 — Dictionary + del + Accessing + Changing Values
#Create a dictionary containing 4 items.
#Then:
#1. Access and print one value.
#2. Change one value.
#3. Delete one item using del.
#4. Print the final dictionary.

numbers0 = {
    "num1": 1,
    "num2": 2,
    "num3": 3,
    "num4": 4,
}

numbers0 ["num1"] = 6
print(numbers0)
print(numbers0["num1"])
del numbers0 ["num1"]
print(numbers0)


print("Q13------------------------------------------------------------------------------------------------------------")
#Question 13/20 — Mixed: List + Dictionary + if/else + Comparison
#Create a list containing 3 exam scores.
#Create a dictionary containing a student’s name and age.
#Then:
#1. Access the student’s age from the dictionary.
#2. Access the student’s first exam score from the list.
#3. Check if the student is 18 or older.
#4. If they are 18 or older, print "Adult student".
#5. Otherwise, print "Under 18".
#6. Print the student’s name and first exam score.

score_list =[20,18,17]

student13 = {
    "name1":"bandar",
    "age101":23
}

print(student13 ["age101"])
print(score_list[0])

if student13["age101"] >= 18 :
    print("Adult")
else:
    print("under 18")

print(student13 ["name1"])
print(score_list[0])

print("Q14------------------------------------------------------------------------------------------------------------")
#Question 14/20 — if + elif + else + Comparison Operators
#Create a program that asks the user for their exam score.
#Then classify the score:
#* 80 or higher → "Excellent"
#* 60–79 → "Good"
#* 50–59 → "Pass"
#* Below 50 → "Fail"
#Use if, elif, and else.
#Also convert the user’s input to an integer.

exam_result = input("write your score: ")
exam_result1 = int(exam_result)

if exam_result1 >= 80:
    print("excellent")
elif exam_result1 >= 60 :
    print("good")
elif exam_result1 >= 50 :
    print("pass")
else:
    print("fail")


print("Q15------------------------------------------------------------------------------------------------------------")
#Q15 — not + if/else + List
#1. Create a list with 3 numbers.
#2. Create a variable called number and give it a number.
#3. Check the number:
#   * If the number is NOT greater than 10 → print "10 or less"
#    * Otherwise → print "Greater than 10"
#4. Print the list.

list_numbers = [1,2,3]
number103 = 23

if not number103 > 10 :
    print("10 or less")
else:
    print("greater than 10")

print(list_numbers)

print("Q16------------------------------------------------------------------------------------------------------------")
#Q16/20 — or + comparison operators
# student enters their age.
#If the age is less than 18 OR greater than 60, print:
#"Special age group"
#Otherwise, print:
#"Normal age group"

student104 = input("write your age: ")
student105 = int(student104)

if student105 < 18 or student105 > 60:
    print("special age group")
else:
   print ("Normal age group")


print("Q17------------------------------------------------------------------------------------------------------------")
#Q17/20 — not + comparison
#Create a variable called score and give it a number.
#Check the score:
#* If the score is NOT less than 50, print "Pass"
#* Otherwise, print "Fail"

score = 49
if not score < 50:
    print("pass")
else:
    print("fail")

print("Q18------------------------------------------------------------------------------------------------------------")
# Q18/20 — == + != + if/elif/else
#Create a variable called password and give it a value.
#Check it:
#* If the password is equal to "1234" → print "Correct"
#* If the password is not equal to "1234" → print "Wrong"

password = 4423
if password == "1234" :
    print("correct")
else:
   print ("wrong")

print("Q19------------------------------------------------------------------------------------------------------------")
#Q19/20 — != + if/else
#Create a variable called country and give it a country name.
#Check it:
#* If the country is not equal to "Malaysia" → print "Different country"
#* Otherwise → print "Malaysia"
country = input("write your country: ")

if country != "Malaysia":
    print("Different country")
else:
    print("Malaysia")


print("Q20------------------------------------------------------------------------------------------------------------")
#Q20/20 — Final Mixed Challenge 
#Create:
#1. A list containing 3 numbers.
#2. A dictionary containing a student’s name and score.
#3. Change the student’s score to another value.
#4. Check the score:
#    * If the score is 80 or higher → "Excellent"
#    * If the score is 50 or higher → "Pass"
#    * Otherwise → "Fail"
#5. Print the list.
#6. Print the student’s name.

list_numbers_final = [1,2,3]
student_final = {
    "name":"bandar",
    "score104": 50
}

student_final ["score104"] = 80

if student_final ["score104"] >= 80 :
    print ("excellent")
elif student_final ["score104"] >= 50 :
    print("pass")
else:
    print("fail")

print(list_numbers_final)
print(student_final["name"])