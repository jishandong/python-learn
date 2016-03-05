from time import ctime,sleep
def fib(x):
    sleep(0.5)
    if x < 2:return 1
    return (fib(x-2)+fib(x-1))
def fac(x):
    sleep(0.5)
    if x < 2:return 1
    return(x * fac(x-1))
def sum(x):
    sleep(0.5)
    if x < 2:return 1
    return (x + sum(x-1))
print (fib(5),fac(5),sum(5))
