# Problem 1-5 points:

# n = int(input())
# list = []

# def letters_after_vowels(text):
#     vowels = "aeiou"
#     result = ""

#     for i in range(len(text)-1):
#         if text[i] and text[i - 1] in vowels:
#             continue
#         if text[i] in vowels:
#             result += text[i + 1]
#     return result

# for _ in range(n):
#     user_input = input()
#     answer = letters_after_vowels(user_input)
#     list.append(answer)

# answer_iterator = iter(list)

# for _ in range(n):
#     print(next(answer_iterator))

# Problem 2-5 points:

# n = int(input())
# list = []

# for _ in range(n):
#     line = input()
#     numbers = line.split()
#     waste = int(numbers[0]) / (int(numbers[1]) - int(numbers[2])) * int(numbers[2])
#     list.append(int(round(waste)))

# answer_iterator = iter(list)

# for _ in range(n):
#     print(next(answer_iterator))

# Problem 3-25 points:

# cases = int(input())
# missing = []

# for _ in range(cases):
#     N = int(input())
#     numbers = [int(s) for s in input().split()]
#     answers = list(range(1, N + 1))
#     for i in answers:
#         if i not in numbers:
#             missing.append(int(i))

# answer_iterator = iter(missing)

# for _ in range(cases):
#     print(next(answer_iterator))

# Problem 4-50 points:

n = int(input())

morse_to_letter = {}
letter_to_morse = {}

for _ in range(26):
    code = input().split(maxsplit=1)
    letter = code[0]
    morse = code[1]
    letter_to_morse[letter] = morse
    morse_to_letter[morse] = letter

# phrase = input()
# encoded_phrase = []

# for char in phrase:
#     if char == " ":
#         encoded_phrase.append("      ")
#     else:
#         encoded_phrase.append(letter_to_morse[char])

# print('   '.join(encoded_phrase))

coded_message = input()
decoded_phrase = []
coded_letter = []

for i, ch in enumerate(coded_message):
    if ch != " " and coded_message[i+1] == " " and coded_message[i+2] == " " and coded_message[i+3] == " " and coded_message[i+4] == " ":
        coded_letter.append(ch)
        morse_letter = " ".join(coded_letter)
        answer_letter = morse_to_letter[morse_letter]
        decoded_phrase.append(answer_letter)
        coded_letter.clear()
        print(decoded_phrase)
    if ch == " " and coded_message[i+1] == " " or ch == " " and coded_message[i-1] == " ":
        if coded_message[i-2] == " " and coded_message[i-2] == " ":
            decoded_phrase.append(" ")
            continue
    else:
        coded_letter.append(ch)
    if coded_message[i] and coded_message[i+1] and coded_message[i+2] and coded_message[i+3] == " " or i == len(coded_message) - 1:
        coded_letter.append(ch)
        morse_letter = " ".join(coded_letter)
        answer_letter = morse_to_letter[morse_letter]
        decoded_phrase.append(answer_letter)
        coded_letter.clear()
        print(decoded_phrase)

print(decoded_phrase)