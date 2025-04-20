evens = [x for x in range(10) if x % 2 == 0 and x != 0]

def cuboid(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

def lowest_student_score_name():
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    lowest = min(students, key=lambda x: x[1])[1]
    return [x[0] for x in students if x[1] == lowest]

hi = lambda : 'hellow'

# Create a list of the cubes of all numbers from 1 to 10 using list comprehension.
cubes = [x**3 for x in range(1, 11)]

odds = list(filter(lambda x: x % 2 == 1, range(10)))

m = [x for x in range(1, 31) if x % 5 == 0]

n = list(map(lambda x: x**2, range(1, 11)))

words = ["apple", "ant", "banana", "avocado", "berry", "apricot"]

w = [x for x in words if len(x) > 5]

print(m)
print(n)
print(w)
