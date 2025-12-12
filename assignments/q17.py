#Write a python program using function to find the sum of odd series and even series
#Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
#Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def odd_series_sum(n):
    sum_odd = 0
    for i in range(1, n+1, 2):
        n1 = i*10 + 2
        sum_odd += n1 / factorial(i)
    return sum_odd

def even_series_sum(n):
    sum_even = 0
    for i in range(2, n+1, 2):
        n1 = i*10 + 2
        sum_even += n1 / factorial(i)
    return sum_even

n = int(input("Enter the value of n: "))

sum_odd = odd_series_sum(n)
sum_even = even_series_sum(n)

print("Sum of odd series:", sum_odd)
print("Sum of even series:", sum_even)
