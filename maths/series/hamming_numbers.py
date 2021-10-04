"""
Run the doctests with the following command:
python3 -m doctest -v hamming_numbers.py
or
python -m doctest -v hamming_numbers.py
For manual testing run:
python3 hamming_numbers.py

"""


def hamming(n_element: int) -> list:
    """
    A Hamming number is a positive integer of the form 2^i*3^j*5^k, for some
    non-negative integers i, j, and k.
    More info at: https://en.wikipedia.org/wiki/Regular_number .

    This function creates an ordered list of n length as requested, and afterwards
    returns the last value of the list. It must be given a positive integer.

    :param n_element: The number of elements on the list
    :return: The nth element of the list

        Examples:
    >>> hamming(5)
    [1, 2, 3, 4, 5]
    >>> hamming(10)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    >>> hamming(15)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    """
    n_element = int(n_element)
    if n_element < 1:
        my_error= ValueError("a should be a positive number")
        raise my_error

    hamming_list = [1]
    i, j, k = (0, 0, 0)
    index = 1
    while index < n_element:
        while hamming_list[i] * 2 <= hamming_list[-1]:
            i += 1
        while hamming_list[j] * 3 <= hamming_list[-1]:
            j += 1
        while hamming_list[k] * 5 <= hamming_list[-1]:
            k += 1
        hamming_list.append(
            min(hamming_list[i] * 2, hamming_list[j] * 3, hamming_list[k] * 5)
        )
        index += 1
    return hamming_list


if __name__ == "__main__":
    n = input("Enter the last number (nth term) of the Hamming Number Series: ")
    print("Formula of Hamming Number Series => 2^i * 3^j * 5^k")
    hamming_numbers = hamming(n)
    print("-----------------------------------------------------")
    print(f"The list with nth numbers is: {hamming_numbers}")
    print("-----------------------------------------------------")
