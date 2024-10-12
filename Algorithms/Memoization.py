

memo = [None] * 100
counter = 0

def dyn_fib(n):
    global counter
    counter += 1
    
    # if memo[n] is not None:
    #     return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    # memo[n] = dyn_fib(n-1) + dyn_fib(n-2)
    return dyn_fib(n-1) + dyn_fib(n-2)
    # return memo[n]


dyn_fib(35)
print(counter)
