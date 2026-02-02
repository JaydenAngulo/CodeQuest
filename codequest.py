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

# tests = int(input("").strip())
# separator = ","
# employees = []

# for case in range(tests):
#     timestamps = input("").strip()
#     employees.append(timestamps)
    
# for i in employees:
#     hours_list = i.split(',')
#     name = hours_list[0]
#     hours_list.pop(0)
#     total_hours = 0
#     total_minutes = 0
#     for day in hours_list:
#         hours_minutes = day.split(':')
#         hour = int(hours_minutes[0])
#         minutes = int(hours_minutes[1])
#         total_hours += hour
#         total_minutes += minutes
#         if total_minutes >= 60:
#             total_hours += 1
#             total_minutes -= 60
#     if total_hours == 1:
#         hour_plurality = "hour"
#     else:
#         hour_plurality = "hours"

#     if total_minutes == 1:
#         minute_plurality = "minute"
#     else:
#         minute_plurality = "minutes"

#     if total_hours == 0:
#         print(f"{name}={total_minutes} {minute_plurality}")
#         continue
#     if total_minutes == 0:
#         print(f"{name}={total_hours} {hour_plurality}")
#     else:
#         print(f"{name}={total_hours} {hour_plurality} {total_minutes} {minute_plurality}")

# Problem 7-25 points:

tests = int(input())

for i in range(tests):
    info = input().split()
    diameter = int(info[0])
    required_revolutions_per_wheel_rotation = int(info[1])
    required_power_per_motor_revolution = int(info[2])
    motor_revolutions_per_minute = int(info[3])
    available_motor_capacity = int(info[4])
    required_motor_voltage = int(info[5])
    required_distance = int(info[6])
    circumference = diameter * 3.14
    required_wheel_rotations = (required_distance * 100) / circumference
    total_required_motor_revolutions = required_revolutions_per_wheel_rotation * required_wheel_rotations
    total_required_power = required_power_per_motor_revolution * total_required_motor_revolutions
    contained_power = available_motor_capacity * required_motor_voltage
    total_time = round((required_distance * 100) / (total_required_motor_revolutions * motor_revolutions_per_minute), 4)
    answer = {}
    if contained_power >= total_required_power:
        answer[i] = f"Success {total_time}"
    else:
        answer[i] = "Fail"
    
print(answer[1])

for i in range(tests):
        print(answer.get(i))