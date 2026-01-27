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

# Problem 4-50 points(unfinished):

# n = int(input())

# morse_to_letter = {}
# letter_to_morse = {}

# for _ in range(26):
#     code = input().split(maxsplit=1)
#     letter = code[0]
#     morse = code[1]
#     letter_to_morse[letter] = morse
#     morse_to_letter[morse] = letter

# phrase = input()
# encoded_phrase = []

# for char in phrase:
#     if char == " ":
#         encoded_phrase.append("      ")
#     else:
#         encoded_phrase.append(letter_to_morse[char])

# print('   '.join(encoded_phrase))

# coded_message = input()
# decoded_phrase = []
# coded_letter = []

# for i, ch in enumerate(coded_message):
#     if ch != " " and coded_message[i+1] == " " and coded_message[i+2] == " " and coded_message[i+3] == " " and coded_message[i+4] == " ":
#         coded_letter.append(ch)
#         morse_letter = " ".join(coded_letter)
#         answer_letter = morse_to_letter[morse_letter]
#         decoded_phrase.append(answer_letter)
#         coded_letter.clear()
#         print(decoded_phrase)
#     if ch == " " and coded_message[i+1] == " " or ch == " " and coded_message[i-1] == " ":
#         if coded_message[i-2] == " " and coded_message[i-2] == " ":
#             decoded_phrase.append(" ")
#             continue
#     else:
#         coded_letter.append(ch)
#     if coded_message[i] and coded_message[i+1] and coded_message[i+2] and coded_message[i+3] == " " or i == len(coded_message) - 1:
#         coded_letter.append(ch)
#         morse_letter = " ".join(coded_letter)
#         answer_letter = morse_to_letter[morse_letter]
#         decoded_phrase.append(answer_letter)
#         coded_letter.clear()
#         print(decoded_phrase)

# print(decoded_phrase)

# Problem 5-40 points:

# tests = int(input())

# records = input().split()

# separator = ","

# old = int(records[0])

# new = int(records[1])

# old_phone = {}
# old_address = {}

# for _ in range(old):
#     old_info = input()
#     old_info_list = old_info.split(separator)
#     old_phone[old_info_list[0]] = old_info_list[1]
#     old_address[old_info_list[0]] = old_info_list[2]

# new_phone = {}
# new_address = {}

# for _ in range(new):
#     new_info = input()
#     new_info_list = new_info.split(separator)
#     new_phone[new_info_list[0]] = new_info_list[1]
#     new_address[new_info_list[0]] = new_info_list[2]

# old_names_list = list(old_phone.keys())
# new_names_list = list(new_phone.keys())

# info = []

# for item in old_names_list:
#     if item not in new_names_list:
#         info.append(f"{item} DELETED")
#     else:
#         if old_phone[item] != new_phone[item] and old_address[item] != new_address[item]:
#             info.append(f"{item} UPDATED BOTH")
#             continue
#         if old_phone[item] != new_phone[item]:
#             info.append(f"{item} UPDATED PHONE NUMBER")
#         if old_address[item] != new_address[item]:
#             info.append(f"{item} UPDATED ADDRESS")

# for item in new_names_list:
#     if item not in old_names_list:
#         info.append(f"{item} CREATED")

# info.sort()
# count = len(info)
# info_count = 0

# for _ in range(count):
#     print(info[info_count])
#     info_count += 1

# Problem 6-20 points:

tests = int(input())
separator = ","
employees = {}

for _ in range(tests):
    timestamps = input().split(separator)
    for _ in range(len[timestamps] - 1):
        if timestamps[0]
    employees[timestamps[0]]