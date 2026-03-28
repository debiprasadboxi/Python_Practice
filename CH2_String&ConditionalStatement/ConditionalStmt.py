# Conditional Statements
# Syntex: if(condition):
#         statment1
#     elif(condition):
#         statmenet2
#     else:
#         statementN;

# Example 1
# age = 24
# if(age>=18):
#     print("Can Vote ")
#     print("Can Drive")

# Example 2
# light = "green"
# if light == "red":
#     print("STOP")
# elif light == "green":
#     print("GO")
# elif light == "yellow":
#     print("LOOK")
# else:
#     print("Light is Broken")

# print("End of Code")

# Example 3
# Grade students based on marks
# marks>=90,grade A; 90>marks>=80,grade=B
# 80>marks>=70,grade=C;# 70>marks,grade=D

# marks = int(input("Student Marks :"))
# if marks >= 90:
#     # print("Grade A")
#     grade = "A"
# elif marks < 90 and marks >= 80:
#     # print("Grade B")
#     grade = "B"
# elif marks < 80 and marks >= 70:
#     # print("Grade C")
#     grade = "C"
# else:
#     # print("Grade D")
#     grade = "D"
# print("Grade of the student ->", grade)

# Example 4
# Nesting
age = int(input("Enter Age :"))
if age >= 18:
    if age >= 80:
        print("Can't Drive")
    else:
        print("Can Drive")
else:
    print("Cann't Drive")
