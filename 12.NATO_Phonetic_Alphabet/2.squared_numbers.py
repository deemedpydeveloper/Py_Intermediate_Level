# Create a squared numbers list using list comprehension method.

numbers = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [pow(number, 2) for number in numbers]
print(squared_numbers)