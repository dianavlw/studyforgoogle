Project Euler

Notes:

a[-1] is the last elementin array
a[-2] is the second to last element in array
s[::-1] reversed the string #splice a string, backwards 
for i in range(n) loop

Factors and Multiples:

Factor aka divisor of a number even divides it:
10 is a factor of 20
20 // 10 = 2

3 is a factor of 12 
12 / 3 == 4

Multiple of a number n is any integer times n:
20 is a multiple of 10
10 * 2 = 20
12 is a multple of 3
3 * 4 = 12

Problem 1.

Multiples of 3 and 5.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

solve by using a for loop

sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
         sum += i
print(sum)

Problem 2. 
Even Fibonacci Numbers.
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib = [1, 2]

while True:
  next = fib[-1] + fib[-2]
  if next > 4000000:
    break
  fib.append(next)
#getting all the fib numbers
sum = 0
for n in fib:
  if n % 2 == 0:
    sum += n
#printing all the even fib nums
print(sum)

Problem 3. 
Largest Prime Factor:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

#generate prime num then check if its a prime factor
# A factor is a whole number that evenly divides another number. 
# That is, dividing the number by the factor results in a remainder of 0. 
#For example, the factors of 4 are -4 , -2 , -1 , 1 , 2 , and 4 .
24 = 4 * 6
24 = 24 * 1
24 = 2 * 12
12 = 2 * 6
6 = 2 * 3
3 = 3* 1
24 is not a prime number, its not a perfect square.
Prime factors are factors of a number that are, themselves, prime numbers. 
#list all primes or number = 600851475143
primes = []
i = 2
n = 600851475143

while i * i <=n:
    is_prime = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i
    i += 1
print(primes)

#get largest
largest_prime = 0
for p in primes:
    if n %. p == 0:
       largest_prime = p
print(largest_prime)
                      
OR
def largestPrime(n):
  i = 2
  while i<n:
    if n%i == 0:
        n = n//i
    else:
      i += 1
  return n
print(largestPrime(600851475143))

Problem 4. 
                      
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.                     
# 3-digit number starts at 100 up to but not including 1000
largest_pali = 0

for a in range(100, 1000):
    for b in range(a, 1000):
        c = a * b
        s = str(c)
        if s == s[::-1]: #reverse a string
           if c > largest_pali:
              largest_pali = c
print(largest_pali)

Problem 5.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

GCD: Greates Common Divisor
5 is gcd of 15 and 25
12 is for 12 and 24
                      
LCM = Least Common Multiple                     
30 is the lcm of 10 and 15                       
24 is the lcm of 12 and 24
                      
            2520 = 2*2*2*3*5*7 
             /\         
         252   10        
         /\    /\          
       126(2)(5)(2)   
       /\               
     63 (2)               
     /\                 
    9 (7)               
   /\                   
  (3)(3)                  
                      
def check(n):
   for i in range(11, 21):
     if n % i ==0:
       continue
    else:
       return True
   return True
                      
                      
x = 2520
 while not check(x):
  x += 2520
print(x)
                      
                      
                      
                      
                      
                      
                      
