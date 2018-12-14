import functools

my_list = [1, 2, 3, 4, 5]


def add_it(x, y):
    print("add_it(" + str(x) + ", " + str(y) + ")")
    return (x + y)

# https://docs.python.org/3/library/functools.html

# Functional:
sum = functools.reduce(add_it, my_list)
print(sum)

# Lambda:
sum = functools.reduce(lambda x, y: x + y, my_list)
print(sum)

# Imperative:
sum = 0
for x in my_list:
    sum += x
print(sum)
