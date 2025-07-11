#takes a secret word as input (without spaces)

secret = input("Enter your secret word:- ")
print(secret.replace(" ",""))

# replace all the vowels with *
vowels = "aeiouAEIOU"
for vowel in vowels:
    secret = secret.replace(vowel, "*")
print(secret)

# reverse the entire string
print(secret[::-1])

# then shift each letter 2 places ahead in the alphabet (wrap around if needed , e.g.., y -> a, z -> b)
