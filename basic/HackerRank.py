evens = [x for x in range(10) if x % 2 == 0 and x != 0]

def cuboid(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

def lowest_student_score_name():
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    lowest = min(students, key=lambda x: x[1])[1]
    return [x[0] for x in students if x[1] == lowest]

print(lowest_student_score_name())


