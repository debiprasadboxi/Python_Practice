## Store following word meanings in a python dictonary:
## table: "a piece of furniture", "list of facts & figures"
## cat: "a small animal"

# you can store this value in 2 ways
# either in List or Tuple
# table_meaning_list = {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of facts & figures"],
# }
# print(table_meaning_list)
# table_meaning_tuple = {
#     "cat": "a small animal",
#     "table": ("a piece of furniture", "list of facts & figures"),
# }
# print(table_meaning_tuple)


## You are given a list of subjects for students. Assume one classroom is required for
## 1 subject. How many classrooms are needed by all students.
## "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
# put this value into set object and find the length
# list_subjects = {
#     "python",
#     "java",
#     "C++",
#     "python",
#     "javascript",
#     "java",
#     "python",
#     "java",
#     "C++",
#     "C",
# }
# print("Required Class Room for all Subject is: ", len(list_subjects))


## WAP to enter marks of 3 subjects from the user and store them in a dictionary.
## Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}
# chemistryMarks = float(input("Enter mark of Chemistry :"))
# marks.update({"chemistry": chemistryMarks})
# physicsMarks = float(input("Enter mark of Physics :"))
# marks.update({"physics": physicsMarks})
# mathsMarks = float(input("Enter mark of Maths :"))
# marks.update({"maths": mathsMarks})

# print(marks)
# print("chemistry marks: ", marks.get("chemistry"))
# print("physics marks: ", marks.get("physics"))
# print("maths marks: ", marks.get("maths"))


## Figure out a way to store 9 & 9.0 as seperate values in the set.
## (You can take help of built-in data type)

set_Value = set()
set_Value.add(9)
set_Value.add("9.0")  # one possible solutation convert to String
print(set_Value)
# another way to store both 9 and 9.0
values = {("float", 9.0), ("int", 9)}
print(values)
