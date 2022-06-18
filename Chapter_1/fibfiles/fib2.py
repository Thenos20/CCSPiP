#returns the 10 first numbers in the fibonacci series

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)


if __name__ == "__main__":
    n = 0
    while fib2(n) < 10:
        print(fib2(n))
        n = n + 1
