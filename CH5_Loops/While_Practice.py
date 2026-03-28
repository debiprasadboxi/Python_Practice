## print number from 1 to 100
# number = 1
# while number <= 100:
#     print(number)
#     number += 1


# # print numbers from 100 to 1
# number = 100
# while number >= 1:
#     print(number)
#     number -= 1


# # print the multiplication table of a number 'n'.
# number = int(input("Enter a Number for Multiplication: "))
# count = 1
# while count <= 10:
#     print(number, "X", count, "=", number * count)
#     count += 1


# # print the elements of the following list using a loop:
# # [1,4,9,16,25,36,49,64,81,100]
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# leng = len(list) - 1
# i = 0
# while i <= leng:
#     print(list[i])
#     i += 1


# search for a number x in the tuple using loop.
tuple = (1, 5, 2, 4, 9, 88, 43, 12, 55)
x = int(
    input("From the given tuple serahc the number '(1, 5, 2, 4, 9, 88, 43, 12, 55)': ")
)
leng = len(tuple) - 1
# valueFound = False

while leng >= 0:
    if tuple[leng] == x:

        print("Match the tuple value at postion :", leng + 1)
        # valueFound = True
        break
    else:
        print("Finding...")
    leng -= 1

else:  # this else block is for while loop, Not for if statement, This is part of while loop syntax incling else block.
    print("No value Found")


# ::Syntex::
# while condition:
# loop body
# else:  # runs if the loop ends normally (condition becomes False)
