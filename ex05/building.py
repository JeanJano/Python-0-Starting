import sys


def ft_count(str):
    """
    Count the number of upper case letters, lower case letters, punctuation
    marks, spaces, and digits in a string.

    Parameters:
    str (str): The string to be analyzed.

    Returns:
    None
    """
    upper = 0
    lower = 0
    ponct = 0
    space = 0
    digit = 0

    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace() or i == '\n':
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            ponct += 1

    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(ponct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


def main():
    """
    Main function that reads input from the command line or standard input and
    calls the ft_count function.

    If one argument is provided in the command line, it is passed to the
    ft_count function.
    If no arguments are provided, the function reads from the standard
    input and passes the input to the ft_count function.
    If more than one argument is provided, an AssertionError is raised.

    Returns:
    None
    """
    try:
        n = len(sys.argv)

        assert n < 3, "AssertionError: more than one argument is provided"

        if (n == 1):
            message = sys.stdin.readline()
            ft_count(message)

        if (n == 2):
            ft_count(sys.argv[1])

    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
