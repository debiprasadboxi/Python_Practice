## Print the elments of the following list using a loop:
## [1,4,9,16,25,36,49,64,81,100]
# listPrint = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for listData in listPrint:
#     print(listData)


## Search for a  number 'X' in this tuple using loop:
## [1,4,9,16,25,36,49,64,81,100]
# listSearch = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49, 16]
# x = int(
#     input("Enter search Value from given List '[1,4,9,16,25,36,49,64,81,100,49,16]' :")
# )
# indx = 0
# for searchValue in listSearch:
#     if searchValue == x:
#         print("Value Found at position: ", indx + 1)
#         break
#     indx += 1
# else:
#     print("Value Not Found")


# # Using for and range()
# # Print numbers from 1 to 100
# for num in range(1, 101):
#     print(num)


# # Print numbers from 100 to 1
# for num in range(100, 0, -1):
#     print(num)


# # Print the multiplication table of a  number 'n'
# n = int(input("Enter Number for multiplication table: "))
# for num in range(1, 11):
#     print(n, "X", num, "=", n * num)


## WAP to find the sum of first 'n' natural numbers.(Using While)
## First usecase using while
# n = int(input("Enter 'n'th number to find SUM: "))
# count = 1
# sum = 0
# while n >= count:
#     sum += count
#     count += 1
# print("Sum is :", sum)

## second usecase using for
# n = int(input("Enter 'n'th number to find SUM: "))
# sum = 0
# for ele in range(1, n + 1):
#     sum += ele
# print("Total of sum :", sum)


## WAP to find the factorial of first 'n' numbers.(Using For)
n = int(input("Enter Number to Find out factorial of 'n'th number "))
factorial = 1
for fact in range(n, 1, -1):  # or for fact in range (1, n+1)
    factorial *= fact
print("Factorial of  'n'th Number using For loop is   :", factorial)

factWhile = 1
i = 1
while i <= n:
    factWhile *= i
    i += 1
print("Factorial of  'n'th Number using While loop is :", factWhile)
