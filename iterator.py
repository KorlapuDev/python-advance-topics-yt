nums = [10, 20, 30]

# Iterable se Iterator banaya
my_iterator = iter(nums)

# Ab values manually nikalte hain
print(next(my_iterator)) # Output: 10
print(next(my_iterator)) # Output: 20
print(next(my_iterator)) # Output: 30
print(next(my_iterator)) # Output: StopIteration Error!