# recursively solve problem

def add_two_nums(a, b):
    if b == 0:
        return a

    if b > 0:
        return add_two_nums(a + 1, b - 1)

print(add_two_nums(1, 4))