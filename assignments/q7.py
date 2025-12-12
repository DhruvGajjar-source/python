#Program to find Greatest Common Divisor of two numbers. For example, 
#theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
num = min(n1,n2)
gcd = 1

for i in range(1,num+1):
    if n1%i == 0 and n2%i == 0:
        gcd = i 
        
print("Gratest Common Divisor is : ",gcd)
