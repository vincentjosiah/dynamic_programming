import time
import sys

memo = {}

def fib(n):
    global memo
    if n in memo: 
        print(str(n) + ": " + str(memo[n]))
        return memo[n]
    if n <= 2:  f = 1
    else:       f = fib(n-1) + fib (n-2)

    print(str(n) + ": " + str(f))
    memo[n] = f
    return f

start_time = time.time()
print(fib(int(sys.argv[1])))
print("Run-time: %s seconds" % (time.time() - start_time))