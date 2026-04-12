# Default Parameters in Python
# Assign a default value to parameter, which is used when no argument is passed.


# Example:1
def cal_prod(a, b=2):  # b is a default parameter with default value 2
    print(a * b)
    return a * b


# Note: Default value should be assigned to the last parameter of the function, otherwise it will give an error.
# example: def cal_prod(a=2, b): # This will give an error because default parameter is not at the end of the parameter list.

cal_prod(3, 3)  # if there is no argument passed for b, it will take the default value 2
cal_prod(3)  # if there is no argument passed for b, it will take the default value 2
