import sys

def ft_count(str):
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
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        elif i == '\n':
            space += 1
        else:
            ponct += 1

    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(ponct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")

def read_until_eof():
    user_input = ''
    while True:
        try:
            user_input = sys.stdin.read()  # Read a single character
            # if char == '\x04':  # Ctrl-D (EOF) character
            #     print("je suis la")
            #     ft_count(user_input)
            #     break
            # user_input += char
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
    
    return user_input

def main():
    try:
        n = len(sys.argv)

        assert n < 3, "AssertionError: more than one argument is provided"

        if (n == 1):
            read_until_eof()

        if (n == 2):
            ft_count(sys.argv[1])

    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    main()