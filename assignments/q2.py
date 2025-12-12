#2. Write a Python program to count occurrences of a substring in a string.

#using in-built function

string = input("Enter the string: ")
substring = input("Enter the substring to count: ")
count = string.count(substring)
print("Occurrences of ",substring," in the string: ",count)


#without in bulit function.

string = input("Enter the main string: ")
sub = input("Enter the substring to find: ")

count = 0
a = len(string)
b = len(sub)

for i in range(a - b + 1):
    match = True
    for j in range(b):
        if string[i + j] != sub[j]:
            match = False
            break
    if match:
        count += 1

print("Occurrences:", count)