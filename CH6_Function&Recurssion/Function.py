# Function


def sum(a, b):
    return a + b


def average_num(a, b, c):
    sum = a + b + c
    average = sum / 3
    return average


def percentage(number, percentage):
    per = number * (percentage / 100)
    return per


print("Sum of 2 number: ", sum(1, 2))
print("Average of 3 numbers :", average_num(32, 31, 30))
print("Percentage of a Number :", percentage(455, 5))


## Experiement of print method where sep and end variable check
print("Hello", "World!", sep="-", end=" ")
print("Sandeep")
