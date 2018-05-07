a = [2, 3, 4, 5, 6, 7, 8, 9, 0]
xyz = [0, 12, 4, 6, 242, 7, 9]
for x in xyz:
    if x in a:
        print(x)

print([x for x in xyz if x in a])
