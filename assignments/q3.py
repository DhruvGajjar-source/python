#Write a Python program to count the occurrences of each word in a givensentence

sentence = input("Enter a sentence: ")

words = sentence.lower().split()
count = {}

for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("Occurrences of each word : ")
for j, k in count.items():
    print(j, ":", k)
