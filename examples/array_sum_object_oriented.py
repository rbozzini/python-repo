class ChangeList(object):
    def __init__(self, any_list):
        self.any_list = any_list

    def do_add(self):
        self.sum = sum(self.any_list)

my_list = [1, 2, 3, 4, 5]
create_sum = ChangeList(my_list)
create_sum.do_add()
print(create_sum.sum)
