# reverse string

def reverse_string(s):
    print(s[::-1])

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

# write a function that find all pairs that sum to zero, and return list of that pairs

def find_sum_to_zero(ls):
    n = len(ls)
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            print(f"first = {ls[i]}, second = {ls[j]}")
            if ls[i] + ls[j] == 0:
                pairs.append((ls[i], ls[j]))
    
    return pairs


momentum = [3, -1, 2, -3, 1, -2, 4]
# print(find_sum_to_zero(momentum))
t = [1, 2, 4, 3, 8, 8]

def t_test(ls):
    n = len(ls)

    for i in range(n):
        for j in range(i + 1, n):
            pass

def find_runner_up(ls):
    clean_ls = list(set(t))
    print(clean_ls)
    sorted_list = sorted(clean_ls, reverse=True)
    return sorted_list[1]


print(find_runner_up(t))
