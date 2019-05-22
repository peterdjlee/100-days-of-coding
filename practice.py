# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they 
# will turn 100 years old.

# print('Please enter your name:')
# name = input()
# print('Please enter your age:')
# age = int(input())

# yearWhenHundred = str(2019 + (100 - age))
# print(name + ', you\'re going to turn 100 in the year ' + yearWhenHundred)

################################################################################
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an 
# even / odd number react differently when divided by 2?

# print('Please enter a number:')
# num = int(input())

# if num % 2 == 0:
#     print(str(num) + ' is even')
# else:
#     print(str(num) + ' is odd')

################################################################################
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for num in a:
#     if num < 5:
#         print(num)

#################################################################################
# Let’s say I give you a list saved in a variable: 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and makes a new list that has only 
# the even elements of this list in it.

# b = [x for x in a if x % 2 == 0]
# print(b)
