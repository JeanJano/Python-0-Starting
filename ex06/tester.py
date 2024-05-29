from ft_filter import ft_filter


def myFunc(x):
    """
    Check if a given age is 18 or older.

    Parameters:
    x (int): The age to check.

    Returns:
    bool: True if the age is 18 or older, False otherwise.
    """
    if x < 18:
        return False
    else:
        return True


def main():
    """
    The function uses two methods to filter the ages: the built-in filter
        function and a custom function called ft_filter.
    The results of both methods are printed to the console.

    Returns:
    None
    """

    print("\nbuilt-in doc function")
    print(filter.__doc__)

    print("\nCustom doc function")
    print(ft_filter.__doc__)

    ages = [5, 12, 17, 18, 24, 32]

    # built-in filter function

    adults = filter(myFunc, ages)
    print("Built-in filter function:")
    print(adults)
    print(list(adults))

    filtered = filter(lambda x: x > 0, [1, -1, 2, -2, 3, -3])
    print(list(filtered))  # Output: [1, 2, 3]

    funct = filter(None, [1, 0, 2, 0, 3, 0])
    print(list(funct))  # Output: [1, 2, 3]

    iter = filter(myFunc, [])
    print(list(iter))  # Output: []

    # custom ft_filter function

    print("\nCustom ft_filter function:")
    adults1 = ft_filter(myFunc, ages)
    print(adults1)
    print(list(adults1))

    # lambda function to filter positive numbers
    # take x as input and return true if x > 0 else false
    filtered = ft_filter(lambda x: x > 0, [1, -1, 2, -2, 3, -3])
    print(list(filtered))  # Output: [1, 2, 3]

    funct1 = ft_filter(None, [1, 0, 2, 0, 3, 0])
    print(list(funct1))  # Output: [1, 2, 3]

    iter1 = ft_filter(myFunc, [])
    print(list(iter1))  # Output: []


if __name__ == "__main__":
    main()
