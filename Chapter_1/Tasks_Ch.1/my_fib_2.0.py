from functools import lru_cache


@lru_cache(maxsize=None)
def my_fib2(n):
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
    return last


n = 0
while n < 20:
    print(my_fib2(n))
    n = n + 1
