cols = [2, 5, 10, 100]
rows = [int(n) for n in input("Input a list of numbers").split()]
colls = [ ] 
for x in rows:
    col = []
    for y in cols:
        col.append(x - y)
    colls.append(col)
print(colls)