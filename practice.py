work = {
    "Monday" : 5,
    "Tuesday" : 8,
    "Wednesday" : 6,
    "Thursday" : 7,
    "Friday" : 5,
}
work["Saturday"] = 5
work.pop(
    "Wednesday")
print(len(work))
if "Friday" in work:
    print(work)