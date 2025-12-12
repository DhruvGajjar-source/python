#Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2,3),(4,5,6),(7,8,9)]
l1 = []

for i in range(len(l)):
    for j in range(len(l[i])):
        l1.append(l[i][j])
    print(l1)
    l1.clear()
