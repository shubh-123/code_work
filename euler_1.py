import time

start_time = time.time()

count  = 0
for x in range (0, 1000):
    if (x % 3 == 0) | (x % 5 == 0):
        count = count + x
        
print(count)

exec_time = time.time() - start_time

print("execution time is: ", exec_time, "sec")

