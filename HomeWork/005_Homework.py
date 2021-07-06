tupple_1 = (1, 2, 3, 4, 5, 8)
tupple_2 = (9, 10, 11, 12)

tupple_1 = list(tupple_1)
for x in tupple_2[::-1]:
    tupple_1.insert(2,x)

tupple_1 = tuple(tupple_1)
print(tupple_1)