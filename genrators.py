def sampleGenFunc():
    #some code here
    yield 1
    yield 2
    yield 3

x = sampleGenFunc()
# print(x)
# print(next(x)) # Output: 1
# print(next(x)) # Output: 2
# print(next(x)) # Output: 3

# for i in x:
#     print(i)