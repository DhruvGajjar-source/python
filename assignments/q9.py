#Write a Python program to find the second smallest number in a list.

list = [11,21,9,6,23,61,7]

for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i + 1]:
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp
print(list[1])
