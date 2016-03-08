'对函数做性能分析和计时统计'
import time
from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        r = func(*args,**kwargs)
        end = time.perf_counter()
        print('{}.{}:{}'.format(func.__module__,func.__name__,end-start))
        return r
    return wrapper
@timethis
def countnumber(n): #计时的主程序，只要将该部分代替即可
    while n>0:
        n -= 1
countnumber(10000)
