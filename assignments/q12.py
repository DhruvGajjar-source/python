#Write a Python program to convert a list of tuples into a dictionary.

#direct method
l = [('a', 1), ('b', 2), ('c', 3)]
result = dict(l)

print(result)

#using loop
result = {}
for key, value in l:
    result[key] = value

print(result)
