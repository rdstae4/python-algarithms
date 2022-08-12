class MaxFenwickTree:
    """
    Maximum Fenwick Tree

    More info: https://cp-algorithms.com/data_structures/fenwick.html
    ---------
    >>> ft = MaxFenwickTree(5)
    >>> ft.query(0, 5)
    0
    >>> ft.update(4, 100)
    >>> ft.query(0, 5)
    100
    >>> ft.update(4, 0)
    >>> ft.update(2, 20)
    >>> ft.query(0, 5)
    20
    >>> ft.update(4, 10)
    >>> ft.query(2, 5)
    20
    >>> ft.update(2, 0)
    >>> ft.query(0, 5)
    10
    >>> ft = MaxFenwickTree(10000)
    >>> ft.update(255, 30)
    >>> ft.query(0, 10000)
    30
    """

    def __init__(self, size: int) -> None:
        """
        Create empty Maximum Fenwick Tree with specified size

        Parameters:
            size: size of Array

        Returns:
            None
        """
        self.size = size
        self.arr = [0] * (size + 1)
        self.tree = [0] * (size + 1)

    @staticmethod
    def get_next(index: int) -> int:
        """
        Get next index in O(1)
        """
        return index + (index & -index)

    @staticmethod
    def get_prev(index: int) -> int:
        """
        Get previous index in O(1)
        """
        return index - (index & -index)

    def update(self, index: int, value: int) -> None:
        """
        Set index to value in O(lg^2 N)

        Parameters:
            index: index to update
            value: value to set

        Returns:
            None
        """
        self.arr[index] = value
        index += 1  # 1-indexed
        while index < self.size + 1:
            self.tree[index] = max(value, self.query(self.get_prev(index), index))
            index = self.get_next(index)

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range [l, r) in O(lg^2 N)

        Parameters:
            left: left index of query range (inclusive)
            right: right index of query range (exclusive)

        Returns:
            Maximum value of range [left, right)
        """
        result = 0
        while left < right:
            current_left = self.get_prev(right)
            if left < current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right - 1])  # Because of right is exclusive
                right -= 1
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
