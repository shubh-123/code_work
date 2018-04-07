import time
import math

start_time = time.time()

num = 60085147514

# if number is prime, this function returns 1, else 0
def checkifprime(number):
    prime = 1
    factor = 2
    count = math.ceil(math.sqrt(number)) + 1
    while (factor < count and prime == 1):
        if(number % factor == 0):
            prime = 0
        factor += 1
    return prime;

isprime = 0
x = math.ceil(num / 2)
primefactor = 0

while (x > 1 and isprime == 0):
    if( num % x == 0 and checkifprime(x) == 1):
        isprime = 1
        print(x)
    x -= 1

if( x == 1):
    print(num, " is a prime number")
else:
    print("largest prime factor of ", num, " is ", x+1)

exec_time = time.time() - start_time

print("execution time is: ", exec_time, "sec")
