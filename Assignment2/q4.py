# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number: "))
multiplication_table(number)