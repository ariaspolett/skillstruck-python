def assign_partner(students):
    students.sort()
    groups = []
    n = len(students)
    for x in range(n//2):
        pair = (students[x], students[n - 1 - x])
        groups.append(pair)
    if n % 2 == 1:
        middle_name = sorted_names[n // 2]
        groups.append((middle_name,))
    return groups
students = input("Enter the student names: ").split()
pairs = assign_partner(students)
print(pairs)