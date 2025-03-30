# reverse string

def reverse_string(s):
    print(s[::-1])

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

reverse_string("Hello")
print(factorial(4))