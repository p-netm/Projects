__problem_statement__ = "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” " \
                        "instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples " \
                        "of both three and five print “FizzBuzz”"


def fizz_buzz():
    for number in range(1, 101):
        print(inside_fizz_buzz(number))


def inside_fizz_buzz(arg):
    if arg % 3 == 0 and arg % 5 == 0:
        return 'FizzBuzz'
    elif arg % 3 == 0:
        return 'Fizz'
    elif arg % 5 == 0:
        return 'Buzz'
    else:
        return arg

fizz_buzz()