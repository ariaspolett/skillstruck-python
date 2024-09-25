lists = []
students = int(input("How many students took the test?"))
while students > 0:
    score = [n for n in input("Enter the student name and grade").split(" ")]
    lists.append(score)
    students -= 1

def get_top_scores(lists):
    maxi = 0
    top_students = []

    for entry in lists:
        name, score = entry[0], int(entry[1])
        if score > maxi:
            maxi = score
            top_students = [name]
        elif score == maxi:
            top_students.append(name)
    return top_students
    
top_students = get_top_scores(lists)
print(top_students)