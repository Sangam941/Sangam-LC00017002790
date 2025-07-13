# 10. Accept a list of numbers and remove all duplicate values

numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, numbers.split()))
unique_numbers = list(set(numbers_list))
print("List after removing duplicates:", unique_numbers)