## LOOPS in Python
## Loops are used for sequential traversal. For Traversing a sequence (like a list, tuple, string)
## we can use for loop.

# Syntex of for loop
# for variable in sequence:
#     statement(s)

## Example1: List
# list = [1, 2, 3]
# for elements in list:
#     print(elements)

## Example1: tuple
# tuple = ("hello", "worlds", "Test", "data")
# for tup in tuple:
#     print(tup)

## Example1: string
# strData = "My Name is Debi Boxi"
# for char in strData:
#     if char == "z":
#         break
#     print(char)
# else:
#     print("END...")

## Method 1: range()
## Range functions returns a sequence of numbers, starting from 0 by default, and increments by
## 1(by default), and stops a specified number
## Syntex: range(start?, stop, step?)
# # Example1:
# for i in range(5):
#     print(i)
# else:
#     print("========")

# # Example2:
# for j in range(1, 5):  # '1' is optional if not deafult value is '0'
#     print(j)
# else:
#     print("========")

# # Example3:
# for k in range(1, 10, 2):  # '1' and '2' is optional if not deafult value is '0' and '1'
#     print(k)
# else:
#     print("========")

# Example : Find even numbers using range function:
# for even in range(2, 50, 2):
#     print(even)

## pass Statment
## pass is a null statment that does nothing. It is used as a placeholder for future code.
# for el in range(10):
# pass
for elem in range(5):
    pass
if elem < 5:
    pass
print("Some useful work")
