# 6. Accept a string and check whether it is a palindrome or not (same forward and backward).

string = input("Enter a string: ")
is_palindrome = string == string[::-1]
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")