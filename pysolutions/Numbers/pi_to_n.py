"""
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go."""
import math


precision = (input("Input your chosen precision level: "))
if not precision.isdigit():
    raise ValueError("Unrecognized data format")
else:
    precision = int(precision)
    print(round(math.pi, precision))
