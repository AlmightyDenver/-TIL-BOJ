from timeit import default_timer as timer

n = int(input())
TT = []
start = timer()

#Fibonacci Numbers
def Fib(n):
    if n == 1 or n ==2:
        return 1
    return Fib(n-2) + Fib(n-1)
print(Fib(n))

stop = timer()
T = stop - start
print('Funct : ' + str(T))



#Fibonacci Numbers Memozation

start = timer()

#Memoz1
def fib(n):
    if n in fib.cache:
        return fib.cache[n]
    ret = fib(n-2) + fib(n-1)
    fib.cache[n] = ret
    return ret
fib.cache = {1:1, 2:1}

print(fib(n))

stop = timer()
T = stop - start
print('Memoz1 : ' + str(T))

#Memoz2

start = timer()

class Memoz(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret
@Memoz
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(n))

stop = timer()
T = stop - start
print('Memoz2 : ' + str(T))

#Fibonacci Numbers Dynamic Programming
start = timer()

def fib(n):
    f = [-1] * (n + 1)
    return fib_helper(n, f)


def fib_helper(n, f):
    if f[n] > 0:
        return f[n]
    if n == 0 or n == 1:
        q = n
    else:
        q = fib_helper(n - 2, f) + fib_helper(n - 1, f)
    f[n] = q

    return q

print(fib(n))

stop = timer()
T = stop - start
print('DP : ' + str(T))
