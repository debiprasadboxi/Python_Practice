# Recursion:
# When a function calls itself repeatedly until a certain condition is met, it is called recursion.


# # Example 1: Print n to 1 backwards
# def show(n):
#     # Below condition called Base Case, which is the condition that stops the recursion.
#     if n == 0:
#         return
#     print(n)
#     show(n - 1)
#     # print("END")


# show(5)  # 5, 4, 3, 2, 1


# Example 2: Returns n factorial 'n!'
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


no = int(input("Enter the Number to find Factorial: "))
fact = factorial(no)
print("Factorial of", no, "is = ", fact)
