#Write a Python program to get a single string from two given strings, separatedbya space and swap the first two characters of each string.

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

nstr1 = str2[:2] + str1[2:]
nstr2 = str1[:2] + str2[2:]

str3 = nstr1 + " " + nstr2
print(str3)