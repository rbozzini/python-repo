def do_add(any_list):
    sum = 0
    for x in any_list:
        sum += x
    return sum

my_list = [1, 2, 3, 4, 5]
print(do_add(my_list))
