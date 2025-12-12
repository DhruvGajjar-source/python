#Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
#Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

d = {}

for num in lst:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

print(d)

