# 9. Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0, 1
fibonacci_sequence = []
for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b
print("Fibonacci sequence:", fibonacci_sequence)