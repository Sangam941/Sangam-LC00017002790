# Q1: write a program to detect doule spaces in a string.
name = "sangam  singh  dhami"
double_spaces = name.count("  ")
print(f"Number of double spaces: {double_spaces}")

# Q2: write a program to replace double spaces with single space in a string.
name_with_single_space = name.replace("  ", " ")
print(f"String after replacing double spaces: '{name_with_single_space}'")


# Q3: write a program to format the followiing letter using escape sequence characters.
letter = "Dear Students,\n This python course is going well.\n thanks!"
print(letter)



