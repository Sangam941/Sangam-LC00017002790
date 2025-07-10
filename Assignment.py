# Python String Practice Questions

# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]
s = "PythonPractice"

print(s[1])
print(s[-3:])
print(s[2:7])

# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.
string = "developer"
print(string[::-1])

# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count+= 1
    return count

print(count_vowels("Hello World"))

# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()  # Remove spaces and convert to lowercase
    return cleaned == cleaned[::-1]

is_palindrome_result = is_palindrome("A man a plan a canal Panama")
print(is_palindrome_result)

# 5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"

text = "   hello world! welcome to Python.   "
cleaned_text = text.strip().title().replace("Python", "Programming")
print(cleaned_text)


# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

longest_word_result = find_longest_word("The quick brown fox jumped over the lazy dog")
print(longest_word_result)

# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

s1 = "Py"
s2 = "thon"
print(s1 + s2)  
print(s1 * 3)   
print("y" in s1)  

# 8. Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

remove_duplicates_result = remove_duplicates("programming")
print(remove_duplicates_result)

# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
anagram_result = are_anagrams("listen", "silent")
print(anagram_result)

# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

word_frequency_result = word_frequency("Hello world hello")
print(word_frequency_result)
