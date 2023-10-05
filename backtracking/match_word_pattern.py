def matchWordPattern(pattern: str, input_string: str) -> bool:
    """
    Determine if a given pattern matches a string using backtracking.

    pattern: The pattern to match.
    input_string: The string to match against the pattern.
    return: True if the pattern matches the string, False otherwise.

    >>> matchWordPattern("aba", "GraphTreesGraph")
    True

    >>> matchWordPattern("xyx", "PythonRubyPython")
    True

    >>> matchWordPattern("GG", "PythonJavaPython")
    False
    """

    def backtrack(pattern_index, str_index):
        if pattern_index == len(pattern) and str_index == len(input_string):
            return True
        if pattern_index == len(pattern) or str_index == len(input_string):
            return False

        char = pattern[pattern_index]

        if char in pattern_map:
            mapped_str = pattern_map[char]
            if input_string.startswith(mapped_str, str_index):
                return backtrack(pattern_index + 1, str_index + len(mapped_str))
            else:
                return False

        for end in range(str_index + 1, len(input_string) + 1):
            substr = input_string[str_index:end]
            if substr in str_map:
                continue

            pattern_map[char] = substr
            str_map[substr] = char

            if backtrack(pattern_index + 1, end):
                return True

            del pattern_map[char]
            del str_map[substr]
        return False

    pattern_map = {}
    str_map = {}
    return backtrack(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
