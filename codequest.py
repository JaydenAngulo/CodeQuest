# Problem 1:

def letters_after_vowels(text):
    vowels = "aeiou"
    result = ""

    for i in range(len(text)-1):
        if text[i] in vowels:
            result += text[i + 1]
    return result

user_input = input("Enter a string: ")
output = letters_after_vowels(user_input)
print(output)