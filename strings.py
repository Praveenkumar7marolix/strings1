def remove_character(input_string, char_to_remove):
    return input_string.replace(char_to_remove, '')

input_string = "Hello, world!"
char_to_remove = "o"
result = remove_character(input_string, char_to_remove)
print(result)
def is_palindrome(input_string):
    clean_string = input_string.lower().replace(" ", "")
    return clean_string == clean_string[::-1]

input_string = "racecar"
if is_palindrome(input_string):
    print("Palindrome")
else:
    print("Not a Palindrome")
def check_vowel_or_consonant(character):
    vowels = "aeiou"
    if character.lower() in vowels:
        return "Vowel"
    else:
        return "Consonant"

character = input("Enter a character: ")
print(check_vowel_or_consonant(character))
def replace_spaces(input_string, replacement_char):
    return input_string.replace(" ", replacement_char)

input_string = "Hello world, how are you?"
replacement_char = "_"
result = replace_spaces(input_string, replacement_char)
print(result)
def count_characters(input_string):
    alphabets = digits = special_chars = 0
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1
    return alphabets, digits, special_chars

input_string = "Hello123!@"
a_count, d_count, s_count = count_characters(input_string)
print("Alphabets:", a_count)
print("Digits:", d_count)
print("Special Characters:", s_count)
def remove_spaces(input_string):
    return input_string.replace(" ", "")

input_string = "Hello   world!  How   are  you?"
result = remove_spaces(input_string)
print(result)
import re

def sum_integers_in_string(input_string):
    numbers = re.findall(r'\d+', input_string)
    return sum(map(int, numbers))

input_string = "I have 3 apples and 5 bananas, and 2 oranges."
total_sum = sum_integers_in_string(input_string)
print("Sum of integers:", total_sum)
def remove_repeated_chars(input_string):
    unique_chars = []
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

input_string = "mississippi"
result = remove_repeated_chars(input_string)
print(result)
def remove_repeated_chars(input_string):
    unique_chars = []
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

input_string = "mississippi"
result = remove_repeated_chars(input_string)
print(result)
def remove_repeated_chars(input_string):
    unique_chars = []
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

input_string = "mississippi"
result = remove_repeated_chars(input_string)
print(result)
def count_occurrence(input_string, target_char):
    return input_string.count(target_char)

input_string = "hello world"
target_char = "l"
occurrences = count_occurrence(input_string, target_char)
print(f"'{target_char}' appears {occurrences} times.")
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("Anagrams")
else:
    print("Not Anagrams")
def custom_sort(input_string):
    alphabets = []
    digits = []
    for char in input_string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isdigit():
            digits.append(char)
    sorted_string = ''.join(sorted(alphabets) + sorted(digits))
    return sorted_string

input_string = "a3b1c2"
sorted_result = custom_sort(input_string)
print(sorted_result)