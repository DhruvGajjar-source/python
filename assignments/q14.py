#Write a Python program to find the highest 3 values in a dictionary.

d = {'a': 3, 'b': 1, 'c': 2, 'd': 8, 'e': 5}

items = list(d.items())

for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

d1 = dict(items[:3])
print(d1)
