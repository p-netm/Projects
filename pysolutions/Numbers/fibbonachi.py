"""a number and have the program generate the Fibonacci sequence to that number or to the Nth number. """

input_choice = input("Chosen limit: ")
first = 1
second = 1
counter = 0
print(0, 1, 1, end=", ")
while counter < int(input_choice):
    first, second = second, first + second
    print(second, end=", ")
    counter += 1

    # incomplete