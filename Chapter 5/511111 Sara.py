def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

rows = [ ] #input for rows
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

for r in range(9): #make sure rows are acceptable
    if not checkset(rows[r]):
        ok = False
        break

if ok:
    for c in range(9): #make sure columns are acceptable
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

if ok:
    for r in range(0, 9, 3): #each row has 0-9
        for c in range(0, 9, 3): #each column has 0-9
            sqr = ''
            for i in range(3): #make sure squares are acceptable
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

if ok:
    print("Yes")
else:
    print("No")
