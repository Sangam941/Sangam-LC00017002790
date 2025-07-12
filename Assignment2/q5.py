# 5. Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))