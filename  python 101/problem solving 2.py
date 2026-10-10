#day2
#------------------------------------------------------------------------------------
print("1----------------------------------------------------")
#Question 1 — List: Accessing Elements
names = ["Dana" , "mariam" , "Hessah" , "fatimah"]

print (names[0])
print (names[2])
print (names[3])

print("2----------------------------------------------------")
#Question 2 — List: Changing Elements
#You have a list containing Dana, Mariam, and Hessah.
#Change Dana’s name to Ghada using her position in the list, then print the entire list.

names1 = ["Dana","mariam","hessah"]
names1 [0]= ("Ghada")

print(names1)

print("3----------------------------------------------------")
#Question 3 — List: append()
#Create a list containing Dana and Mariam. Add Hessah to the end of the list using append(), then print the list.

names2 = ["Dana","mariam"]
names2.append("hessah")

print(names2)

print("4----------------------------------------------------")
#Question 4 — List: insert()
#Create a list containing Dana, Mariam, and Hessah.
#Add Ghada at index 1 using insert(), then print the entire list.

names3 = ["Dana","mariam","hessah"]
names3.insert(1,"Ghada")
print(names3)

print("5----------------------------------------------------")
#Question 5 — List: remove()
#Create a list containing Dana, Mariam, and Hessah.
#Remove Mariam from the list using remove(), then print the entire list.

names4 = ["dena",'mariam','hessah']
names4.remove("mariam")
print(names4)

print("6----------------------------------------------------")
#Question 6 — List: clear()
#Create a list containing three names.
#Remove all elements from the list using clear(), then print the list to confirm that it is empty.

names5 = ["bandar","khaled","salem"]
names5.clear()
print(names5)

print("7----------------------------------------------------")
#Question 7 — List: type()
#Create a list containing three names. Check and print the type of the list using Python.

names6 = ["bandar","khaled","salem"]
print(type(names6))

print("8----------------------------------------------------")
#Question 8 — List: Index
#Create a list containing four names. Print the index number of the third name using Python.

names7 = ["bandae","khaled","salem","bawazir"]

print(names7 [2])

print("9----------------------------------------------------")
#Question 9 — Tuple: Creating a Tuple
#Create a tuple containing three names, then print the tuple.
names8 = ("bandar","khaled","salem")
print(names8)
print(type(names8))

print("10----------------------------------------------------")
#Question 10 — Tuple: Accessing Elements
#Create a tuple containing four names. Print the first name and the third name from the tuple.

names9 = ("bandar","boke",'bookz','bndori')
print (names9[0])
print (names9[2])

print("11----------------------------------------------------")

#Question 11 — Dictionary: Creating a Dictionary
#Create a dictionary for a student containing:
#their name
#their age
#their university
#Then print the dictionary.

student = {
    "name":"bandar khaled bawazir",
    "age":23,
    "university":"city"
}

print(student)

print("12----------------------------------------------------")
#Question 12 — Dictionary: Accessing Values
#Using your student dictionary, print only the student’s university.

print(student["university"])

print("13----------------------------------------------------")
#Question 13 — Dictionary: Changing Values
#Using your student dictionary, change the student’s age from 23 to 25, then print the dictionary.
student ["age"] = 25
print(student["age"])

print("14----------------------------------------------------")
#Question 14 — Dictionary: Adding Elements
#Using your student dictionary, add a new key called "major" with the value "Computer Science", then print the whole dictionary.
student ["major"] = "computer science"
print(student)

print("15----------------------------------------------------")
#Question 15 — Dictionary: keys()
#Using your student dictionary, print all the keys in the dictionary.

print(student.keys())

print("16----------------------------------------------------")
#Question 16 — Dictionary: values()
#Using your student dictionary, print all the values in the dictionary.

print(student.values())

print("17----------------------------------------------------")
#Question 17 — Dictionary: Removing Elements — del
#Using your student dictionary, remove the "major" key from the dictionary using del, then print the whole dictionary.

del student ["major"]
print(student)

print("18----------------------------------------------------")
#Question 18 — List Syntax []
#Create a list of three names using the correct list syntax, then print the list.
names_student = ["bandar","khaled","salem"]
print(names_student)

print("19----------------------------------------------------")
#Question 19 — Tuple Syntax ()
#Create a tuple of three names using the correct tuple syntax, then print the tuple.
names_members = ("bandar","khaled","bawazir")
print(names_members)


print("20----------------------------------------------------")
#Question 20 — Dictionary Syntax {}
#Create a dictionary containing a student’s name and age using the correct dictionary syntax, then print the dictionary.

student_uni = {
    "name": "bandar",
    "age": 23
}

print(student_uni)
