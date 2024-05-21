import sys

def is_int(str) -> bool:
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

try:
    n = len(sys.argv)

    assert n != 1, "AssertionError: no argument is provided"
    assert n < 3, "AssertionError: more than one argument is provided"

    value = sys.argv[1]

    assert is_int(value), "AssertionError: argument is not a number"

    if int(value) % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

except AssertionError as e:
    print(e)