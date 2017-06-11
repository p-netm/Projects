""" Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found."""

string = input("Enter a string, and i will tell you how many vowels you have: ")
vowels = [char for char in string if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
print("".join(vowels))
print(len(vowels))
