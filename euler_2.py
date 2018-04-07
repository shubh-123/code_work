import time

start_time = time.time()

count  = 0
x = 1
y = 1

while( x < 4000000 and y < 4000000):
    if(y % 2 == 0):
        count = count + y

    x = x + y
        
    if(x % 2 == 0):
        count = count + x
        
    y = y + x
    
print(count)

exec_time = time.time() - start_time

print("execution time is: ", exec_time, "sec")
