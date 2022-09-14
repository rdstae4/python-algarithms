from timeit import timeit


def sum_of_digits(n: int) -> int:
	"""
	Find the sum of digits of a number.

	>>> sum_of_digits(12345)
	15
	>>> sum_of_digits(123)
	6
	>>> sum_of_digits(-123)
	6
	>>> sum_of_digits(0)
	0
	"""
	n = -n if n < 0 else n
	res = 0
	while n > 0:
		res += n % 10
		n = n // 10
	return res


def sum_of_digits_recursion(n: int) -> int:
	"""
	Find the sum of digits of a number using recursion

	>>> sum_of_digits_recursion(12345)
	15
	>>> sum_of_digits_recursion(123)
	6
	>>> sum_of_digits_recursion(-123)
	6
	>>> sum_of_digits_recursion(0)
	0
	"""
	n = -n if n < 0 else n
	return n if n < 10 else n % 10 + sum_of_digits(n // 10)


def sum_of_digits_compact(n: int) -> int:
	"""
	Find the sum of digits of a number

	>>> sum_of_digits_compact(12345)
	15
	>>> sum_of_digits_compact(123)
	6
	>>> sum_of_digits_compact(-123)
	6
	>>> sum_of_digits_compact(0)
	0
	"""
	return sum(int(c) for c in str(abs(n)))


def digital_root(n: int) -> int:
	"""
	finding the digital root of n
	https://en.wikipedia.org/wiki/Digital_root

	>>> digital_root(394328)
	2
	>>> digital_root(-394328)
	-1
	>>> digital_root(123)
	6
	>>> digital_root(0)
	0
	>>> digital_root("109820394")
	-1
	"""

	try:
		return n % 9 or n & 9 if n >= 0 else -1
	except TypeError:
		return -1


def benchmark() -> None:
	"""
	Benchmark code for comparing 4 functions,
	with 3 different length int values.
	"""
	print("\nFor small_num = ", small_num, ":")
	print(
		"> sum_of_digits()",
		"\t\tans =",
		sum_of_digits(small_num),
		"\ttime =",
		timeit("z.sum_of_digits(z.small_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_recursion()",
		"\tans =",
		sum_of_digits_recursion(small_num),
		"\ttime =",
		timeit("z.sum_of_digits_recursion(z.small_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_compact()",
		"\tans =",
		sum_of_digits_compact(small_num),
		"\ttime =",
		timeit("z.sum_of_digits_compact(z.small_num)", setup="import __main__ as z"),
		"seconds",
	)
	result = timeit("z.digital_root(z.small_num)", setup="import __main__ as z")
	print(f"> digital_root()\tans = {digital_root(small_num)}\ttime = {result} seconds")

	print("\nFor medium_num = ", medium_num, ":")
	print(
		"> sum_of_digits()",
		"\t\tans =",
		sum_of_digits(medium_num),
		"\ttime =",
		timeit("z.sum_of_digits(z.medium_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_recursion()",
		"\tans =",
		sum_of_digits_recursion(medium_num),
		"\ttime =",
		timeit("z.sum_of_digits_recursion(z.medium_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_compact()",
		"\tans =",
		sum_of_digits_compact(medium_num),
		"\ttime =",
		timeit("z.sum_of_digits_compact(z.medium_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> digital_root()",
		"\t\tans =",
		digital_root(medium_num),
		"\ttime =",
		timeit("z.digital_root(z.medium_num)", setup="import __main__ as z"),
		"seconds",
	)

	print("\nFor large_num = ", large_num, ":")
	print(
		"> sum_of_digits()",
		"\t\tans =",
		sum_of_digits(large_num),
		"\ttime =",
		timeit("z.sum_of_digits(z.large_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_recursion()",
		"\tans =",
		sum_of_digits_recursion(large_num),
		"\ttime =",
		timeit("z.sum_of_digits_recursion(z.large_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> sum_of_digits_compact()",
		"\tans =",
		sum_of_digits_compact(large_num),
		"\ttime =",
		timeit("z.sum_of_digits_compact(z.large_num)", setup="import __main__ as z"),
		"seconds",
	)
	print(
		"> digital_root()",
		"\tans =",
		digital_root(large_num),
		"\ttime =",
		timeit("z.digital_root(z.large_num)", setup="import __main__ as z"),
		"seconds",
	)


if __name__ == "__main__":
	small_num = 262144
	medium_num = 1125899906842624
	large_num = 1267650600228229401496703205376
	benchmark()
	import doctest

	doctest.testmod()
