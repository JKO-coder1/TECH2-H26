"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""


import numpy as np


def argmax(values):
    """
    Return the index of the maximum value in a collect

    Parameters
    ----------
    Values
        Seguence of values

    return
    ------
    imax : int
        Index of maximum
    """

    N = len(values)

    if N == 0:
        print('Not supported sequence')
        return

    imax = None
    # Set the vmax to the lowest possible value
    vmax = -np.inf

    for i in range(N):
        # First iteration: value = 2
        value = values[i]
        # Check whether this value is larger than any previous
        if value > vmax:
            # Update the index and the vmax
            imax = i
            vmax = value

    return imax


values = [2, 3, -1, 7, 4]
imax = argmax(values)
print(f'The maximum is located at {imax}')

# Compare to NumPy's argmax
j = np.argmax(values)
print(f'The maximum is located at {j}')





