#Write a Python program to check whether a list contains a sublist.

lst = [1,2,3,4,5,6,7]
s_list = [5,6,7]

l = len(lst)
s = len(s_list)
found = False

for i in range(l - s + 1):  
    if lst[i:i+s] == s_list:
        print("Sublist found!!")
        found = True
        break

if found == False:
    print("Sublist not found!")
