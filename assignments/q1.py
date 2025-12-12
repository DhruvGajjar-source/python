#1. Write a python program to sum of the first n positive integers.

n=int(input("Enter a number till you want sum : "))
sum=0
for i in range(0,n):
    sum+=i
print("Sum of number is : ",sum)