"""Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin
 form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed
 (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules. """
import re


string = input("Enter a string to be pig latinated: ")
if string[0] in ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(string + "ay")
else:
    exponent = re.findall(r'^[^aeiouAEIOU]+([aeiouAEIOU]\w*)', string)
    mantisa = re.findall(r'(^[^aeiouAEIOU]+)[aeiouAEIOU]\w*', string)
    print( exponent[0].capitalize() + mantisa[0].lower() + "ay" )
