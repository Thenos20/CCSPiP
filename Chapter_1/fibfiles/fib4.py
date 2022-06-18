from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n:int) -> int:
    if n<2:
        return n
    return fib4(n-2) + fib4(n-1)

n = 0
while n < 20:
    print(fib4(n))
    n = n + 1