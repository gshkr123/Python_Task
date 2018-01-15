with open('file.csv') as f:
    r=reader(f)
    for r in row:
        print (row)

with open('file.csv', 'w') as f:
    w=csv.writer(f)
    w.writerow(["fluffy", "cat"])
    w.writerow(["plummy", "dummy"])
