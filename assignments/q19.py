#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

def unique_elements(lst):
    u_lst = []
    for i in lst:
        if i not in u_lst:
            u_lst.append(i)
    return u_lst

l = [1, 2, 2, 3, 4, 4, 5, 1]
new_list = unique_elements(l)
print("Unique list : ", new_list)
