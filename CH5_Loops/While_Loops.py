## Loops aare used to repeat a block of code multiple times. In Python,
# there are two main types of loops: FOR loops and WHILE loops.
## While Loops
## Syntax:
## while condition:
## code block
## Example:

# count = 5
# i = 1
# while i <= count:
#     print("Debi Boxi")
#     i += 1
# print("value of 'i':", i)

## Methods of while loops:
## 1. break: Used to exit the loop immediately when a certain condition is met.
## Example: Using BREAK
# i = 1
# while i <= 5:
#     print("Value of 'i' :", i)
#     if i == 3:
#         break # Exit the loop when 'i' is equal to 3
#     i += 1
# print("END OF LOOP")

## 2. continue: Used to skip the current iteration and move to the next iteration of the loop.
## Example: Using CONTINUE
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue  # Skip the rest of the code block and move to the next iteration
#     print("Value of 'i' :", i)
#     i += 1


## 3. else: Used to execute a block of code when the loop condition becomes false
## Example: Using ELSE
# i = 1
# while i <= 5:
#     print("Value of 'i' :", i)
#     i += 1
# else:
#     print("Loop has ended. 'i' is now greater than 5.")
