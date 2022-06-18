memo = {0: 0, 1: 1}


def fib3(n):
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n - 2)
    return memo[n]


if __name__ == "__main__":
    n = 0
    while n < 20:
        print(fib3(n))
        n = n + 1
