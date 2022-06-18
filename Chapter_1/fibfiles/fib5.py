def fib5(n: int)->int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
    return last

n = 0

while n < 2:
    print(fib5(n))
    n = n + 1
