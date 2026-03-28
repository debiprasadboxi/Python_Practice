# Tuples In Python
# A built-in data type that lets us create immutable sequences of values.
# It is almost same same List but Tuples is immutable like String

# tuple = (1, 3, 2, 5, 9)
# print(tuple)

# tuple = (1, 2, 3, 4)
# if you treat bracket value as tuple then add ',' aftr value. else it will treat as int type in this given example
# if tuple variable has multiple values like (1,2,3,4) then ',' is optional at end of the value, else we need to add ',' in single value
# print(tuple)
# print(type(tuple))
# print(tuple[1 : tuple.__len__()])

# Methods of tuple
# count and index
# tuple = (1, 2, 3, 4, 2, 5, 6)
# print(tuple.count(2))  # it will return the count of element in tuple
# print(tuple.index(2))  # it will return the index of 1st occurance of element


# Tuple Practices Questions
# WAP to ask the user to enter names of their 3 favorite movies and store then in a list.
# listMovies = []
# listMovies.append(input("Enter the name of your favorite movie: "))
# listMovies.append(input("Enter the name of your favorite movie: "))
# listMovies.append(input("Enter the name of your favorite movie: "))

# print("Your favorite movies are:", listMovies)


# WAP to check if a list contains a palindrome of elements.(hints: use copy() method))
# palList = [1, 2, "Hello", 2, 1]
# palListCopy = palList.copy()
# palListCopy.reverse()
# if palList == palListCopy:
#     print("The list is palindrome")
# else:
#     print("The list is not palindrome")


# WAP to count the number of student with the "A" grade in the following tuple.
# gradesTuple = ("C", "D", "A", "A", "B", "B", "A")
gradeTuple = ("C", "D", "A", "A", "B", "B", "A")
print(gradeTuple.count("A"))


# Store the above tuple in a list and sort them from A to D.
# Convert a tuple to a list (this is what you asked):
my_list = list(gradeTuple)
print("Tuple:", gradeTuple)
print("Converted List:", my_list)
my_list.sort()
print("Sorted List:", my_list)
