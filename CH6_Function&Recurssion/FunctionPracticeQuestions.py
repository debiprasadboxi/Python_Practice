# # 1. WAF to print the length of a list. (list is a parameter)
# def list_len(listData):
#     return len(listData)


# list_data = [1, 4, 3, 2, 9, 8, 6, 7, 4, 3, 6]
# list_heros = ["Thor", "Ironman", "Captain America", "Spiderman", "Shaktiman"]
# print("Length of the List is : ", list_len(list_data))
# print("Length of the List is : ", list_len(list_heros))


# # 2. WAF to print the elements of a list in a single line. (list is a parameter)
# def list_print(listData):
#     print("Print List in Single line :", end=" ")
#     for elements in listData:
#         print(elements, end=" ")


# list_single = ["Hi,", "I", "am", "Debi", "Prasad", "Boxi"]
# list_print(list_single)


# # 3. WAF to find the factorial of n. (n is a parameter)
# def fact_call(n):
#     fact = 1
#     for elements in range(1, n + 1):
#         fact *= elements

#     return fact


# n = int(input("Enter the 'n' number for find the Factorial: "))
# print("Factorial is:", fact_call(n))


# 4. WAF to convert USD to INR
def convert_usd2inr(usd, inr=94.59):
    return usd * inr


USD = float(input("Enter USD Amount: "))
print(USD, "USD=", convert_usd2inr(USD), "INR")
