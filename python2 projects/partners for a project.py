#THIS IS NOT CORRECT, STILL WORKING ON IT!!!
def assign_partner(students):
    students.sort()
    students.reverse()
    groups = []
    for x in range(len(students)//2):
        pair = (students[x], students[-(x + 1)])
        groups.append(pair)
    print(groups)
students = input("Enter the student names: ").split()
assign_partner(students)
#Percy Nico Jason Leo Will Grover 