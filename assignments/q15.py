#Given a number n, write a python program to make and print the list of Fibonacci
#series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output :
#First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

n = int(input("Enter n: "))
fib = [0, 1]

for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])
print(fib)
