"""
asg0-onlytesting

The goal of this first lab is testing your setup. The submission will
be graded but it will not count for the final assessment.

Your task is to implement the functions below. See the /docstring/ of
the function for the purpose of the function.

The function /docstring/s contain also real examples and usage of the
functions. You can run these examples by executing the script from
command line:

python3 asg0.py

Note that the unit tests may contain different tests.
"""


def squares():
    """
    Returns a list of the squares of the first ten natural
    numbers. Try using list comprehensions.

    Parameters
    ----------
    None
    
    Returns
    -------
    list(int)
        A list of integer numbers

    Examples
    --------
    
    >>> squares()
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [n**2 for n in range(1,11)]



def multiples(arg):
    """
    Returns a list of numbers in the range [0,100] that are multiples of arg. 

    Parameters
    ----------
    arg : int
        the multiplier

    Returns
    -------
    list(int)
        Description of return value

    Examples
    --------
    
    >>> multiples(4)
    [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]
    """
    return [n for n in range(0,101) if n%arg == 0]



def sum_lists(arg1, arg2):
    """
    Return a list that is the element-wise sum of the elements of the
    two lists of equal size passed as arguments.

    Lists can be used to represent vectors of numbers as in Linear
    Algebra. However, as you can test in a python shell, for example,
    `ipython`, the effect the operator `+` is not really the expected
    one in linear algebra.

    Parameters
    ----------
    arg1 : list(numeric)
        a list of numbers
    arg2 : list(numeric)
        a list of numbers

    Returns
    -------
    list(int)
        a list containing the element-wise sum of the two lists

    Raises
    ------
    ValueError
        If the two lists are not of equal size
        that are relevant to the interface.


    Examples
    --------
    
    >>> va = [1, 1, 1]
    >>> vb = [2, 2, 2]
    >>> sum_lists(va,vb)
    [3, 3, 3]
    """
    if (len(arg1) != len(arg2)):
        raise ValueError("List arguents of different lenghts")
    else:
        return [arg1[i] + arg2[i] for i in range(len(arg1))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


