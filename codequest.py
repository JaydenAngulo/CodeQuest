# Problem 1:

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

# Problem 2:

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

# Problem 3:

cases = int(input())
missing = []

for _ in range(cases):
    N = int(input())
    numbers = [int(s) for s in input().split()]
    answers = list(range(1, N + 1))
    for i in answers:
        if i not in numbers:
            missing.append(int(i))

answer_iterator = iter(missing)

for _ in range(cases):
    print(next(answer_iterator))