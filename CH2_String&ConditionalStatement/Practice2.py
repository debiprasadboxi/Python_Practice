# 1 WAP to check if a number entered by the user is odd or even

# number = int(input("Enter a Number:"))
# if number % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")


# 2 WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))
num3 = int(input("Enter 3rd Number:"))
num4 = int(input("Enter 4th Number:"))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("First Number is Greatest:", num1)
elif num2 > num3 and num2 > num4:
    print("Second Number is Greatest:", num2)
elif num3 > num4:
    print("Third Number is Greatest:", num3)
else:
    print("Forth Number is Greatest:", num4)


# 3 WAP to check if a number is a multiple of 7 or not.

# number = int(input("Enter a Number:"))
# if number % 7 == 0:
#     print("Number is Multiple by '7'")
# else:
#     print("Number is not Multiple by '7'")
