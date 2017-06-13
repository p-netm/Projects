"""Check if Palindrome - Checks if the string entered by the user is a palindrome.
 That is that it reads the same forwards as backwards like “racecar” """
import re
string = input("Enter text to be checked if Palindrome: ")
string_half = len(string) // 2
if len(string) % 2 == 0:
    first_part = string[0:string_half]
    second_part = first_part[::-1]
    pattern = first_part + second_part
elif len(string) % 2 == 1:
    first_part = string[0: string_half]
    second_part = first_part[::-1]
    pattern = first_part + '\w' + second_part

if (bool(re.search(pattern, string))):
    print("{} is indeed a Palindrome".format(string.capitalize()))
else:
    print("{} is not a Palindrome". format(string.capitalize()))