# Print

# Lenght

# Range range(start, stop, step)
"""Create a sequence of numbers."""

print("My list of numbers using manual input:")
NumberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print(NumberList)

print("My list of numbers using range:")
NumberListByRangeFunction = list(range(0, 11))
print(NumberListByRangeFunction)

print("My list of numbers using range with step of 10:")
NumberListByRangeFunction = list(range(10, 101, 10))
print(NumberListByRangeFunction)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object with a *.  The * "unpacks" an iterable, so that each element is passed as a separate argument, rather than the function receiving the iterable object as a single argument:
nums_list2 = [*range(1,12,2)]
print(nums_list2)


