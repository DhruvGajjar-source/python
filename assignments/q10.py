#Write a Python program to get unique values from a list.

l = [1,3,2,1,3,6,3,9,8]
Unq_list = []
for i in l:
    if i not in Unq_list:
        Unq_list.append(i)
print(Unq_list)