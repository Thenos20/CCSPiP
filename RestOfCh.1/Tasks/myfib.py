based = {0: 0, 1: 1}


def my_fib(n):
    if n not in based:
        based[n] = my_fib(n-1) + my_fib(n - 2)
    return based[n]


no = 0
while no < 2:
    print(my_fib(no))
    no = no + 1
