# # Write a recursive function to calculate the sum of first 'n' natural numbers.
# def sumOfNaturalNos(no):
#     if no == 0:
#         return 0
#     return no + sumOfNaturalNos(no - 1)


# no = int(input("Find Sum of any Postive number: "))
# sum = sumOfNaturalNos(no)
# print("Sum is 'n th' number is", sum)


# # Write a recursive function to print all elements in a list. (Hints: Use list & index as parameters.)
# def printList(listData, index=0):
#     if index == len(listData):
#         return
#     print(listData[index])
#     printList(listData, index + 1)


# fruits = ["Mango", "Litchi", "Apple", "Banana"]
# printList(fruits)
