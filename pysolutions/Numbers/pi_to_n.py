"""
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go."""
import math

def put_precision(constant):
    precision = (input("Input your chosen precision level: "))
    limit = 20
    if not precision.isdigit():
        raise ValueError("Unrecognized data format")
    elif int(precision) > limit:
        print("Precision bypassed the limit")
    else:
        precision = int(precision)
        print(round(constant, precision))

if __name__ == "__main__":
    put_precision(math.pi)
