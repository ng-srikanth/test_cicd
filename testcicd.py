def count_even_odd(n):
    """
    Count the number of even and odd numbers up to n (exclusive).

    Args:
        n (int): The upper limit for the range of numbers.

    Returns:
        tuple: A tuple containing the count of even numbers and the count of odd numbers.

    Examples:
        >>> count_even_odd(10)
        (5, 5)

        >>> count_even_odd(20)
        (10, 10)

        >>> count_even_odd(1)
        (1, 0)

        >>> count_even_odd(0)
        (0, 0)
    """
    count_even = 0
    count_odd = 0
    for i in range(n):
        if i%2 == 0:
            count_even += 1
        elif i%2 != 0:
            count_odd+=1
        else:
            pass
    return count_even,count_odd

count_even_odd(100)