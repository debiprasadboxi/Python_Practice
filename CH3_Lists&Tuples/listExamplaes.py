# #Lists in Python
# A built-in data type that stores set of values
# It can store elements of different types(int,float,string,etc.)

# marksList = [94.4, 87.5, 95.2, 66.4, 45.1]
# student = ["Karan", 85, "Delhi"]
# print(marksList)
# # print(type(marksList))
# # print(len(marksList))
# print(marksList[2])
# print(student)

# List is mutual
# student = ["Karan", 85.6, 17, "Delhi"]
# student[0] = "DebiPrasad"
# print("List Details:", student)

# List Slicing
# marks = [85, 94, 76, 63, 48]
# print(marks[1:4])

# ============================================#
# List Method
# append, sort, reverse, insert
# Append
# list = [2, 1, 3]
# print(list)
# list.append(4)
# print(list)

# Sort and Reverse
# list = [4, 2, 3, 5, 1]
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# Reverse only
# list = [2, 4, 3, 1, 6, 0]
# print(list)
# list.reverse()
# print(list)


# Insert
# list = [1, 3, 5, 6, 7]
# print(list)
# list.insert(1, 2)
# list.insert(3, 4)
# print(list)

# Remove:  remove the 1st occurance of element
list = [1, 3, 4, 5, 3]
# list.remove(3)
# print(list)

# POP will remove the element at index
listPop = [1, 3, 2, 4, 6, 5]
# listPop.pop(3)
# print(listPop)

# Adding 2 list
print(list.__add__(listPop))
