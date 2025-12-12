#Write a Python program to sort a dictionary (ascending /descending) by value.

#Ascending
d = {'a': 3, 'b': 1, 'c': 2}

items = list(d.items())

for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_d = dict(items)
print("Ascending:", sorted_d)

#descending
d = {'a': 3, 'b': 1, 'c': 2}

items = list(d.items())

for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_di = dict(items)
print("Descending:", sorted_di)

