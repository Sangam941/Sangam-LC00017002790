# 8. Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.

even_numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
    
print("Even numbers:", even_numbers)