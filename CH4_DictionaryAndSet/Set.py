## Set in Python
## Set is the collection of the unordered items.
## Each element in the set must be unique and immutable (cannot be changed).
## But set itself is mutable, we can add or remove elements from the set.
## Syntex:
## set = {element1, element2, element3, ...}

## Example1:
# my_set = {1, 2, 3, 4, 5, 2, "hello", "hi"}
# print(my_set)
# print(type(my_set))
# print(len(my_set))


## Example2:
## creae a empty set and add some element in it

# my_set = set()  # this is the way to create a empty set
# my_set1 = {}  # this is not a set, this is a empty dictionary
# print(my_set)
# print(type(my_set))
# print(my_set1)
# print(type(my_set1))

## Example3:
## Set Methods1:
## add() method is used to add an element in the set
# my_set = {1, 2, 3}
# print(my_set)
# my_set.add(4)
# print(my_set)
# my_set.add("Hello")
# tuple = (5, 6)
# my_set.add(tuple)
# # this will raise a type error because dictionary is not hashable and cannot be added to the set
# dict = {"name": "DebiBoxi", "age": 35}
# my_set.add(dict)
# # this will raise a type error because list is not hashable and cannot be added to the set
# list = [7, 8]
# my_set.add(list)
# print(my_set)

## Set Methods2:
## remove() method is used to remove an element from the set.
## If the element is not present in the set, it raises a key error.

# my_set = {1, 2, 3, 4}
# print(my_set)
# my_set.remove(3)
# print(my_set)
# my_set.remove(5)  # this will raise a key error because 5 is not present in the set

## Set Methods3:
## clear() method is used to remove all the elements from the set.
# my_set = {1, 2, 3, 4}
# print(len(my_set))
# my_set.clear()
# print(len(my_set))

## Set Methods4:
## pop() method is used to remove and return an arbitrary element from the set.
# my_set = {"world", "test", "hello", "hi"}
# print(my_set)
# print(my_set.pop())
# print(my_set)


## Set Methods5:
## union() method is used to return a new set that contains all the elements from both sets.
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 1, 6, 7, 8}
my_set3 = my_set1.union(my_set2)
print(my_set3)

## Set Methods6:
## intersection() method is used to return a new set that contains only the elements that are present in both sets.
my_set4 = {1, 2, 3, 4, 5, "hello"}
my_set5 = {4, 1, 6, 7, 8, "hello"}
my_set6 = my_set4.intersection(my_set5)
print(my_set6)
